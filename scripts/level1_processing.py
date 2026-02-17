from pathlib import Path
import shutil
from preprocess_mala import preprocess_mala

def copy_file(output_filepath: Path, input_filepath: Path):
    output_filepath.parent.mkdir(exist_ok=True, parents=True)
    if output_filepath.is_file():
        return
    
    print(f"Copying {input_filepath} to {output_filepath}")
    shutil.copy(input_filepath, output_filepath)

def create_renaming_plan():

    level0_dir = Path(r"C:\Users\satuki\OneDrive - Universitetet i Oslo\PFA_data_Svalbard")
    level1_dir = Path("processed/level1")#.absolute()

    renaming = {
        # AUSTFONNA 2025
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0002_B1": "austfonna-profile-2025-100MHz-mala-01",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0005_B1": "austfonna-profile-2025-100MHz-mala-02",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0007_B1": "austfonna-profile-2025-100MHz-mala-03",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0008_B1": "austfonna-profile-2025-100MHz-mala-04",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0009_B1": "austfonna-profile-2025-100MHz-mala-05",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0010_B1": "austfonna-profile-2025-100MHz-mala-06",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0011_B1": "austfonna-profile-2025-100MHz-mala-07",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0012_B1": "austfonna-profile-2025-100MHz-mala-08",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0013_B1": "austfonna-profile-2025-100MHz-mala-09",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0014_B1": "austfonna-profile-2025-100MHz-mala-10",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0015_B1": "austfonna-profile-2025-100MHz-mala-11",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0016_B1": "austfonna-profile-2025-100MHz-mala-12",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0017_B1": "austfonna-profile-2025-100MHz-mala-13",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0018_B1": "austfonna-profile-2025-100MHz-mala-14",
        r"Austfonna\2025\Level0_COP_Malå_100MHz\DAT_0019_B1": "austfonna-profile-2025-100MHz-mala-15",

        r"Austfonna\2025\Level0_COP_pulseEKKO_200MHz\grid_cmp1": "austfonna-profile-2025-200MHz-pulseekko-01",
        r"Austfonna\2025\Level0_COP_pulseEKKO_200MHz\grid_cmp2": "austfonna-profile-2025-200MHz-pulseekko-02",
        r"Austfonna\2025\Level0_COP_pulseEKKO_200MHz\grid_cmp3": "austfonna-profile-2025-200MHz-pulseekko-03",
        r"Austfonna\2025\Level0_COP_pulseEKKO_200MHz\line_through_all_cmps": "austfonna-profile-2025-200MHz-pulseekko-04",

        # AMUNDSENISEN 2025
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0118_A1": "amundsenisen-profile-2025-100MHz-mala-01",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0120_A1": "amundsenisen-profile-2025-100MHz-mala-02",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0135_A1": "amundsenisen-profile-2025-100MHz-mala-03", # short files: 128, 135, 137, 138, 140, 142
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0136_A1": "amundsenisen-profile-2025-100MHz-mala-04",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0137_A1": "amundsenisen-profile-2025-100MHz-mala-05",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0138_A1": "amundsenisen-profile-2025-100MHz-mala-06",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0139_A1": "amundsenisen-profile-2025-100MHz-mala-07",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0140_A1": "amundsenisen-profile-2025-100MHz-mala-08",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0142_A1": "amundsenisen-profile-2025-100MHz-mala-09",

        r"Amundsenisen\2025\Level0_COP_pulseEKKO_200MHz\line1": "amundsenisen-profile-2025-200MHz-pulseekko-01",
        r"Amundsenisen\2025\Level0_COP_pulseEKKO_200MHz\line4": "amundsenisen-profile-2025-200MHz-pulseekko-02",
        r"Amundsenisen\2025\Level0_COP_pulseEKKO_200MHz\line5": "amundsenisen-profile-2025-200MHz-pulseekko-03",


        # AMUNDSENISEN 2006
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\AMU1": "amundsenisen-profile-2006-200MHz-mala-01",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\AMU2": "amundsenisen-profile-2006-200MHz-mala-02",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\AMU3": "amundsenisen-profile-2006-200MHz-mala-03",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\AMU4": "amundsenisen-profile-2006-200MHz-mala-04",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu8": "amundsenisen-profile-2006-200MHz-mala-05",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu9": "amundsenisen-profile-2006-200MHz-mala-06",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu11": "amundsenisen-profile-2006-200MHz-mala-07",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu12": "amundsenisen-profile-2006-200MHz-mala-08",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu13": "amundsenisen-profile-2006-200MHz-mala-09",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu14": "amundsenisen-profile-2006-200MHz-mala-10",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu15": "amundsenisen-profile-2006-200MHz-mala-11",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu16": "amundsenisen-profile-2006-200MHz-mala-12",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu19": "amundsenisen-profile-2006-200MHz-mala-13",
        r"Amundsenisen\2006\Level0_COP_Malå_200MHz\amu20": "amundsenisen-profile-2006-200MHz-mala-14",


    }

    for orig_dir, radar_id in renaming.items():
        filepaths = list((level0_dir / orig_dir).iterdir())
        if len(filepaths) == 0:
            raise ValueError(f"Directory {orig_dir} is empty")
        
        renamed_files = {}
        for filepath in filepaths:
            new_filename = radar_id + filepath.suffix
            new_filepath = level1_dir / radar_id.split("-")[0] / radar_id / new_filename

            if "mala" in radar_id and filepath.suffix not in [".cor", ".rad", ".rd3"]:
                continue
            if "pulseekko" in radar_id and filepath.suffix not in [".hd", ".gp2", ".dt1"]:
                continue
            
            renamed_files[new_filepath.suffix] = (filepath, new_filepath)

        if "mala" in radar_id:
            better_gps_track = None
            if "austfonna-profile-2025-100MHz-mala" in radar_id:
                better_gps_track = level0_dir / r"Austfonna\2025\Level0_COP_Malå_100MHz\kinematic2025_ppp_1s_radar.zip"
            preprocess_mala(
                output_rad_filepath=renamed_files[".rad"][1],
                input_rad_filepath=renamed_files[".rad"][0],
                input_cor_filepath=renamed_files[".cor"][0],
                input_rd3_filepath=renamed_files[".rd3"][0],
                better_gps_path=better_gps_track,
            )
        else:
            for (filepath, new_filepath) in renamed_files.values():
                copy_file(output_filepath=new_filepath, input_filepath=filepath)


                


if __name__ == "__main__":
    create_renaming_plan()

