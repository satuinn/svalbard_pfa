import geopandas as gpd
import pandas as pd
import scipy.interpolate
import numpy as np

from pathlib import Path
import itertools


def twt_to_depth(twt: np.ndarray, antenna_separation: float, velocity: float = 0.19):
    return np.sqrt(
        (velocity ** 2 * twt ** 2 / 4) - (antenna_separation ** 2 / 4) 
    )


def combine_cor_and_pick(corfile: Path, pick_file: Path, out_path: Path, step_size_m: float = 1.):

    if corfile.suffix == ".cor":
        cor_data = pd.read_csv(corfile, sep="\t", header=None, names=["trace_n", "date", "time", "latitude", "N", "longitude", "E", "altitude", "M", "1"])
        antenna_separation = 2
        # See the gp2 (pulseEKKO) part for why this below exists
        trace_n_multiplier = 1
    elif corfile.suffix == ".gp2":
        cor_data = read_gp2(corfile)
        antenna_separation = 1

        # The GPRPy x coordinate is in "distance", which is incorrectly calculated from the pulseEKKO header
        # It's multiplying the trace number with the "STEP SIZE USED" field in the header
        # This part undoes that conversion, through calculating a "trace_n_multiplier" which all picked trace x coords are multiplied by 
        header = {}
        for line in corfile.with_suffix(".hd").read_text().splitlines():
            if "=" not in line:
                continue
            key, value = line.split("=", maxsplit=1)

            # Try to convert all values to floats. No worries if it doesn't work
            try:
                value = float(value.strip())
            except ValueError:
                value = value.strip()

            header[key.strip()] = value

        trace_n_multiplier = 1 / header["STEP SIZE USED"]
    else:
        raise ValueError(f"Unrecognized filetype: {corfile}")

    cor_data = gpd.GeoDataFrame(cor_data, geometry=gpd.points_from_xy(cor_data["longitude"], cor_data["latitude"], crs=4326)).to_crs(32633)
    cor_data["easting"] = cor_data.geometry.x
    cor_data["northing"] = cor_data.geometry.y

    cor_data["distance"] = ((cor_data[["easting", "northing"]].diff(axis="rows").fillna(0) ** 2).sum(axis="columns") ** 0.5).cumsum()
    
    sample_distances = np.arange(0, cor_data["distance"].max(), step=step_size_m)
    sample_trace_n = scipy.interpolate.interp1d(cor_data["distance"], cor_data["trace_n"])(sample_distances)

    pick_data = pd.read_csv(pick_file, sep="\t", header=None, names=["trace_n", "pfa_twt"])
    pick_data["trace_n"] *= trace_n_multiplier
    pick_data = pick_data.groupby("trace_n").mean()

    pick_data_interp = scipy.interpolate.interp1d(pick_data.index, pick_data["pfa_twt"], bounds_error=False)(sample_trace_n)
    pick_data = pd.DataFrame({"trace_n": sample_trace_n, "pfa_twt": pick_data_interp}).dropna().set_index("trace_n", drop=True)

    for col in ["easting", "northing", "altitude"]:
        model = scipy.interpolate.interp1d(cor_data["trace_n"], cor_data[col], fill_value="extrapolate")

        pick_data[col] = model(pick_data.index)

    pick_data = gpd.GeoDataFrame(pick_data, geometry=gpd.points_from_xy(pick_data["easting"], pick_data["northing"], crs=cor_data.crs))

    pick_data["layer"] = pick_file.stem

    pick_data["pfa_depth"] = twt_to_depth(pick_data["pfa_twt"], antenna_separation=antenna_separation)

    pick_data.to_file(out_path)
    return pick_data

def locate_all_cor_and_pick(base_dirs: list[Path], out_dir: Path = Path("picks/auf2025")):

    all_data = []
    for base_dir in base_dirs:
        for cor_path in itertools.chain(base_dir.rglob("*.cor"), base_dir.rglob("*.gp2")):
            base_name = cor_path.stem.replace("_A1", "")
            print(f"Looking for {base_name} picks")

            for pick_fp in cor_path.parent.glob(f"picks_{base_name}*.txt"):
                if "crevasse" in pick_fp.name:
                    continue
                print(f"\tFound {pick_fp.name}")

                out_path = out_dir / f"{pick_fp.stem}.geojson"

                out_path.parent.mkdir(exist_ok=True, parents=True)
                new_data = combine_cor_and_pick(corfile=cor_path, pick_file=pick_fp, out_path=out_path)

                all_data.append(new_data)

    pd.concat(all_data).to_file(out_dir / f"all_picks_{out_dir.stem}.geojson")



def read_gp2(filepath: Path):
    data = pd.read_csv(filepath, skiprows=5).rename(columns={"traces": "trace_n"})

    gpgga = data["GPS"].str.split(",", expand=True)

    data["latitude"] = gpgga[2].str.slice(0, 2).astype(float) + gpgga[2].str.slice(2, None).astype(float) / 60
    data["longitude"] = gpgga[4].str.slice(0, 3).astype(float) + gpgga[4].str.slice(3, None).astype(float) / 60
    data["altitude"] = gpgga[9].astype(float)
    data = data.groupby("trace_n", as_index=False).first()
    return data[["trace_n", "longitude", "latitude", "altitude"]]


if __name__ == "__main__":
    locate_all_cor_and_pick(
        [
            #Path(r"C:\Users\satuki\svalbard_pfa\MALÅ 100 MHz Amundsenisen 2025"),
            #Path(r"C:\Users\satuki\svalbard_pfa\Line Data PulseEkko AMU 2025\Lineset")
            Path(r"C:\Users\satuki\svalbard_pfa\Line Data PulseEkko AUS 2025")
        ]
    )
    #d = read_gp2(Path(r"C:\Users\satuki\svalbard_pfa\Line Data PulseEkko AMU 2025\Lineset\line1.gp2"))
    #print(d)

