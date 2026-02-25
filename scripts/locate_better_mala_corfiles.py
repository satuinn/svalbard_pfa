import geopandas as gpd
import pandas as pd
import numpy as np

from pathlib import Path

def corfile_colnames() -> list[str]:
    return ["trace_n", "date_str", "time_str", "lat", "lat_ref", "lon", "lon_ref", "alt", "M", "1"]

def expected_dtypes() -> dict[str, type | str]:
    return {
        "trace_n": int,
        "date_str": str,
        "time_str": str,
        "lat": float,
        "lat_ref": str,
        "lon": float,
        "lon_ref": str,
        "alt": str,
        "M": str,
        "1": str,
    }

def read_corfile(filepath: Path) -> gpd.GeoDataFrame:
    """Read a corfile into memory."""
    data = pd.read_csv(filepath, sep=r"\s+", header=None, names=corfile_colnames())

    # Remove unlikely points
    data = data[(data["lat"] > 70) & (data["lat"] < 81) & (data["lon"] > 10) & (data["lon"] < 25)]

    data = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data["lon"], data["lat"], crs=4326))

    if data.shape[0] == 0:
        return data

    # Set the index to the datetime it represents (useful for syncing)
    data.index = pd.to_datetime(data["date_str"] + "T" + data["time_str"])

    data = data.loc[~data.index.duplicated(keep="first")]

    return data


def save_corfile(filepath: Path, cor_data: gpd.GeoDataFrame):
    """Save a corfile."""
    cor_data = cor_data[corfile_colnames()]

    for key, dtype in expected_dtypes().items():
        cor_data[key] = cor_data[key].astype(dtype)

    cor_data.to_csv(filepath, sep="\t", header=False, index=False)

def find_other_corfiles(orig_corfile_path: Path, disallow_same_dir: bool = True, max_level: int = 2):
    """Find other corfiles close by that may be candidates for improved coordinate data.

    Parameters
    ----------
    orig_corfile_path
        The path of the original corfile
    disallow_same_dir
        Don't look in the same directory as the corfile (only in other dirs)
    max_level
        Maximum amount of directory levels to look back. e.g. 2 for a/b/c will look in a/

    """
    orig_corfile_path = orig_corfile_path.absolute()

    for other_filepath in orig_corfile_path.parents[max_level].rglob("*.*"):
        if other_filepath.suffix.lower() != ".cor":
            continue
        if other_filepath == orig_corfile_path:
            continue
        if disallow_same_dir and other_filepath.parent == orig_corfile_path.parent:
            continue
        yield other_filepath


def corfiles_compatible(first: gpd.GeoDataFrame, second: gpd.GeoDataFrame) -> tuple[float, gpd.GeoDataFrame] | tuple[None, None]:
    """Check if corfiles are compatible in time, and return the second if yes.

    Parameters
    ----------
    first
        The "reference" corfile to test the candidate on
    second
        The "candidate" corfile that may be a replacement

    Returns
    -------
    If they are not compatible, (None, None) is returned

    If they are compatible, the NMAD in northing (m) is returned
    and the candidate, aligned to the times of the reference.
    """

    trace_n_overlap = first["trace_n"].isin(second["trace_n"])
    if not np.any(trace_n_overlap):
        return None, None

    # Merge on datetime and only retain the rows that occur in both datasets 
    joined = first.merge(second, left_index=True, right_index=True, how="inner")

    # If the merged version is significantly shorter than the original, they're probably not a match.
    if (joined.shape[0] / first.shape[0]) < 0.3:
        return None, None

    diffs = joined["lat_x"].values - joined["lat_y"].values
    lat_nmad = 1.4826 * np.nanmedian(np.abs((diffs - np.nanmedian(diffs)))) * 111132

    return lat_nmad, second.loc[joined.index]


def replace_corfile(orig_corfile: Path) -> Path | None:
    """Attempt to replace a corfile with a corrected one by looking in nearby directories.

    Parameters
    ----------
    orig_corfile
        The original corfile where a replacement candidate should be found

    Returns
    -------
    If a candidate is found:
        A path to a corrected corfile, saved in a temporary directory.
    If no candidate is found:
        None
    """
    corfile = read_corfile(orig_corfile)

    temp_dir = Path("temp_corfiles/")
    temp_fp = temp_dir / "corfile_0000.cor"

    if temp_fp.is_file():
        for i in range(10000):
            temp_fp = temp_dir / f"corfile_{str(i).zfill(4)}.cor" 
            if not temp_fp.is_file():
                break

    for other in find_other_corfiles(orig_corfile):

        diff, better_cor = corfiles_compatible(corfile, read_corfile(other))

        # This means: If the corfile was not compatible in time
        if diff is None or better_cor is None:
            continue

        # If the difference is almost nothing, it's likely the same corfile as the original but with a different name
        # If the difference is very large, it was collected at the same time but somewhere else.
        if diff < 0.01 or diff > 30:
            continue

        print(f"Replacing {orig_corfile.name} with {other.name}: {diff:.2f} m difference") 

        temp_fp.parent.mkdir(exist_ok=True)
        save_corfile(temp_fp, better_cor)
        return temp_fp

   
