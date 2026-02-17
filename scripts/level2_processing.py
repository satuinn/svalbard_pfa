import subprocess
from pathlib import Path
import numpy as np

RSGPR_PATH = "rsgpr"

def locate_rsgpr():
    """Try to locate an installation of rsgpr"""
    global RSGPR_PATH
    import socket

    if socket.gethostname() == "erik-ryzen":
        new_path = Path("~/Projects/UiO/rsgpr/target/release/rsgpr").expanduser()
        if not new_path.is_file():
            return
        RSGPR_PATH = new_path


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
    cmds = (
        [
            RSGPR_PATH,
            "-v",
            f"{medium_velocity}",
            "--steps",
            ",".join(steps),
            "--filepath",
            str(input_filepath),
            "--output",
            str(output_filepath),
        ]
        + ((["--dem", str(dem_path)]) if dem_path is not None else [])
    )

    result = subprocess.run(
        cmds,
        capture_output=True,
    )
    if result.returncode != 0:
        raise ValueError(f"rsgpr failed: {result.stderr}")

    log_filepath = Path(output_filepath).with_suffix(".log")
    log_filepath.write_text(f"stdout:\n{result.stdout.decode()}\n\n\nstderr:\n{result.stderr.decode()}")


def normalize(data: np.ndarray, contrast: float = 0.9):
    """Normalize the data and convert to an unsigned 8 bit integer array."""
    data = np.abs(data)
    minval_abs, maxval_abs = np.percentile(np.abs(data[50:]), [1, 99])
    data = np.clip(contrast * (data - minval_abs) / (maxval_abs - minval_abs), 0, 1)

    return (data * 255).astype("uint8")

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

        PIL.Image.fromarray(arr).save(jpg_path)


def process_data(redo: bool = False):
    """Process (level2) GPR data using rsgpr.

    Parameters
    ----------
    redo
        Reprocess data despite already existing.
    """
    locate_rsgpr()
    level1_dir = Path("processing/level1")
    level2_dir = Path("processing/level2")

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

        # Vary the siglog strength because overall signal strengths vary depending on
        # GPR brand, time and frequency.
        siglog_level = 3
        if header_filepath.suffix == ".hd":
            siglog_level = 0
        elif "amundsenisen-profile-2006" in header_filepath.stem:
            siglog_level = 2

        steps = [
            "zero_corr",
            "gain(0.08)",
            "bandpass(0.1 0.9)",
            f"siglog({siglog_level})",
        ]

        output_filepath.parent.mkdir(exist_ok=True, parents=True)

        print(output_filepath.name)
        if not output_filepath.is_file() and not redo:
            run_rsgpr(input_filepath=header_filepath, output_filepath=output_filepath, steps=steps)

        generate_jpgs(output_filepath)


if __name__ == "__main__":
    process_data()
