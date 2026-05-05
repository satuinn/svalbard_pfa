from pathlib import Path
import shutil
from preprocess_mala import preprocess_mala
from locate_better_mala_corfiles import replace_corfile 

def copy_file(output_filepath: Path, input_filepath: Path):
    output_filepath.parent.mkdir(exist_ok=True, parents=True)
    #if output_filepath.is_file():
    #    return
    
    print(f"Copying {input_filepath} to {output_filepath}")
    shutil.copy(input_filepath, output_filepath)

def create_renaming_plan():

    level0_dir = Path(r"C:\Users\satuki\OneDrive - Universitetet i Oslo\PFA_data_Svalbard")
    level1_dir = Path("processed/level1")#.absolute()

    renaming = {


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


        # AUSTFONNA 2026
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0007_A1": "austfonna-profile-2026-800MHz-mala-01",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0006_A1_27042026": "austfonna-profile-2026-800MHz-mala-02",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0007_A1_27042026": "austfonna-profile-2026-800MHz-mala-03",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0008_A1_27042026": "austfonna-profile-2026-800MHz-mala-04",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0009_A1_27042026": "austfonna-profile-2026-800MHz-mala-05",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0010_A1_27042026": "austfonna-profile-2026-800MHz-mala-06",

        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0011_A1_02042026_uio_monitor": "austfonna-profile-2026-800MHz-mala-07",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0012_A1_02042026_uio_monitor": "austfonna-profile-2026-800MHz-mala-08",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0013_A1_02042026_uio_monitor": "austfonna-profile-2026-800MHz-mala-09",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0014_A1_02042026_uio_monitor": "austfonna-profile-2026-800MHz-mala-10",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0016_A1_02042026_uio_monitor": "austfonna-profile-2026-800MHz-mala-11",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0016_A1_02042026_unis_monitor": "austfonna-profile-2026-800MHz-mala-12",

        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0023_A1_03052026_unis_monitor": "austfonna-profile-2026-800MHz-mala-13",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0024_A1_03052026_unis_monitor": "austfonna-profile-2026-800MHz-mala-14",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0025_A1_03052026_unis_monitor": "austfonna-profile-2026-800MHz-mala-15",
        r"Austfonna\2026\Level0_COP_Malå_800MHz\DAT_0026_A1_03052026_unis_monitor": "austfonna-profile-2026-800MHz-mala-16",

        r"Austfonna\2026\Level0_COP_Malå_100MHz\DAT_0017_A1_03052026_unis_monitor": "austfonna-profile-2026-100MHz-mala-01",
        r"Austfonna\2026\Level0_COP_Malå_100MHz\DAT_0019_A1_03052026_unis_monitor": "austfonna-profile-2026-100MHz-mala-02",
        r"Austfonna\2026\Level0_COP_Malå_100MHz\DAT_0020_A1_03052026_unis_monitor": "austfonna-profile-2026-100MHz-mala-03",
        r"Austfonna\2026\Level0_COP_Malå_100MHz\DAT_0021_A1_03052026_unis_monitor": "austfonna-profile-2026-100MHz-mala-04",
        r"Austfonna\2026\Level0_COP_Malå_100MHz\DAT_0022_A1_03052026_unis_monitor": "austfonna-profile-2026-100MHz-mala-05",

        # pulseEKKO
        r"Austfonna\2026\Level0_COP_pulseEKKO_200MHz\grid_cmp1": "austfonna-profile-2026-200MHz-pulseekko-01",
        r"Austfonna\2026\Level0_COP_pulseEKKO_200MHz\line2_around_camp": "austfonna-profile-2026-200MHz-pulseekko-02",
        r"Austfonna\2026\Level0_COP_pulseEKKO_200MHz\line3_around_camp": "austfonna-profile-2026-200MHz-pulseekko-03",
        r"Austfonna\2026\Level0_COP_pulseEKKO_200MHz\line4_around_camp": "austfonna-profile-2026-200MHz-pulseekko-04",



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

        # AUSTFONNA 2024
        r"Austfonna\2024\Level0_COP_Malå_25MHz\DAT_0024_A1": "austfonna-profile-2024-25MHz-mala-01",
        r"Austfonna\2024\Level0_COP_Malå_25MHz\DAT_0025_A1": "austfonna-profile-2024-25MHz-mala-02",

        r"Austfonna\2024\Level0_COP_Malå_800MHz\DAT_0004_A1": "austfonna-profile-2024-800MHz-mala-01",
        r"Austfonna\2024\Level0_COP_Malå_800MHz\DAT_0015_A1": "austfonna-profile-2024-800MHz-mala-02",
        r"Austfonna\2024\Level0_COP_Malå_800MHz\DAT_0016_A1": "austfonna-profile-2024-800MHz-mala-03",
        r"Austfonna\2024\Level0_COP_Malå_800MHz\DAT_0017_A1": "austfonna-profile-2024-800MHz-mala-04",
        r"Austfonna\2024\Level0_COP_Malå_800MHz\DAT_0018_A1": "austfonna-profile-2024-800MHz-mala-05",
        r"Austfonna\2024\Level0_COP_Malå_800MHz\DAT_0019_A1": "austfonna-profile-2024-800MHz-mala-06",
        r"Austfonna\2024\Level0_COP_Malå_800MHz\DAT_0020_A1": "austfonna-profile-2024-800MHz-mala-07",

        # AUSTFONNA 2023 
        r"Austfonna\2023\Level0_COP_Malå_800MHz\DAT_0131_A1_2023-05-05": "austfonna-profile-2023-800MHz-mala-01",
        r"Austfonna\2023\Level0_COP_Malå_800MHz\DAT_0133_A1_2023-05-05": "austfonna-profile-2023-800MHz-mala-02",
        r"Austfonna\2023\Level0_COP_Malå_800MHz\DAT_0137_A1_2023-05-09": "austfonna-profile-2023-800MHz-mala-03",


        # AUSTFONNA 2004
        # main
        r"Austfonna\2004\Level0_COP_Malå_800MHz\120-13": "austfonna-profile-2004-800MHz-mala-01",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\120-131": "austfonna-profile-2004-800MHz-mala-02",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\vest4": "austfonna-profile-2004-800MHz-mala-03",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\vest9": "austfonna-profile-2004-800MHz-mala-04",

        # the rest
        r"Austfonna\2004\Level0_COP_Malå_800MHz\120-11": "austfonna-profile-2004-800MHz-mala-05",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\120-12": "austfonna-profile-2004-800MHz-mala-06",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\120-1311": "austfonna-profile-2004-800MHz-mala-07",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\120-13111": "austfonna-profile-2004-800MHz-mala-08",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\vest3": "austfonna-profile-2004-800MHz-mala-09",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\vest5": "austfonna-profile-2004-800MHz-mala-10",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\vest8": "austfonna-profile-2004-800MHz-mala-11",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry1": "austfonna-profile-2004-800MHz-mala-12",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry2": "austfonna-profile-2004-800MHz-mala-13",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry3": "austfonna-profile-2004-800MHz-mala-14",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry4": "austfonna-profile-2004-800MHz-mala-15",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry5": "austfonna-profile-2004-800MHz-mala-16",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry6": "austfonna-profile-2004-800MHz-mala-17",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry7": "austfonna-profile-2004-800MHz-mala-18",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry8": "austfonna-profile-2004-800MHz-mala-19",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry9": "austfonna-profile-2004-800MHz-mala-20",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry10": "austfonna-profile-2004-800MHz-mala-21",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry11": "austfonna-profile-2004-800MHz-mala-22",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry12": "austfonna-profile-2004-800MHz-mala-23",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry13": "austfonna-profile-2004-800MHz-mala-24",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry14": "austfonna-profile-2004-800MHz-mala-25",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\472cry1_2304-04": "austfonna-profile-2004-800MHz-mala-26",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au1": "austfonna-profile-2004-800MHz-mala-27",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au2": "austfonna-profile-2004-800MHz-mala-28",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au3": "austfonna-profile-2004-800MHz-mala-29",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au6": "austfonna-profile-2004-800MHz-mala-30",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au7": "austfonna-profile-2004-800MHz-mala-31",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au8": "austfonna-profile-2004-800MHz-mala-32",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au9": "austfonna-profile-2004-800MHz-mala-33",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\121au10": "austfonna-profile-2004-800MHz-mala-34",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\797cry1": "austfonna-profile-2004-800MHz-mala-35",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\797cry2": "austfonna-profile-2004-800MHz-mala-36",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\797cry3": "austfonna-profile-2004-800MHz-mala-37",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\797cry4": "austfonna-profile-2004-800MHz-mala-38",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\au-met1": "austfonna-profile-2004-800MHz-mala-39",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\au-met2": "austfonna-profile-2004-800MHz-mala-40",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\au-met3": "austfonna-profile-2004-800MHz-mala-41",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\au-met4": "austfonna-profile-2004-800MHz-mala-42",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122rep1": "austfonna-profile-2004-800MHz-mala-43",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\cry797s1": "austfonna-profile-2004-800MHz-mala-44",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\cry797s2": "austfonna-profile-2004-800MHz-mala-45",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\cry797s3": "austfonna-profile-2004-800MHz-mala-46",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\cry797s4": "austfonna-profile-2004-800MHz-mala-47",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\cry797s5": "austfonna-profile-2004-800MHz-mala-48",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\cry797s6": "austfonna-profile-2004-800MHz-mala-49",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\cry797s7": "austfonna-profile-2004-800MHz-mala-50",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122au1": "austfonna-profile-2004-800MHz-mala-51",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122au2": "austfonna-profile-2004-800MHz-mala-52",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122au3": "austfonna-profile-2004-800MHz-mala-53",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122au4": "austfonna-profile-2004-800MHz-mala-54",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122au5": "austfonna-profile-2004-800MHz-mala-55",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122au6": "austfonna-profile-2004-800MHz-mala-56",
        r"Austfonna\2004\Level0_COP_Malå_800MHz\d122au7": "austfonna-profile-2004-800MHz-mala-57",


        # AUSTFONNA 2005
        # main
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2304-2": "austfonna-profile-2005-800MHz-mala-01",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2404-2": "austfonna-profile-2005-800MHz-mala-02",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf23041": "austfonna-profile-2005-800MHz-mala-03",

        # the rest
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2304-1": "austfonna-profile-2005-800MHz-mala-04",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2304-3": "austfonna-profile-2005-800MHz-mala-05",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2304-4": "austfonna-profile-2005-800MHz-mala-06",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2304-5": "austfonna-profile-2005-800MHz-mala-07",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2404-3": "austfonna-profile-2005-800MHz-mala-08",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf1": "austfonna-profile-2005-800MHz-mala-09",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf2": "austfonna-profile-2005-800MHz-mala-10",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf3": "austfonna-profile-2005-800MHz-mala-11",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf4": "austfonna-profile-2005-800MHz-mala-12",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf5": "austfonna-profile-2005-800MHz-mala-13",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf6": "austfonna-profile-2005-800MHz-mala-14",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\asf7": "austfonna-profile-2005-800MHz-mala-15",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\ost1": "austfonna-profile-2005-800MHz-mala-16",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\ost2": "austfonna-profile-2005-800MHz-mala-17",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\ost3": "austfonna-profile-2005-800MHz-mala-18",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\ost4": "austfonna-profile-2005-800MHz-mala-19",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\ost5": "austfonna-profile-2005-800MHz-mala-20",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\ost6": "austfonna-profile-2005-800MHz-mala-21",
        r"Austfonna\2005\Level0_COP_Malå_800MHz\ost7": "austfonna-profile-2005-800MHz-mala-22",


        # AUSTFONNA 2006
        # main
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile3_030506": "austfonna-profile-2006-800MHz-mala-01",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile13_020506": "austfonna-profile-2006-800MHz-mala-02",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile14_020506": "austfonna-profile-2006-800MHz-mala-03",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile15_020506": "austfonna-profile-2006-800MHz-mala-04",

        # the rest 
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile3_010506": "austfonna-profile-2006-800MHz-mala-05",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile6_010506": "austfonna-profile-2006-800MHz-mala-06",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile7_010506": "austfonna-profile-2006-800MHz-mala-07",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile8_010506": "austfonna-profile-2006-800MHz-mala-08",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile9_010506": "austfonna-profile-2006-800MHz-mala-09",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile10_010506": "austfonna-profile-2006-800MHz-mala-10",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile11_010506": "austfonna-profile-2006-800MHz-mala-11",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile12_010506": "austfonna-profile-2006-800MHz-mala-12",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile13_010506": "austfonna-profile-2006-800MHz-mala-13",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile14_010506": "austfonna-profile-2006-800MHz-mala-14",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile15_010506": "austfonna-profile-2006-800MHz-mala-15",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile5_020506": "austfonna-profile-2006-800MHz-mala-16",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile6_020506": "austfonna-profile-2006-800MHz-mala-17",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile7_020506": "austfonna-profile-2006-800MHz-mala-18",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile8_020506": "austfonna-profile-2006-800MHz-mala-19",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile9_020506": "austfonna-profile-2006-800MHz-mala-20",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile10_020506": "austfonna-profile-2006-800MHz-mala-21",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile11_020506": "austfonna-profile-2006-800MHz-mala-22",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile12_020506": "austfonna-profile-2006-800MHz-mala-23",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile16_020506": "austfonna-profile-2006-800MHz-mala-24",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile1_030506": "austfonna-profile-2006-800MHz-mala-25",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile2_030506": "austfonna-profile-2006-800MHz-mala-26",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile4_030506": "austfonna-profile-2006-800MHz-mala-27",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile5_030506": "austfonna-profile-2006-800MHz-mala-28",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile6_030506": "austfonna-profile-2006-800MHz-mala-29",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile7_030506": "austfonna-profile-2006-800MHz-mala-30",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile8_030506": "austfonna-profile-2006-800MHz-mala-31",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile2_040506": "austfonna-profile-2006-800MHz-mala-32",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile3_040506": "austfonna-profile-2006-800MHz-mala-33",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile4_040506": "austfonna-profile-2006-800MHz-mala-34",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile1_270406": "austfonna-profile-2006-800MHz-mala-35",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile2_270406": "austfonna-profile-2006-800MHz-mala-36",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile3_270406": "austfonna-profile-2006-800MHz-mala-37",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile5_270406": "austfonna-profile-2006-800MHz-mala-38",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile6_270406": "austfonna-profile-2006-800MHz-mala-39",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile7_270406": "austfonna-profile-2006-800MHz-mala-40",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile8_270406": "austfonna-profile-2006-800MHz-mala-41",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile9_270406": "austfonna-profile-2006-800MHz-mala-42",
        r"Austfonna\2006\Level0_COP_Malå_800MHz\Profile10_270406": "austfonna-profile-2006-800MHz-mala-43",

        #AUSTFONNA 2007:
        # main
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-3": "austfonna-profile-2007-800MHz-mala-01",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-15": "austfonna-profile-2007-800MHz-mala-02",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2504-2": "austfonna-profile-2007-800MHz-mala-03",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2504-3": "austfonna-profile-2007-800MHz-mala-04",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-2": "austfonna-profile-2007-800MHz-mala-05",

        # the rest
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-1": "austfonna-profile-2007-800MHz-mala-06",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-2": "austfonna-profile-2007-800MHz-mala-07",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-3": "austfonna-profile-2007-800MHz-mala-08",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-4": "austfonna-profile-2007-800MHz-mala-09",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-5": "austfonna-profile-2007-800MHz-mala-10",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-6": "austfonna-profile-2007-800MHz-mala-11",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-7": "austfonna-profile-2007-800MHz-mala-12",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-8": "austfonna-profile-2007-800MHz-mala-13",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\0105-121-9": "austfonna-profile-2007-800MHz-mala-14",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-4": "austfonna-profile-2007-800MHz-mala-15",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-5": "austfonna-profile-2007-800MHz-mala-16",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-6": "austfonna-profile-2007-800MHz-mala-17",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-7": "austfonna-profile-2007-800MHz-mala-18",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-8": "austfonna-profile-2007-800MHz-mala-19",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-9": "austfonna-profile-2007-800MHz-mala-20",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-10": "austfonna-profile-2007-800MHz-mala-21",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-11": "austfonna-profile-2007-800MHz-mala-22",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-12": "austfonna-profile-2007-800MHz-mala-23",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-13": "austfonna-profile-2007-800MHz-mala-24",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2204-14": "austfonna-profile-2007-800MHz-mala-25",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-12": "austfonna-profile-2007-800MHz-mala-26",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-13": "austfonna-profile-2007-800MHz-mala-27",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-14": "austfonna-profile-2007-800MHz-mala-28",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-15": "austfonna-profile-2007-800MHz-mala-29",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-16": "austfonna-profile-2007-800MHz-mala-30",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-17": "austfonna-profile-2007-800MHz-mala-31",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-18": "austfonna-profile-2007-800MHz-mala-32",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-19": "austfonna-profile-2007-800MHz-mala-33",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-20": "austfonna-profile-2007-800MHz-mala-34",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-21": "austfonna-profile-2007-800MHz-mala-35",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2304-22": "austfonna-profile-2007-800MHz-mala-36",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2504-4": "austfonna-profile-2007-800MHz-mala-37",

        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-122-1": "austfonna-profile-2007-800MHz-mala-38",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-122-2": "austfonna-profile-2007-800MHz-mala-39",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-122-3": "austfonna-profile-2007-800MHz-mala-40",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-122-4": "austfonna-profile-2007-800MHz-mala-41",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-122-5": "austfonna-profile-2007-800MHz-mala-42",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-122-6": "austfonna-profile-2007-800MHz-mala-43",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-122-7": "austfonna-profile-2007-800MHz-mala-44",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-797-1": "austfonna-profile-2007-800MHz-mala-45",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-797-2": "austfonna-profile-2007-800MHz-mala-46",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-797-3": "austfonna-profile-2007-800MHz-mala-47",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-797-4": "austfonna-profile-2007-800MHz-mala-48",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\2904-cry4": "austfonna-profile-2007-800MHz-mala-49",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-1": "austfonna-profile-2007-800MHz-mala-50",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-3": "austfonna-profile-2007-800MHz-mala-51",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-4": "austfonna-profile-2007-800MHz-mala-52",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-5": "austfonna-profile-2007-800MHz-mala-53",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-6": "austfonna-profile-2007-800MHz-mala-54",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-cr": "austfonna-profile-2007-800MHz-mala-55",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\base07-1k2": "austfonna-profile-2007-800MHz-mala-56",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\base07-av-1": "austfonna-profile-2007-800MHz-mala-57",
        r"Austfonna\2007\Level0_COP_Malå_800MHz\base07-ns1": "austfonna-profile-2007-800MHz-mala-58",
        

        #AUSTFONNA 2008:
        # main
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-2": "austfonna-profile-2008-800MHz-mala-01",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-21": "austfonna-profile-2008-800MHz-mala-02",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-111-a-1": "austfonna-profile-2008-800MHz-mala-03",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\duv-ned1_3004-08": "austfonna-profile-2008-800MHz-mala-04",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p111_b08_nw1_0205-08": "austfonna-profile-2008-800MHz-mala-05",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p120-n4_2704-08": "austfonna-profile-2008-800MHz-mala-06",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p120-n5_2704-08": "austfonna-profile-2008-800MHz-mala-07",

        # the rest
        r"Austfonna\2008\Level0_COP_Malå_800MHz\121-a1": "austfonna-profile-2008-800MHz-mala-08",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\121-a2": "austfonna-profile-2008-800MHz-mala-09",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\121-a3": "austfonna-profile-2008-800MHz-mala-10",   
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned1": "austfonna-profile-2008-800MHz-mala-11",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned2": "austfonna-profile-2008-800MHz-mala-12",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned3": "austfonna-profile-2008-800MHz-mala-13",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned4": "austfonna-profile-2008-800MHz-mala-14",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned5": "austfonna-profile-2008-800MHz-mala-15",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned6": "austfonna-profile-2008-800MHz-mala-16",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned7": "austfonna-profile-2008-800MHz-mala-17",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned8": "austfonna-profile-2008-800MHz-mala-18",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\472-ned9": "austfonna-profile-2008-800MHz-mala-19",  
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-22": "austfonna-profile-2008-800MHz-mala-20",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-23": "austfonna-profile-2008-800MHz-mala-21",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-118-v1": "austfonna-profile-2008-800MHz-mala-22",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-121-a1": "austfonna-profile-2008-800MHz-mala-23",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-472-s1": "austfonna-profile-2008-800MHz-mala-24",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\cry-472-n-1": "austfonna-profile-2008-800MHz-mala-25",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\cry-472-n-2": "austfonna-profile-2008-800MHz-mala-26",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\cry-472-n-3": "austfonna-profile-2008-800MHz-mala-27",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\cry-797-s1": "austfonna-profile-2008-800MHz-mala-28",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\cry-797-s2": "austfonna-profile-2008-800MHz-mala-29",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\cry-797-s3": "austfonna-profile-2008-800MHz-mala-30",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\cry-797-s4": "austfonna-profile-2008-800MHz-mala-31",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\duv-ned2_3004-08": "austfonna-profile-2008-800MHz-mala-32",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\duv-ned4_3004-08": "austfonna-profile-2008-800MHz-mala-34",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\duv-ned5_3004-08": "austfonna-profile-2008-800MHz-mala-35",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\duv-ned6_3004-08": "austfonna-profile-2008-800MHz-mala-36",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\duv-ned7_3004-08": "austfonna-profile-2008-800MHz-mala-37",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p118-E1": "austfonna-profile-2008-800MHz-mala-38",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p118-E2": "austfonna-profile-2008-800MHz-mala-39",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p118-E3": "austfonna-profile-2008-800MHz-mala-40",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p120-n1_2704-08": "austfonna-profile-2008-800MHz-mala-41",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p120-n2_2704-08": "austfonna-profile-2008-800MHz-mala-42",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p120-n3_2704-08": "austfonna-profile-2008-800MHz-mala-43",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p120-n6_2704-08": "austfonna-profile-2008-800MHz-mala-44",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p122-S1": "austfonna-profile-2008-800MHz-mala-45",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p122-S2": "austfonna-profile-2008-800MHz-mala-46",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p122-S3": "austfonna-profile-2008-800MHz-mala-47",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p122-S4": "austfonna-profile-2008-800MHz-mala-48",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-opp1": "austfonna-profile-2008-800MHz-mala-49",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-opp2": "austfonna-profile-2008-800MHz-mala-50",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-opp4": "austfonna-profile-2008-800MHz-mala-51",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S1": "austfonna-profile-2008-800MHz-mala-52",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S2": "austfonna-profile-2008-800MHz-mala-53",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S3": "austfonna-profile-2008-800MHz-mala-54",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S4": "austfonna-profile-2008-800MHz-mala-55",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S5": "austfonna-profile-2008-800MHz-mala-56",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S6": "austfonna-profile-2008-800MHz-mala-57",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S7": "austfonna-profile-2008-800MHz-mala-58",
        r"Austfonna\2008\Level0_COP_Malå_800MHz\p797-S8": "austfonna-profile-2008-800MHz-mala-59",

        #AUSTFONNA 2009:
        # main
        r"Austfonna\2009\Level0_COP_Malå_800MHz\eton2_3004-09": "austfonna-profile-2009-800MHz-mala-01",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\nv2_2904-09": "austfonna-profile-2009-800MHz-mala-02",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\nv3_2904-09": "austfonna-profile-2009-800MHz-mala-03",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\nv5-invers_2904-09": "austfonna-profile-2009-800MHz-mala-04",

        # the rest
        r"Austfonna\2009\Level0_COP_Malå_800MHz\118-1-invers": "austfonna-profile-2009-800MHz-mala-05",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-1": "austfonna-profile-2009-800MHz-mala-06",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-2": "austfonna-profile-2009-800MHz-mala-07",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-3": "austfonna-profile-2009-800MHz-mala-08",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-4": "austfonna-profile-2009-800MHz-mala-09",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-5": "austfonna-profile-2009-800MHz-mala-10",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-6": "austfonna-profile-2009-800MHz-mala-11",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-7": "austfonna-profile-2009-800MHz-mala-12",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-8": "austfonna-profile-2009-800MHz-mala-13",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-9": "austfonna-profile-2009-800MHz-mala-14",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472s-10": "austfonna-profile-2009-800MHz-mala-15",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472-soer1": "austfonna-profile-2009-800MHz-mala-16",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472-soer2": "austfonna-profile-2009-800MHz-mala-17",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\472-soer3": "austfonna-profile-2009-800MHz-mala-18",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\797-nord-1": "austfonna-profile-2009-800MHz-mala-19",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\797-nord-2": "austfonna-profile-2009-800MHz-mala-20",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\797-nord-3": "austfonna-profile-2009-800MHz-mala-21",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\797-nord-4": "austfonna-profile-2009-800MHz-mala-22",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\dlr-a-b1": "austfonna-profile-2009-800MHz-mala-23",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\dlr-c-d1": "austfonna-profile-2009-800MHz-mala-24",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\eton1_3004-09": "austfonna-profile-2009-800MHz-mala-25",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\eton3_3004-09": "austfonna-profile-2009-800MHz-mala-26",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\eton4_3004-09": "austfonna-profile-2009-800MHz-mala-27",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\eton5_3004-09": "austfonna-profile-2009-800MHz-mala-28",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\hart1": "austfonna-profile-2009-800MHz-mala-29",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\hart2": "austfonna-profile-2009-800MHz-mala-30",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\hart3": "austfonna-profile-2009-800MHz-mala-31",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\hart4": "austfonna-profile-2009-800MHz-mala-32",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\hart5": "austfonna-profile-2009-800MHz-mala-33",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\hart6": "austfonna-profile-2009-800MHz-mala-34",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\hart7": "austfonna-profile-2009-800MHz-mala-35",
        r"Austfonna\2009\Level0_COP_Malå_800MHz\nv4_2904-09": "austfonna-profile-2009-800MHz-mala-36",


        #AUSTFONNA 2010:
        # main
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0012_A1_0505-10": "austfonna-profile-2010-800MHz-mala-01",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0041_A1_2504-10": "austfonna-profile-2010-800MHz-mala-02",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0042_A1_2504-10": "austfonna-profile-2010-800MHz-mala-03",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0043_A1_2504-10": "austfonna-profile-2010-800MHz-mala-04",

        # the rest
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0001_A1_0405-10": "austfonna-profile-2010-800MHz-mala-05",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0002_A1_0405-10": "austfonna-profile-2010-800MHz-mala-06",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0003_A1_0405-10": "austfonna-profile-2010-800MHz-mala-07",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0004_A1_0405-10": "austfonna-profile-2010-800MHz-mala-08",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0005_A1_0405-10": "austfonna-profile-2010-800MHz-mala-09",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0006_A1_0405-10": "austfonna-profile-2010-800MHz-mala-10",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0007_A1_0405-10": "austfonna-profile-2010-800MHz-mala-11",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0008_A1_0405-10": "austfonna-profile-2010-800MHz-mala-12",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0009_A1_0405-10": "austfonna-profile-2010-800MHz-mala-13",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0010_A1_0405-10": "austfonna-profile-2010-800MHz-mala-14",

        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0011_A1_0505-10": "austfonna-profile-2010-800MHz-mala-15",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0013_A1_0505-10": "austfonna-profile-2010-800MHz-mala-16",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0014_A1_0505-10": "austfonna-profile-2010-800MHz-mala-17",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0016_A1_0505-10": "austfonna-profile-2010-800MHz-mala-18",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0017_A1_0505-10": "austfonna-profile-2010-800MHz-mala-19",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0018_A1_0505-10": "austfonna-profile-2010-800MHz-mala-20",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0020_A1_0505-10": "austfonna-profile-2010-800MHz-mala-21",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0021_A1_0505-10": "austfonna-profile-2010-800MHz-mala-22",

        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0001_A1_2904-10": "austfonna-profile-2010-800MHz-mala-23",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0002_A1_2904-10": "austfonna-profile-2010-800MHz-mala-24",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0003_A1_2904-10": "austfonna-profile-2010-800MHz-mala-25",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0004_A1_2904-10": "austfonna-profile-2010-800MHz-mala-26",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0005_A1_2904-10": "austfonna-profile-2010-800MHz-mala-27",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0006_A1_2904-10": "austfonna-profile-2010-800MHz-mala-28",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0007_A1_2904-10": "austfonna-profile-2010-800MHz-mala-29",

        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0044_A1_2504-10": "austfonna-profile-2010-800MHz-mala-30",

        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0045_A1_2604-10": "austfonna-profile-2010-800MHz-mala-31",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0046_A1_2604-10": "austfonna-profile-2010-800MHz-mala-32",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0047_A1_2604-10": "austfonna-profile-2010-800MHz-mala-33",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0048_A1_2604-10": "austfonna-profile-2010-800MHz-mala-34",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0049_A1_2604-10": "austfonna-profile-2010-800MHz-mala-35",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0050_A1_2604-10": "austfonna-profile-2010-800MHz-mala-36",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0051_A1_2604-10": "austfonna-profile-2010-800MHz-mala-37",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0052_A1_2604-10": "austfonna-profile-2010-800MHz-mala-38",
        r"Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0053_A1_2604-10": "austfonna-profile-2010-800MHz-mala-39",


        #AUSTFONNA 2011:
        # main
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0305-11": "austfonna-profile-2011-800MHz-mala-01",  
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0105-11": "austfonna-profile-2011-800MHz-mala-02", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_1105-11": "austfonna-profile-2011-800MHz-mala-03", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0009_A1_0705-11": "austfonna-profile-2011-800MHz-mala-04",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0017_A1_0405-11": "austfonna-profile-2011-800MHz-mala-05",

        # the rest
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_0105-11": "austfonna-profile-2011-800MHz-mala-06", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_0105-11": "austfonna-profile-2011-800MHz-mala-07", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0005_A1_0105-11": "austfonna-profile-2011-800MHz-mala-08", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0006_A1_0105-11": "austfonna-profile-2011-800MHz-mala-09", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0007_A1_0105-11": "austfonna-profile-2011-800MHz-mala-10", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0008_A1_0105-11": "austfonna-profile-2011-800MHz-mala-11", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0009_A1_0105-11": "austfonna-profile-2011-800MHz-mala-12", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0010_A1_0105-11": "austfonna-profile-2011-800MHz-mala-13", 

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0001_A1_0205-11": "austfonna-profile-2011-800MHz-mala-14", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0205-11": "austfonna-profile-2011-800MHz-mala-15",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_0205-11": "austfonna-profile-2011-800MHz-mala-16",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_0205-11": "austfonna-profile-2011-800MHz-mala-17",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0005_A1_0205-11": "austfonna-profile-2011-800MHz-mala-18",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0006_A1_0205-11": "austfonna-profile-2011-800MHz-mala-19",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0007_A1_0205-11": "austfonna-profile-2011-800MHz-mala-20", 

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0001_A1_0305-11": "austfonna-profile-2011-800MHz-mala-21", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_0305-11": "austfonna-profile-2011-800MHz-mala-22", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_0305-11": "austfonna-profile-2011-800MHz-mala-23", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0005_A1_0305-11": "austfonna-profile-2011-800MHz-mala-24", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0006_A1_0305-11": "austfonna-profile-2011-800MHz-mala-25", 

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0013_A1_0405-11": "austfonna-profile-2011-800MHz-mala-26",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0016_A1_0405-11": "austfonna-profile-2011-800MHz-mala-27",

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0505-11": "austfonna-profile-2011-800MHz-mala-28",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_0505-11": "austfonna-profile-2011-800MHz-mala-29",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_0505-11": "austfonna-profile-2011-800MHz-mala-30",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0005_A1_0505-11": "austfonna-profile-2011-800MHz-mala-31",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0006_A1_0505-11": "austfonna-profile-2011-800MHz-mala-32",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0007_A1_0505-11": "austfonna-profile-2011-800MHz-mala-33",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0008_A1_0505-11": "austfonna-profile-2011-800MHz-mala-34",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0009_A1_0505-11": "austfonna-profile-2011-800MHz-mala-35",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0010_A1_0505-11": "austfonna-profile-2011-800MHz-mala-36",

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0001_A1_0605-11": "austfonna-profile-2011-800MHz-mala-37",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0605-11": "austfonna-profile-2011-800MHz-mala-38",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_0605-11": "austfonna-profile-2011-800MHz-mala-39",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_0605-11": "austfonna-profile-2011-800MHz-mala-40",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0005_A1_0605-11": "austfonna-profile-2011-800MHz-mala-41",

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0001_A1_0705-11": "austfonna-profile-2011-800MHz-mala-42",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0705-11": "austfonna-profile-2011-800MHz-mala-43",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_0705-11": "austfonna-profile-2011-800MHz-mala-44",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_0705-11": "austfonna-profile-2011-800MHz-mala-45",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0006_A1_0705-11": "austfonna-profile-2011-800MHz-mala-46",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0007_A1_0705-11": "austfonna-profile-2011-800MHz-mala-47",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0008_A1_0705-11": "austfonna-profile-2011-800MHz-mala-48",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0010_A1_0705-11": "austfonna-profile-2011-800MHz-mala-49",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0011_A1_0705-11": "austfonna-profile-2011-800MHz-mala-50",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0012_A1_0705-11": "austfonna-profile-2011-800MHz-mala-51",

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0001_A1_0805-11": "austfonna-profile-2011-800MHz-mala-52",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0805-11": "austfonna-profile-2011-800MHz-mala-53",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_0805-11": "austfonna-profile-2011-800MHz-mala-54",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_0805-11": "austfonna-profile-2011-800MHz-mala-55",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0005_A1_0805-11": "austfonna-profile-2011-800MHz-mala-56",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0006_A1_0805-11": "austfonna-profile-2011-800MHz-mala-57",

        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_1105-11": "austfonna-profile-2011-800MHz-mala-58", 
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0004_A1_1105-11": "austfonna-profile-2011-800MHz-mala-59",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0005_A1_1105-11": "austfonna-profile-2011-800MHz-mala-60",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0006_A1_1105-11": "austfonna-profile-2011-800MHz-mala-61",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0007_A1_1105-11": "austfonna-profile-2011-800MHz-mala-62",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0008_A1_1105-11": "austfonna-profile-2011-800MHz-mala-63",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0010_A1_1105-11": "austfonna-profile-2011-800MHz-mala-64",
        r"Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0011_A1_1105-11": "austfonna-profile-2011-800MHz-mala-65",



        # AUSTFONNA 2012
        # main
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0011_A1": "austfonna-profile-2012-800MHz-mala-01", 
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0012_A1": "austfonna-profile-2012-800MHz-mala-02",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0017_A1": "austfonna-profile-2012-800MHz-mala-03",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0023_A1": "austfonna-profile-2012-800MHz-mala-04",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0024_A1": "austfonna-profile-2012-800MHz-mala-05",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0035_A1": "austfonna-profile-2012-800MHz-mala-06",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0042_A1": "austfonna-profile-2012-800MHz-mala-07",

        # the rest
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0008_A1": "austfonna-profile-2012-800MHz-mala-08",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0009_A1": "austfonna-profile-2012-800MHz-mala-09",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0010_A1": "austfonna-profile-2012-800MHz-mala-10",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0013_A1": "austfonna-profile-2012-800MHz-mala-11",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0014_A1": "austfonna-profile-2012-800MHz-mala-12",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0015_A1": "austfonna-profile-2012-800MHz-mala-13",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0016_A1": "austfonna-profile-2012-800MHz-mala-14",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0018_A1": "austfonna-profile-2012-800MHz-mala-15",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0019_A1": "austfonna-profile-2012-800MHz-mala-16",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0020_A1": "austfonna-profile-2012-800MHz-mala-17",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0021_A1": "austfonna-profile-2012-800MHz-mala-18",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0022_A1": "austfonna-profile-2012-800MHz-mala-19",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0025_A1": "austfonna-profile-2012-800MHz-mala-20",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0026_A1": "austfonna-profile-2012-800MHz-mala-21",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0029_A1": "austfonna-profile-2012-800MHz-mala-22",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0030_A1": "austfonna-profile-2012-800MHz-mala-23",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0031_A1": "austfonna-profile-2012-800MHz-mala-24",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0032_A1": "austfonna-profile-2012-800MHz-mala-25",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0033_A1": "austfonna-profile-2012-800MHz-mala-26",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0034_A1": "austfonna-profile-2012-800MHz-mala-27",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0036_A1": "austfonna-profile-2012-800MHz-mala-28",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0037_A1": "austfonna-profile-2012-800MHz-mala-29",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0038_A1": "austfonna-profile-2012-800MHz-mala-30",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0039_A1": "austfonna-profile-2012-800MHz-mala-31",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0040_A1": "austfonna-profile-2012-800MHz-mala-32",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0041_A1": "austfonna-profile-2012-800MHz-mala-33",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0045_A1": "austfonna-profile-2012-800MHz-mala-34",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0046_A1": "austfonna-profile-2012-800MHz-mala-35",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0047_A1": "austfonna-profile-2012-800MHz-mala-36",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0048_A1": "austfonna-profile-2012-800MHz-mala-37",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0049_A1": "austfonna-profile-2012-800MHz-mala-38",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0050_A1": "austfonna-profile-2012-800MHz-mala-39",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0051_A1": "austfonna-profile-2012-800MHz-mala-40",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0052_A1": "austfonna-profile-2012-800MHz-mala-41",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0053_A1": "austfonna-profile-2012-800MHz-mala-42",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0054_A1": "austfonna-profile-2012-800MHz-mala-43",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0055_A1": "austfonna-profile-2012-800MHz-mala-44",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0056_A1": "austfonna-profile-2012-800MHz-mala-45",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0057_A1": "austfonna-profile-2012-800MHz-mala-46",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0058_A1": "austfonna-profile-2012-800MHz-mala-47",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0059_A1": "austfonna-profile-2012-800MHz-mala-48",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0061_A1": "austfonna-profile-2012-800MHz-mala-49",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0062_A1": "austfonna-profile-2012-800MHz-mala-50",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0063_A1": "austfonna-profile-2012-800MHz-mala-51",
        r"Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0064_A1": "austfonna-profile-2012-800MHz-mala-52",

                                                               
        # AUSTFONNA 2013
        # main
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0007_A1": "austfonna-profile-2013-800MHz-mala-01", 
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0032_A1": "austfonna-profile-2013-800MHz-mala-02", 
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0044_A1": "austfonna-profile-2013-800MHz-mala-03",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0045_A1": "austfonna-profile-2013-800MHz-mala-04",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0047_A1": "austfonna-profile-2013-800MHz-mala-05",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0066_A1": "austfonna-profile-2013-800MHz-mala-06",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0069_A1": "austfonna-profile-2013-800MHz-mala-07",

        #the rest
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0035_A1": "austfonna-profile-2013-800MHz-mala-08",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0036_A1": "austfonna-profile-2013-800MHz-mala-09",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0037_A1": "austfonna-profile-2013-800MHz-mala-10",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0053_A1": "austfonna-profile-2013-800MHz-mala-11",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0054_A1": "austfonna-profile-2013-800MHz-mala-12",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0005_A1": "austfonna-profile-2013-800MHz-mala-13",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0023_A1": "austfonna-profile-2013-800MHz-mala-14",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0025_A1": "austfonna-profile-2013-800MHz-mala-15",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0026_A1": "austfonna-profile-2013-800MHz-mala-16",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0027_A1": "austfonna-profile-2013-800MHz-mala-17",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0028_A1": "austfonna-profile-2013-800MHz-mala-18",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0029_A1": "austfonna-profile-2013-800MHz-mala-19",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0030_A1": "austfonna-profile-2013-800MHz-mala-20",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0031_A1": "austfonna-profile-2013-800MHz-mala-21",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0033_A1": "austfonna-profile-2013-800MHz-mala-22",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0034_A1": "austfonna-profile-2013-800MHz-mala-23",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0038_A1": "austfonna-profile-2013-800MHz-mala-24",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0039_A1": "austfonna-profile-2013-800MHz-mala-25",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0040_A1": "austfonna-profile-2013-800MHz-mala-26",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0041_A1": "austfonna-profile-2013-800MHz-mala-27",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0042_A1": "austfonna-profile-2013-800MHz-mala-28",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0043_A1": "austfonna-profile-2013-800MHz-mala-29",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0048_A1": "austfonna-profile-2013-800MHz-mala-30",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0049_A1": "austfonna-profile-2013-800MHz-mala-31",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0050_A1": "austfonna-profile-2013-800MHz-mala-32",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0051_A1": "austfonna-profile-2013-800MHz-mala-33",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0052_A1": "austfonna-profile-2013-800MHz-mala-34",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0055_A1": "austfonna-profile-2013-800MHz-mala-35",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0056_A1": "austfonna-profile-2013-800MHz-mala-36",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0057_A1": "austfonna-profile-2013-800MHz-mala-37",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0058_A1": "austfonna-profile-2013-800MHz-mala-38",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0059_A1": "austfonna-profile-2013-800MHz-mala-39",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0062_A1": "austfonna-profile-2013-800MHz-mala-40",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0067_A1": "austfonna-profile-2013-800MHz-mala-41",
        r"Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0068_A1": "austfonna-profile-2013-800MHz-mala-42",


        # AUSTFONNA 2014
        # main
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0172_A1": "austfonna-profile-2014-800MHz-mala-01", 
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0173_A1": "austfonna-profile-2014-800MHz-mala-02", 
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0175_A1": "austfonna-profile-2014-800MHz-mala-03", 
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0186_A1": "austfonna-profile-2014-800MHz-mala-04",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0198_A1": "austfonna-profile-2014-800MHz-mala-05",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0199_A1": "austfonna-profile-2014-800MHz-mala-06",

        # the rest
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0174_A1": "austfonna-profile-2014-800MHz-mala-07", 
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0178_A1": "austfonna-profile-2014-800MHz-mala-08",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0179_A1": "austfonna-profile-2014-800MHz-mala-09",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0180_A1": "austfonna-profile-2014-800MHz-mala-10",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0181_A1": "austfonna-profile-2014-800MHz-mala-11",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0182_A1": "austfonna-profile-2014-800MHz-mala-12",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0183_A1": "austfonna-profile-2014-800MHz-mala-13",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0184_A1": "austfonna-profile-2014-800MHz-mala-14",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0185_A1": "austfonna-profile-2014-800MHz-mala-15",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0187_A1": "austfonna-profile-2014-800MHz-mala-16",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0188_A1": "austfonna-profile-2014-800MHz-mala-17",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0189_A1": "austfonna-profile-2014-800MHz-mala-18",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0190_A1": "austfonna-profile-2014-800MHz-mala-19",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0191_A1": "austfonna-profile-2014-800MHz-mala-20",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0192_A1": "austfonna-profile-2014-800MHz-mala-21",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0193_A1": "austfonna-profile-2014-800MHz-mala-22",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0194_A1": "austfonna-profile-2014-800MHz-mala-23",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0195_A1": "austfonna-profile-2014-800MHz-mala-24",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0196_A1": "austfonna-profile-2014-800MHz-mala-25",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0197_A1": "austfonna-profile-2014-800MHz-mala-26",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0200_A1": "austfonna-profile-2014-800MHz-mala-27",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0201_A1": "austfonna-profile-2014-800MHz-mala-28",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0202_A1": "austfonna-profile-2014-800MHz-mala-29",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0203_A1": "austfonna-profile-2014-800MHz-mala-30",
        r"Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0204_A1": "austfonna-profile-2014-800MHz-mala-31",


        # AUSTFONNA 2015
        # main
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0001_A1-NW_Helvete": "austfonna-profile-2015-800MHz-mala-01", 
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0002_A1-NW_Helvete": "austfonna-profile-2015-800MHz-mala-02",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0004_A1-NW_Helvete": "austfonna-profile-2015-800MHz-mala-03",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0006_A1-150430_Eton": "austfonna-profile-2015-800MHz-mala-04",

        # the rest
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0005_A1-NW_Helvete": "austfonna-profile-2015-800MHz-mala-05",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0002_A1-150430_Eton": "austfonna-profile-2015-800MHz-mala-06",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0005_A1-150430_Eton": "austfonna-profile-2015-800MHz-mala-07",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0007_A1-150430_Eton": "austfonna-profile-2015-800MHz-mala-08",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0006_A1_150504_472_797_Nord": "austfonna-profile-2015-800MHz-mala-09",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0007_A1_150504_472_797_Nord": "austfonna-profile-2015-800MHz-mala-10",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0008_A1_150504_472_797_Nord": "austfonna-profile-2015-800MHz-mala-11",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0009_A1_150504_472_797_Nord": "austfonna-profile-2015-800MHz-mala-12",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0010_A1_150504_472_797_Nord": "austfonna-profile-2015-800MHz-mala-13",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0011_A1_150504_472_797_Nord": "austfonna-profile-2015-800MHz-mala-14",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0012_A1_150504_472_797_Nord": "austfonna-profile-2015-800MHz-mala-15",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0008_A1_150501_Hartog": "austfonna-profile-2015-800MHz-mala-16",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0009_A1_150501_Hartog": "austfonna-profile-2015-800MHz-mala-17",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0010_A1_150501_Hartog": "austfonna-profile-2015-800MHz-mala-18",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0011_A1_150501_Hartog": "austfonna-profile-2015-800MHz-mala-19",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0012_A1_150501_Hartog": "austfonna-profile-2015-800MHz-mala-20",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0013_A1_150501_Hartog": "austfonna-profile-2015-800MHz-mala-21",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0014_A1_150501_Hartog": "austfonna-profile-2015-800MHz-mala-22",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0013_A1_Brasvell": "austfonna-profile-2015-800MHz-mala-23",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0014_A1_Brasvell": "austfonna-profile-2015-800MHz-mala-24",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0015_A1_Brasvell": "austfonna-profile-2015-800MHz-mala-25",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0016_A1_Brasvell": "austfonna-profile-2015-800MHz-mala-26",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0017_A1_Brasvell": "austfonna-profile-2015-800MHz-mala-27",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0018_A1_Brasvell": "austfonna-profile-2015-800MHz-mala-28",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0017_A1_150502_POCA": "austfonna-profile-2015-800MHz-mala-29",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0018_A1_150502_POCA": "austfonna-profile-2015-800MHz-mala-30",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0019_A1_150502_POCA": "austfonna-profile-2015-800MHz-mala-31",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0020_A1_150502_POCA": "austfonna-profile-2015-800MHz-mala-32",
        #r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0021_A1_150502_POCA": "austfonna-profile-2015-800MHz-mala-33",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0022_A1_150502_POCA": "austfonna-profile-2015-800MHz-mala-34",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0020_A1_150506_Eton_pond_IMAU_core": "austfonna-profile-2015-800MHz-mala-35",
        r"Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0021_A1_150506_Eton_pond_IMAU_core": "austfonna-profile-2015-800MHz-mala-36",


        # AUSTFONNA 2016 
        # main
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0028_A1": "austfonna-profile-2016-800MHz-mala-01", 
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0029_A1": "austfonna-profile-2016-800MHz-mala-02", 
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0031_A1": "austfonna-profile-2016-800MHz-mala-03", 
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0032_A1": "austfonna-profile-2016-800MHz-mala-04",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0033_A1": "austfonna-profile-2016-800MHz-mala-05",

        # the rest
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0001_A1": "austfonna-profile-2016-800MHz-mala-06",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0002_A1": "austfonna-profile-2016-800MHz-mala-07",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0003_A1": "austfonna-profile-2016-800MHz-mala-08",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0004_A1": "austfonna-profile-2016-800MHz-mala-09",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0005_A1": "austfonna-profile-2016-800MHz-mala-10",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0006_A1": "austfonna-profile-2016-800MHz-mala-11",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0008_A1": "austfonna-profile-2016-800MHz-mala-12",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0009_A1": "austfonna-profile-2016-800MHz-mala-13",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0010_A1": "austfonna-profile-2016-800MHz-mala-14",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0011_A1": "austfonna-profile-2016-800MHz-mala-15",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0027_A1": "austfonna-profile-2016-800MHz-mala-16", 
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0030_A1": "austfonna-profile-2016-800MHz-mala-17",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0034_A1": "austfonna-profile-2016-800MHz-mala-18",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0036_A1": "austfonna-profile-2016-800MHz-mala-19",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0037_A1": "austfonna-profile-2016-800MHz-mala-20",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0039_A1": "austfonna-profile-2016-800MHz-mala-21",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0040_A1": "austfonna-profile-2016-800MHz-mala-22",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0042_A1": "austfonna-profile-2016-800MHz-mala-23",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0046_A1": "austfonna-profile-2016-800MHz-mala-24",
        r"Austfonna\2016\Level0_COP_Malå_800MHz\DAT_0047_A1": "austfonna-profile-2016-800MHz-mala-25",


        # AUSTFONNA 2017
        # main
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0138_A1": "austfonna-profile-2017-800MHz-mala-01",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0139_A1": "austfonna-profile-2017-800MHz-mala-02",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0150_A1": "austfonna-profile-2017-800MHz-mala-03",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0151_A1": "austfonna-profile-2017-800MHz-mala-04",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0153_A1": "austfonna-profile-2017-800MHz-mala-05",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0154_A1": "austfonna-profile-2017-800MHz-mala-06",
        
        # the rest
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0127_A1": "austfonna-profile-2017-800MHz-mala-07",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0128_A1": "austfonna-profile-2017-800MHz-mala-08",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0129_A1": "austfonna-profile-2017-800MHz-mala-09",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0130_A1": "austfonna-profile-2017-800MHz-mala-10",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0136_A1": "austfonna-profile-2017-800MHz-mala-11",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0137_A1": "austfonna-profile-2017-800MHz-mala-12",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0140_A1": "austfonna-profile-2017-800MHz-mala-13",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0141_A1": "austfonna-profile-2017-800MHz-mala-14",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0142_A1": "austfonna-profile-2017-800MHz-mala-15",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0143_A1": "austfonna-profile-2017-800MHz-mala-16",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0144_A1": "austfonna-profile-2017-800MHz-mala-17",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0145_A1": "austfonna-profile-2017-800MHz-mala-18",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0146_A1": "austfonna-profile-2017-800MHz-mala-19",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0147_A1": "austfonna-profile-2017-800MHz-mala-20",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0148_A1": "austfonna-profile-2017-800MHz-mala-21",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0149_A1": "austfonna-profile-2017-800MHz-mala-22",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0155_A1": "austfonna-profile-2017-800MHz-mala-23",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0156_A1": "austfonna-profile-2017-800MHz-mala-24",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0157_A1": "austfonna-profile-2017-800MHz-mala-25",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0158_A1": "austfonna-profile-2017-800MHz-mala-26",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0160_A1": "austfonna-profile-2017-800MHz-mala-27",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0161_A1": "austfonna-profile-2017-800MHz-mala-28",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0164_A1": "austfonna-profile-2017-800MHz-mala-29",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0165_A1": "austfonna-profile-2017-800MHz-mala-30",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0166_A1": "austfonna-profile-2017-800MHz-mala-31",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0168_A1": "austfonna-profile-2017-800MHz-mala-32",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0168_A1": "austfonna-profile-2017-800MHz-mala-33",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0169_A1": "austfonna-profile-2017-800MHz-mala-34",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0170_A1": "austfonna-profile-2017-800MHz-mala-35",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0171_A1": "austfonna-profile-2017-800MHz-mala-36",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0172_A1": "austfonna-profile-2017-800MHz-mala-37",
        r"Austfonna\2017\Level0_COP_Malå_800MHz\DAT_0173_A1": "austfonna-profile-2017-800MHz-mala-38",


        # AUSTFONNA 2018
        # main
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0022_A1_2104-18_MALAGS_Eton": "austfonna-profile-2018-800MHz-mala-01",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0023_A1_2104-18_MALAGS_Eton": "austfonna-profile-2018-800MHz-mala-02",

        # the rest
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0020_A1_2104-18_MALAGS_Eton": "austfonna-profile-2018-800MHz-mala-03",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0021_A1_2104-18_MALAGS_Eton": "austfonna-profile-2018-800MHz-mala-04",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0024_A1_2104-18_MALAGS_Eton": "austfonna-profile-2018-800MHz-mala-05",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0020_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-06",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0021_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-07",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0022_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-08",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0023_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-09",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0024_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-10",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0026_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-11",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0027_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-12",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0028_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-13",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0029_A1_2304-18_MALAGS": "austfonna-profile-2018-800MHz-mala-14",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0030_A1_2404-18_MALAGS": "austfonna-profile-2018-800MHz-mala-15",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0031_A1_2404-18_MALAGS": "austfonna-profile-2018-800MHz-mala-16",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0032_A1_2404-18_MALAGS": "austfonna-profile-2018-800MHz-mala-17",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0033_A1_2404-18_MALAGS": "austfonna-profile-2018-800MHz-mala-18",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0034_A1_2404-18_MALAGS": "austfonna-profile-2018-800MHz-mala-19",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0035_A1_2504-18_MALAGS": "austfonna-profile-2018-800MHz-mala-20",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0036_A1_2504-18_MALAGS": "austfonna-profile-2018-800MHz-mala-21",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0037_A1_2504-18_MALAGS": "austfonna-profile-2018-800MHz-mala-22",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0038_A1_2504-18_MALAGS": "austfonna-profile-2018-800MHz-mala-23",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0039_A1_2504-18_MALAGS": "austfonna-profile-2018-800MHz-mala-24",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0040_A1_2504-18_MALAGS": "austfonna-profile-2018-800MHz-mala-25",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0041_A1_2504-18_MALAGS": "austfonna-profile-2018-800MHz-mala-26",
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0045_A1_2604-18_MALAGS": "austfonna-profile-2018-800MHz-mala-27", 
        r"Austfonna\2018\Level0_COP_Malå_800MHz\DAT_0046_A1_2604-18_MALAGS": "austfonna-profile-2018-800MHz-mala-28",


        # AUSTFONNA 2019
        # main
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0061_A1": "austfonna-profile-2019-800MHz-mala-01",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0062_A1": "austfonna-profile-2019-800MHz-mala-02",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0063_A1": "austfonna-profile-2019-800MHz-mala-03",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0065_A1": "austfonna-profile-2019-800MHz-mala-04",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0066_A1": "austfonna-profile-2019-800MHz-mala-05",

        # the rest
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0002_A1": "austfonna-profile-2019-800MHz-mala-06",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0003_A1": "austfonna-profile-2019-800MHz-mala-07",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0004_A1": "austfonna-profile-2019-800MHz-mala-08",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0005_A1": "austfonna-profile-2019-800MHz-mala-09",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0006_A1": "austfonna-profile-2019-800MHz-mala-10",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0008_A1": "austfonna-profile-2019-800MHz-mala-12",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0009_A1": "austfonna-profile-2019-800MHz-mala-13",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0010_A1": "austfonna-profile-2019-800MHz-mala-14",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0011_A1": "austfonna-profile-2019-800MHz-mala-15",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0012_A1": "austfonna-profile-2019-800MHz-mala-16",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0059_A1": "austfonna-profile-2019-800MHz-mala-17",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0060_A1": "austfonna-profile-2019-800MHz-mala-18",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0064_A1": "austfonna-profile-2019-800MHz-mala-19",

        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0001_A1_Hartog": "austfonna-profile-2019-800MHz-mala-20",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0002_A1_Hartog": "austfonna-profile-2019-800MHz-mala-21",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0003_A1_Hartog": "austfonna-profile-2019-800MHz-mala-22",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0004_A1_Hartog": "austfonna-profile-2019-800MHz-mala-23",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0005_A1_Hartog": "austfonna-profile-2019-800MHz-mala-24",
        r"Austfonna\2019\Level0_COP_Malå_800MHz\DAT_0006_A1_Hartog": "austfonna-profile-2019-800MHz-mala-25",


    }

    for orig_dir, radar_id in renaming.items():
        # if not "austfonna-profile-2004-800MHz-mala-26" in radar_id:
        #     continue
        #if radar_id.split("-")[2] < "2019":
        #    continue
        if "2026" not in radar_id:
            continue
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
            
            if 'mala' in radar_id and filepath.suffix == ".cor" and radar_id.split("-")[2] <= "2019":
                try:
                    potential_better_corfile = replace_corfile(filepath)
                    if potential_better_corfile is not None:
                        filepath = potential_better_corfile
                except UnicodeDecodeError as exception:
                    print(f"\t\tFAILED TO READ {filepath}: {exception}")

            renamed_files[new_filepath.suffix] = (filepath, new_filepath)

        if "mala" in radar_id and "amundsenisen-profile-2006" not in radar_id:
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

