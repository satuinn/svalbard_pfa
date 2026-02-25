import geopandas as gpd
import pandas as pd
import numpy as np

from pathlib import Path

def corfile_colnames() -> list[str]:
    return ["trace_n", "date_str", "time_str", "lat", "lat_ref", "lon", "lon_ref", "alt", "M", "1"]

def read_corfile(filepath: Path) -> gpd.GeoDataFrame:

    data = pd.read_csv(filepath, sep=r"\s+", header=None, names=corfile_colnames())

    # Remove unlikely points
    data = data[(data["lat"] > 70) & (data["lat"] < 81) & (data["lon"] > 10) & (data["lon"] < 25)]

    data = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data["lon"], data["lat"], crs=4326))

    if data.shape[0] == 0:
        return data

    data.index = pd.to_datetime(data["date_str"] + "T" + data["time_str"])

    data = data.loc[~data.index.duplicated(keep="first")]

    return data


def save_corfile(filepath: Path, cor_data: gpd.GeoDataFrame):

    cor_data = cor_data[corfile_colnames()]

    cor_data.to_csv(filepath, sep="\t", header=False, index=False)

def find_other_corfiles(orig_corfile_path: Path, disallow_same_dir: bool = True, max_level: int = 2):
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


    trace_n_overlap = first["trace_n"].isin(second["trace_n"])
    if not np.any(trace_n_overlap):
        return None, None


    # joined = first.merge(second, on="trace_n")
    joined = first.merge(second, left_index=True, right_index=True)

    if (joined.shape[0] / first.shape[0]) < 0.3:
        return None, None

    # second_trace_n_overlap = second["trace_n"].isin(first["trace_n"])
    # first = first.loc[trace_n_overlap].sort_values("trace_n")
    # second = second.loc[second_trace_n_overlap].sort_values("trace_n")

    diffs = joined["lat_x"].values - joined["lat_y"].values
    lat_nmad = 1.4826 * np.nanmedian(np.abs((diffs - np.nanmedian(diffs)))) * 111132

    # if 0 < lat_nmad < 10:
    #     import matplotlib.pyplot as plt
    #     minval = joined[["alt_x", "alt_y"]].values.min()
    #     maxval = joined[["alt_x", "alt_y"]].values.max()
    #     plt.plot([minval, maxval], [minval, maxval])
    #     plt.scatter(joined["alt_x"], joined["alt_y"])
    #     plt.show()

    return lat_nmad, second.loc[joined.index]

    print(lat_nmad)
    

    return

    index_overlap = first.index.isin(second.index)

    if not np.any(index_overlap):
        return False

    first = first.loc[index_overlap]
    second = second.loc[first.index]


    print(first.iloc[:2])
    print(second.iloc[:2])

    lat_nmad = (first["alt"] - second["alt"]).abs().median()

    print(lat_nmad)

    

def replace_corfile(orig_corfile: Path) -> Path | None:
    corfile = read_corfile(orig_corfile)

    temp_dir = Path("temp_corfiles/")
    temp_fp = temp_dir / "corfile_0000.cor"

    if temp_fp.is_file():
        for i in range(10000):
            temp_fp = temp_dir / f"corfile_{str(i).zfill(4)}.cor" 
            if not temp_fp.is_file():
                break

    for other in find_other_corfiles(orig_corfile):

        # print(f"\t\tComparing {orig_corfile.name} with {other.name}")
        diff, better_cor = corfiles_compatible(corfile, read_corfile(other))

        if diff is None or better_cor is None:
            continue

        if diff < 0.01 or diff > 30:
            continue

        print(f"Replacing {orig_corfile.name} with {other.name}: {diff:.2f} m difference") 

        temp_fp.parent.mkdir(exist_ok=True)
        save_corfile(temp_fp, better_cor)
        return temp_fp

    


def main():
    # print(read_corfile("~/Downloads/DAT_0069_A1/2007/cor_files_precise-positions/22043_RC.COR"))
    # return
    orig_corfile = Path("/home/erik/Downloads/DAT_0069_A1/2008/Level0_COP_Malå_800MHz/2504-08-21/2504-08-21.cor")
    orig_corfile = Path("/home/erik/Downloads/DAT_0069_A1/2008/Level0_COP_Malå_800MHz/p111_b08_nw1_0205-08/p111_b08_nw1.cor")


    corfile_dir = Path("/home/erik/Downloads/DAT_0069_A1/2008/Level0_COP_Malå_800MHz")

    for orig_corfile in corfile_dir.rglob("*.*"):
        if orig_corfile.suffix.lower() != ".cor":
            continue
        replace_corfile(orig_corfile)


if __name__ == "__main__":
    main()
