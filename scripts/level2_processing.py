from pathlib import Path
import numpy as np
import shutil

REQUIRED_RSGPR_VERSION = "0.4.1"

def lowfreq_corr(x: np.ndarray, fs: float, fmin: float = 0.003, fmax: float = 0.3, alpha: float = 1500., sigma: float = 0.02, min_att: float = 1e-3):
    """Get a correction factor for low-frequency undulations in a signal.

    Parameters
    ----------
    x
        The signal to extract a correction factor from
    fs
        The sampling frequency in [s-1]
    fmin/fmax
        The minimum/maximum bound for frequency correction
    alpha
        A smoothing factor in [s] for the tracked frequency
    sigma
        The level of sudden frequency jump that is allowed
    min_att
        Minimum frequency jump size in the same unit as x

    Returns
    -------
    The estimated correction to subtract to the original signal.
    """
    import scipy.signal
    x = 1 - (x / x.mean())
    N = x.size
    x0 = x - np.median(x)  # robust DC removal

    # --- STFT settings ---
    nperseg = 2048 if N >= 2048 else max(256, (N//2)*2)
    noverlap = int(0.75 * nperseg)

    f, _, Z = scipy.signal.stft(
        x0, fs=fs, window="hann",
        nperseg=nperseg, noverlap=noverlap,
        detrend=False, return_onesided=True,
        boundary="zeros", padded=True
    )
    S = np.abs(Z)

    # --- target band where the artifact lives ---
    band = (f >= fmin) & (f <= fmax)
    fi = np.where(band)[0]
    fb = f[fi]
    Sb = S[fi, :]

    # --- ridge tracking via dynamic programming (Viterbi) ---
    logSb = np.log(Sb + 1e-12)
    Df2 = (fb[:, None] - fb[None, :])**2  # Hz^2 pairwise distances

    dp = np.empty(logSb.shape)
    ptr = np.empty(logSb.shape, dtype=np.int32)

    dp[:, 0] = logSb[:, 0]
    ptr[:, 0] = -1

    for k in range(1, Sb.shape[1]):
        prev = dp[:, k-1]
        scores = prev[None, :] - alpha * Df2
        best_j = np.argmax(scores, axis=1)
        dp[:, k] = logSb[:, k] + scores[np.arange(Sb.shape[0]), best_j]
        ptr[:, k] = best_j

    # backtrack best path
    ridge_rel = np.empty(Sb.shape[1], dtype=np.int32)
    ridge_rel[-1] = int(np.argmax(dp[:, -1]))
    for k in range(logSb.shape[1]-2, -1, -1):
        ridge_rel[k] = ptr[ridge_rel[k+1], k+1]

    ridge_idx = fi[ridge_rel]
    ridge_f = f[ridge_idx]

    # --- soft notch mask around ridge (Gaussian in frequency) ---
    mask = np.ones_like(Z, dtype=float)
    for k in range(Sb.shape[1]):
        f0 = ridge_f[k]
        g = np.exp(-0.5 * ((f - f0) / sigma)**2)
        att = 1 - (1 - min_att) * g
        mask[:, k] *= att

    # --- inverse STFT back to time domain ---
    _, x_clean = scipy.signal.istft(
        Z * mask, fs=fs, window="hann",
        nperseg=nperseg, noverlap=noverlap,
        input_onesided=True, boundary=True
    )

    return x - x_clean[:N]


def run_rsgpr(
    input_filepath: Path | str,
    output_filepath: Path | str,
    steps: list[str],
    dem_path: Path | None = None,
    medium_velocity: float = 0.2,
):
    """Run rsgpr with the given steps.

    Parameters
    ----------
    input_filepath
        The input .rad/.hd filepath for the data to process.
    output_filepath
        The output .nc filepath to save the data in.
    steps
        Which steps to apply on the data.
    dem_path
        Optional. Which DEM to correct elevations with
    medium_velocity
        The assumed velocity of the subsurface in m/ns
    """
    import rsgpr

    required_ver = "0.4.1"
    assert rsgpr.version >= required_ver, f"Incompatible rsgpr version found: {version}. Needs >= {required_ver}"

    if not Path(input_filepath).is_file():
        raise ValueError(f"Cannot find {input_filepath}")
        
    output_filepath = Path(output_filepath)
    tmp_path = output_filepath.with_name(output_filepath.name + ".tmp")

    rsgpr.run_cli(
        filepath=str(input_filepath),
        velocity=medium_velocity,
        steps=steps,
        output=str(tmp_path),
        quiet=True,
        dem=str(dem_path) if dem_path is not None else None,
    )

    shutil.move(tmp_path, output_filepath)


def normalize(data: np.ndarray, contrast: float = 0.9):
    """Normalize the data and convert to an unsigned 8 bit integer array."""
    data_abs = np.abs(data)
    minval_abs, maxval_abs = np.percentile(np.abs(data_abs[50:]), [1, 99])
    data_abs = np.clip(contrast * (data - minval_abs) / (maxval_abs - minval_abs + 1e-12), 0, 1)

    return (data_abs * 255).astype("uint8")


def fix_power_variation(filepath: Path):
    """Correct for horizontal variations in power in a dataset.
    This will overwrite the original data."""
    import xarray as xr
    xr.set_options(display_style='text')
    new_filepath = filepath.with_name(filepath.name + ".tmp")
    with xr.open_dataset(filepath) as data:
        if data.x.shape[0] <= 256:
            print(f"Skipping power correction on {filepath}: too short file")

        if data.attrs.get("power_fixed", 0) == 1:
            print(f"Skipping power correction on {filepath}: it has already been done")
            return

        print(f"Estimating and applying power variation correction.")
        line = np.abs(data.data.isel(y=slice(data.y.shape[0] - 10, None))).mean("y").values
        corr = lowfreq_corr(line, 1 / data.attrs["time-interval"])

        # line = np.abs(data.data.isel(y=slice(data.y.shape[0] - 10))).mean("y").rolling(x=50, min_periods=1, center=True).mean().values
        # corr = (1 - (line / line.mean()))

        data["data"] *= 1 + corr[None, :] * (data["depth"] / data["depth"].max()).values[:, None]

        data.attrs["power_fixed"] = 1

        # Force every attribute to be ASCII characters only. This stopped files from being saved on some computers
        for key, value in data.attrs.items():
            if isinstance(value, str):
                data.attrs[key] = value.encode("ascii", errors="ignore").decode()
        
        data.to_netcdf(new_filepath, encoding={v: {"complevel": 9, "zlib": True} for v in data.data_vars})

    shutil.move(new_filepath, filepath)


def generate_jpgs(processed_filepath: Path, redo: bool = False):
    """Generate JPG versions of a processed radargram.

    Parameters
    ----------
    processed_filepath
        The filepath to the processed (.nc) data.
    redo
        Reprocess data despite already existing.
    """
    jpg_path = processed_filepath.with_name(processed_filepath.stem + ".jpg")
    if jpg_path.is_file() and not redo:
        return

    import xarray as xr
    import PIL.Image

    with xr.open_dataset(processed_filepath) as data:
        arr = normalize(data.data.values)

    maxwidth = 60000
    if arr.shape[1] > maxwidth:
        for i, start in enumerate(range(0, arr.shape[1], maxwidth)):
            end = min(start + maxwidth, arr.shape[1])
            PIL.Image.fromarray(arr[:, start:end]).save(jpg_path.with_stem(jpg_path.stem + f"_{i}"))
    else:
        PIL.Image.fromarray(arr).save(jpg_path)

            

def subsetting(radar_key: str) -> tuple[int, int] | None:
    """Get the predetermined trace subsetting information for a given radar_key,
     or None if no subsetting should be done."""
    subsets = {
        # 2007
        "austfonna-profile-2007-800MHz-mala-01": (0, 5345),
        "austfonna-profile-2007-800MHz-mala-02": (15890, -1),
        "austfonna-profile-2007-800MHz-mala-05": (13421, -1),
        # 2008
        "austfonna-profile-2008-800MHz-mala-07": (0, 11278),
        "austfonna-profile-2008-800MHz-mala-05": (0, 5798),
        "austfonna-profile-2008-800MHz-mala-04": (0, 12834),
        "austfonna-profile-2008-800MHz-mala-03": (0, 4151),
        # 2009
        "austfonna-profile-2009-800MHz-mala-01": (13819, -1),
        "austfonna-profile-2009-800MHz-mala-04": (0, 4440),
        # 2010
        "austfonna-profile-2010-800MHz-mala-02": (15547, -1),
        # 2011
        "austfonna-profile-2011-800MHz-mala-01": (16114, -1),
        "austfonna-profile-2011-800MHz-mala-02": (0, 5647),
        "austfonna-profile-2011-800MHz-mala-03": (0, 4018),
        "austfonna-profile-2011-800MHz-mala-04": (8527, 18126),
        "austfonna-profile-2011-800MHz-mala-05": (32711, -1),
        # 2012
        "austfonna-profile-2012-800MHz-mala-02": (0, 5937),
        "austfonna-profile-2012-800MHz-mala-06": (0, 11755),
        "austfonna-profile-2012-800MHz-mala-07": (8033, -1),
        # 2013
        "austfonna-profile-2013-800MHz-mala-01": (3258, -1),
        "austfonna-profile-2013-800MHz-mala-02": (0, 15943),
        "austfonna-profile-2013-800MHz-mala-03": (8151, -1),
        "austfonna-profile-2013-800MHz-mala-05": (0, 4110),
        "austfonna-profile-2013-800MHz-mala-06": (0, 1983),
        # 2014
        "austfonna-profile-2014-800MHz-mala-03": (7903, -1),
        # 2015
        "austfonna-profile-2015-800MHz-mala-01": (9929, -1),
        "austfonna-profile-2015-800MHz-mala-03": (0, 13153),
        "austfonna-profile-2015-800MHz-mala-04": (22242, -1),

        #2016:
        "austfonna-profile-2016-800MHz-mala-01": (15773, -1),
        "austfonna-profile-2016-800MHz-mala-03": (8720, -1),
        
        #2017:
        "austfonna-profile-2017-800MHz-mala-02": (0, 1304),
        "austfonna-profile-2017-800MHz-mala-03": (9181, -1),
        "austfonna-profile-2017-800MHz-mala-06": (0, 3968),
        
        #2018:
        "austfonna-profile-2018-800MHz-mala-02": (0, 1364),
        
        #2019:
        "austfonna-profile-2019-800MHz-mala-01": (7196, -1),
        "austfonna-profile-2019-800MHz-mala-03": (0, 955),
        "austfonna-profile-2019-800MHz-mala-04": (6332, -1),
        
        
        #2023:
        "austfonna-profile-2023-800MHz-mala-01": (30668, 71580),
        "austfonna-profile-2023-800MHz-mala-03": (0, 26391),

    }

    if radar_key not in subsets:
        return None

    subset = subsets[radar_key]
    if isinstance(subset, int):
        return (subset, -1)
    else:
        return subset
        

def process_radargram(output_filepath: Path, input_header_filepath: Path, radar_key: str | None = None):
    """Process one radargram, with steps defined from its filename/radar_key.

    A JPG will be rendered beside the output_filepath.
    If the data are longer than 60000 traces, the JPG will be split in parts.

    Parameters
    ----------
    output_filepath
        The output .nc filepath to save the data in.
    input_header_filepath
        The input .rad/.hd header filepath for the data to process.
    radar_key
        Optional. The radar_key to use for processing step determination.
        If not provided, it will be determined from the filepath.
    """
    if radar_key is None:
        radar_key = input_header_filepath.stem

    # The power variation fix should most often not be run
    run_fix_power_variation = False

    # Steps for 800MHz
    if "-800MHz-" in radar_key:
        steps = [
            "average_traces(2)",
            "zero_corr",
            "bandpass(0.2 0.5)",
            "gain(0.11)",
            "siglog(2)"
        ]

        if "austfonna-profile-2023" in radar_key or "austfonna-profile-2024" in radar_key:
            run_fix_power_variation = True
        
    # Steps if it's anything else than 800MHz
    else:
        # Vary the siglog strength because overall signal strengths vary depending on
        # GPR brand, time and frequency.
        siglog_level = 3
        if input_header_filepath.suffix == ".hd":
            siglog_level = 0
        elif "amundsenisen-profile-2006" in radar_key:
            siglog_level = 2
        elif "-25MHz-" in radar_key:
            siglog_level = 0

        gain_level = 0.08
        if "-25MHz-" in radar_key:
            gain_level = 0.008

        steps = [
            "zero_corr",
            f"gain({gain_level})",
            "bandpass(0.1 0.9)",
            f"siglog({siglog_level})",
        ]

    # If a subsetting operation has been defined for the key, apply it first.
    if (subset := subsetting(radar_key)) is not None:
        steps.insert(0, f"subset({subset[0]} {subset[1]})")

    output_filepath.parent.mkdir(exist_ok=True, parents=True)

    print(f"Processing {input_header_filepath.name}")
    run_rsgpr(input_filepath=input_header_filepath, output_filepath=output_filepath, steps=steps)

    if run_fix_power_variation:
        fix_power_variation(output_filepath)

    generate_jpgs(output_filepath, redo=True)
    

def process_all_data(redo: bool = False):
    """Process (level2) GPR data using rsgpr.

    Parameters
    ----------
    redo
        Reprocess data despite already existing.
    """
    level1_dir = Path("processed/level1")
    level2_dir = Path("processed/level2")

    for header_filepath in level1_dir.rglob("*.*"):

        if header_filepath.suffix not in [".hd", ".rad"]:
            continue
        # Skip any filepath that doesn't conform to the naming convention
        if not len(header_filepath.stem.split("-")) == 6:
            print(f"Found {header_filepath} but its name was unexpected")
            continue

        # Complicated way to retain the file structure but now in level2
        # E.g. some_dir/level1/subdir/file.rad -> new_dir/level2/subdir/file.rad
        output_filepath = (level2_dir / "/".join(header_filepath.parts[slice(header_filepath.parts.index("level1") + 1, None)])).with_suffix(".nc")

        if "austfonna-profile-2024-25MHz" in output_filepath.stem:
            redo = True
        else:
            continue

        try:
            if not output_filepath.is_file() or redo:
                process_radargram(output_filepath=output_filepath, input_header_filepath=header_filepath)
        except RuntimeError as exception:
            print(f"Failed with error: {exception}")


if __name__ == "__main__":
    process_all_data()
