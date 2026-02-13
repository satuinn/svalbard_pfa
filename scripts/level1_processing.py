from pathlib import Path

def create_renaming_plan():

    level0_dir = Path(r"C:\Users\satuki\OneDrive - Universitetet i Oslo\PFA_data_Svalbard")
    level1_dir = Path("processed/level1")#.absolute()

    renaming = {
        "Austfonna/2025/Level0_COP_Malå_100MHz/DAT_0002_B1": "austfonna-profile-2025-100MHz-mala-01",
        "Austfonna/2025/Level0_COP_Malå_100MHz/DAT_0005_B1": "austfonna-profile-2025-100MHz-mala-02",
        r"Amundsenisen\2025\Level0_COP_Malå_100MHz\DAT_0118_A1": "amundsenisen-profile-2025-100MHz-mala-01",
    }

    renamed_files = {}
    for orig_dir, radar_id in renaming.items():
        if "mala" in radar_id:
            for filepath in (level0_dir / orig_dir).iterdir():
                if filepath.suffix not in [".cor", ".rad", ".rd3"]:
                    continue
                new_filename = radar_id + filepath.suffix
                new_filepath = level1_dir / radar_id.split("-")[0] / radar_id / new_filename
                print(filepath, new_filepath)


if __name__ == "__main__":
    create_renaming_plan()

