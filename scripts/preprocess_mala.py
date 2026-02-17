import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from pathlib import Path
from dataclasses import dataclass
import warnings


@dataclass
class GPR:
    """Convenience container for the three essential Ramac files."""
    rd3: np.ndarray
    rad: dict[str, str]
    cor: pd.DataFrame

def load_ramac(rad_filepath: Path, rd3_filepath: Path | None = None, cor_filepath: Path | None = None) -> GPR:
    """Load a Malå Ramac file into memory.

    Parameters
    ----------
    rad_filepath
        The input filepath to the data. Must end with ".rad"
    rd3_filepath
        Optional. The filepath to the rd3 file. If not given, it's assumed to lie beside the ".rad" file.
    cor_filepath
        Optional. The filepath to the cor file. If not given, it's assumed to lie beside the ".rad" file.

    Returns
    -------
    A loaded GPR class.
    """
    if rad_filepath.suffix != ".rad":
        raise ValueError(f"Possibly wrong rad_filepath provided: {rad_filepath}")
    # If rd3 or cor filepaths aren't given, assume that they're beside the rad file
    if rd3_filepath is None:
        rd3_filepath = rad_filepath.with_suffix(".rd3")
    if cor_filepath is None:
        cor_filepath = rad_filepath.with_suffix(".cor")

    # Read the rad (metadata/header) file
    rad = {}
    for line in rad_filepath.read_text().splitlines():
        key, value = line.split(":")
        rad[key.strip()] = value.strip()

    # Read the cor (coordinate) file
    cor = pd.read_csv(cor_filepath, sep="\t", header=None)

    # Read the rd3 (radargram) file
    rd3 = np.fromfile(rd3_filepath, dtype="<i2").reshape((-1, int(rad["SAMPLES"]))).T

    return GPR(rd3, rad, cor)
    
def remove_empty_traces(gpr: GPR) -> GPR:
    """Remove any trace without data (sum=0).

    This also removes any coordinate associated with that trace.
    """
    # Find which indices to keep (which are not empty traces)
    keep = np.argwhere(np.sum(np.abs(gpr.rd3), axis=0) > 0).ravel()

    if keep.size == gpr.rd3.shape[1]:
        return gpr

    # Identify with corfile points correspond to traces that should not be removed.
    # Note that corfiles are 1-based (hence the +1).
    keep_mask = np.isin(gpr.cor[0], keep + 1)
    # Keep only the non-empty traces in the corfile
    cor = gpr.cor.loc[keep_mask].copy()

    # Re-align the cor trace counter with the now shorter rd3
    cor[0] = np.searchsorted(keep + 1, cor[0]) + 1 

    rd3 = gpr.rd3[:, keep]

    n_removed = gpr.rd3.shape[1] - rd3.shape[1]

    print(f"Removed {n_removed} empty traces")

    rad = gpr.rad.copy()
    rad["LAST TRACE"] = str(rd3.shape[1])

    return GPR(rd3=rd3, rad=rad, cor=cor)



def save_ramac(output_rad_filepath: Path, gpr: GPR) -> None:
    """Save a Malå Ramac file to disk.

    Parameters
    ----------
    output_rad_filepath
        The output filepath of the corrected data. Must end with ".rad". Other files are saved beside it.
    """
    if output_rad_filepath.suffix != ".rad":
        raise ValueError("The output rad file must have a '.rad' suffix")
    cor_filepath = output_rad_filepath.with_suffix(".cor")
    rd3_filepath = output_rad_filepath.with_suffix(".rd3")

    rad_text = "\n".join([f"{key}: {value}" for key, value in gpr.rad.items()])
    output_rad_filepath.write_text(rad_text)

    gpr.cor.to_csv(cor_filepath, sep="\t", header=False, index=False)

    gpr.rd3.astype("int16").T.ravel().tofile(rd3_filepath, format="<i2")


def replace_gps_track(gpr: GPR, gps_filepath: Path):
    """Replace the coordinate information of the corfile with an external track.

    The function assumes that the track and corfile times are synchronized.

    Only a specific track format is supported (used by the Austfonna field campaigns)
    """
    import geopandas as gpd
    import scipy.interpolate

    track = gpd.read_file(gps_filepath)
    # Convert the date to seconds since 2000. This is used for synchronization
    track["time"] = (pd.to_datetime(track["yyyymmdd"].astype(str) + track["HHMMSS"].astype(str), format="%Y%m%d%H%M%S") - pd.Timestamp("2000-01-01")).dt.total_seconds()
    # Adjust the GPS time offset 
    track["time"] -= 18

    coords = gpr.cor.copy()
    # Convert the date to seconds since 2000. This is used for synchronization
    coords["time"] = (pd.to_datetime(coords[1] + coords[2], format="%Y-%m-%d%H:%M:%S") - pd.Timestamp("2000-01-01")).dt.total_seconds()

    if track["time"].max() < coords["time"].min() or track["time"].min() > coords["time"].max():
        warnings.warn("Track and corfile do not align in time. Continuing without correction.")
        return gpr

    # All this block is only for validation.
    # This will convert to m coordinates, compare the two GPSes, and print the result.
    coords = gpd.GeoDataFrame(coords, geometry=gpd.points_from_xy(coords[5], coords[3], crs=4326)).to_crs(track.crs)
    for coord in ["x", "y"]:
        model = scipy.interpolate.interp1d(track["time"], getattr(track.geometry, coord))
        new_coords = model(coords["time"])
        coord_std = (getattr(coords.geometry, coord) - new_coords).std()
        print(f"Correcting track with an {coord} stdev of {coord_std:.2f} m")


    # Interpolate the track's coordinates to the corfile's times
    coords[5] = scipy.interpolate.interp1d(track["time"], track["Longitude"])(coords["time"])
    coords[3] = scipy.interpolate.interp1d(track["time"], track["Latitude"])(coords["time"])
    coords[7] = scipy.interpolate.interp1d(track["time"], track["h_wgs"])(coords["time"])

    return GPR(gpr.rd3, gpr.rad, coords[gpr.cor.columns])


def preprocess_mala(
    output_rad_filepath: Path,
    input_rad_filepath: Path,
    input_rd3_filepath: Path | None = None,
    input_cor_filepath: Path | None = None,
    better_gps_path: Path | None = None
    ):
    """Run preprocessing steps for a Malå Ramac (rd3) dataset.

    1. Removes empty traces (if any)
    2. Corrects the coordinate information with an external track.

    Parameters
    ----------
    output_rad_filepath
        The output filepath of the corrected data. Must end with ".rad". Other files are saved beside it.
    input_rad_filepath
        The input filepath to the data. Must end with ".rad"
    input_rd3_filepath
        Optional. The filepath to the rd3 file. If not given, it's assumed to lie beside the ".rad" file.
    input_cor_filepath
        Optional. The filepath to the cor file. If not given, it's assumed to lie beside the ".rad" file.
    better_gps_path
        Optional. The external track to replace the corfile contents with.
    """
    print(f"Loading {input_rad_filepath}")
    gpr = load_ramac(rad_filepath=input_rad_filepath, rd3_filepath=input_rd3_filepath, cor_filepath=input_cor_filepath)

    gpr = remove_empty_traces(gpr)
    if better_gps_path is not None:
        gpr = replace_gps_track(gpr, gps_filepath=better_gps_path)

    print(f"Saving {output_rad_filepath}")
    output_rad_filepath.parent.mkdir(exist_ok=True, parents=True)
    save_ramac(output_rad_filepath=output_rad_filepath, gpr=gpr)

    

def run_test():

    better_gps_path = Path("/home/erikmann/Downloads/kinematic2025_ppp_1s_radar.zip")
    rad_filepath = Path("/home/erikmann/Downloads/OneDrive_1_12-02-2026/DAT_0002_B1.rad")
    temp_path = Path("temp/gpr0002.rad")
    temp_path.parent.mkdir(exist_ok=True)

    preprocess_ramac(output_rad_filepath=temp_path, rad_filepath=rad_filepath, better_gps_path=better_gps_path)


if __name__ == "__main__":
    run_test()


    
