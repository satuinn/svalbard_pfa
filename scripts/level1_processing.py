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


        # AUSTFONNA 2004
        r"\Austfonna\2004\Level0_COP_Malå_800MHz\120-13": "austfonna-profile-2004-800MHz-mala-01",
        r"\Austfonna\2004\Level0_COP_Malå_800MHz\120-131": "austfonna-profile-2004-800MHz-mala-02",
        r"\Austfonna\2004\Level0_COP_Malå_800MHz\vest4": "austfonna-profile-2004-800MHz-mala-03",
        r"\Austfonna\2004\Level0_COP_Malå_800MHz\vest9": "austfonna-profile-2004-800MHz-mala-04",

        # AUSTFONNA 2005
        r"\Austfonna\2005\Level0_COP_Malå_800MHz\asf2304-2": "austfonna-profile-2005-800MHz-mala-01",
        r"\Austfonna\2005\Level0_COP_Malå_800MHz\asf2404-2": "austfonna-profile-2005-800MHz-mala-02",
        r"\Austfonna\2005\Level0_COP_Malå_800MHz\asf23041": "austfonna-profile-2005-800MHz-mala-03",

        # AUSTFONNA 2006
        r"\Austfonna\2006\Level0_COP_Malå_800MHz\Profile3_030506": "austfonna-profile-2006-800MHz-mala-01",
        r"\Austfonna\2006\Level0_COP_Malå_800MHz\Profile13_020506": "austfonna-profile-2006-800MHz-mala-02",
        r"\Austfonna\2006\Level0_COP_Malå_800MHz\Profile14_020506": "austfonna-profile-2006-800MHz-mala-03",
        r"\Austfonna\2006\Level0_COP_Malå_800MHz\Profile15_020506": "austfonna-profile-2006-800MHz-mala-04",

        #AUSTFONNA 2007:
        r"\Austfonna\2007\Level0_COP_Malå_800MHz\2204-3": "austfonna-profile-2007-800MHz-mala-01",
        r"\Austfonna\2007\Level0_COP_Malå_800MHz\2204-15": "austfonna-profile-2007-800MHz-mala-02",
        r"\Austfonna\2007\Level0_COP_Malå_800MHz\2504-2": "austfonna-profile-2007-800MHz-mala-03",
        r"\Austfonna\2007\Level0_COP_Malå_800MHz\2504-3": "austfonna-profile-2007-800MHz-mala-04",
        r"\Austfonna\2007\Level0_COP_Malå_800MHz\3004-120-2": "austfonna-profile-2007-800MHz-mala-05",


        #AUSTFONNA 2008:
        r"\Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-2": "austfonna-profile-2008-800MHz-mala-01",
        r"\Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-21": "austfonna-profile-2008-800MHz-mala-02",
        r"\Austfonna\2008\Level0_COP_Malå_800MHz\2504-08-111-a-1": "austfonna-profile-2008-800MHz-mala-03",
        r"\Austfonna\2008\Level0_COP_Malå_800MHz\duv-ned1_3004-08": "austfonna-profile-2008-800MHz-mala-04",
        r"\Austfonna\2008\Level0_COP_Malå_800MHz\p111_b08_nw1_0205-08": "austfonna-profile-2008-800MHz-mala-05",
        r"\Austfonna\2008\Level0_COP_Malå_800MHz\p120-n4_2704-08": "austfonna-profile-2008-800MHz-mala-06",
        r"\Austfonna\2008\Level0_COP_Malå_800MHz\p120-n5_2704-08": "austfonna-profile-2008-800MHz-mala-07",

        #AUSTFONNA 2009:
        r"\Austfonna\2009\Level0_COP_Malå_800MHz\eton2_3004-09": "austfonna-profile-2009-800MHz-mala-01",
        r"\Austfonna\2009\Level0_COP_Malå_800MHz\nv2_2904-09": "austfonna-profile-2009-800MHz-mala-02",
        r"\Austfonna\2009\Level0_COP_Malå_800MHz\nv3_2904-09": "austfonna-profile-2009-800MHz-mala-03",
        r"\Austfonna\2009\Level0_COP_Malå_800MHz\nv5-invers_2904-09": "austfonna-profile-2009-800MHz-mala-04",

        #AUSTFONNA 2010:
        r"\Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0012_A1_0505-10": "austfonna-profile-2010-800MHz-mala-01",
        r"\Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0041_A1_2504-10": "austfonna-profile-2010-800MHz-mala-02",
        r"\Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0042_A1_2504-10": "austfonna-profile-2010-800MHz-mala-03",
        r"\Austfonna\2010\Level0_COP_Malå_800MHz\DAT_0043_A1_2504-10": "austfonna-profile-2010-800MHz-mala-04",

        #AUSTFONNA 2011:
        r"\Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_0305-11": "austfonna-profile-2011-800MHz-mala-01",  
        r"\Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0002_A1_0105-11": "austfonna-profile-2011-800MHz-mala-02", 
        r"\Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0003_A1_1105-11": "austfonna-profile-2011-800MHz-mala-03", 
        r"\Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0009_A1_0705-11": "austfonna-profile-2011-800MHz-mala-04",
        r"\Austfonna\2011\Level0_COP_Malå_800MHz\DAT_0017_A1_0405-11": "austfonna-profile-2011-800MHz-mala-05",

        # AUSTFONNA 2012
        r"\Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0011_A1": "austfonna-profile-2012-800MHz-mala-01", 
        r"\Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0012_A1": "austfonna-profile-2012-800MHz-mala-02",
        r"\Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0017_A1": "austfonna-profile-2012-800MHz-mala-03",
        r"\Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0023_A1": "austfonna-profile-2012-800MHz-mala-04",
        r"\Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0024_A1": "austfonna-profile-2012-800MHz-mala-05",
        r"\Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0035_A1": "austfonna-profile-2012-800MHz-mala-06",
        r"\Austfonna\2012\Level0_COP_Malå_800MHz\DAT_0042_A1": "austfonna-profile-2012-800MHz-mala-07",


        # AUSTFONNA 2013
        r"\Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0007_A1": "austfonna-profile-2013-800MHz-mala-01", 
        r"\Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0032_A1": "austfonna-profile-2013-800MHz-mala-02", 
        r"\Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0044_A1": "austfonna-profile-2013-800MHz-mala-03",
        r"\Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0045_A1": "austfonna-profile-2013-800MHz-mala-04",
        r"\Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0047_A1": "austfonna-profile-2013-800MHz-mala-05",
        r"\Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0066_A1": "austfonna-profile-2013-800MHz-mala-06",
        r"\Austfonna\2013\Level0_COP_Malå_800MHz\DAT_0069_A1": "austfonna-profile-2013-800MHz-mala-07",

        # AUSTFONNA 2014
        r"\Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0172_A1": "austfonna-profile-2014-800MHz-mala-01", 
        r"\Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0173_A1": "austfonna-profile-2014-800MHz-mala-02", 
        r"\Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0175_A1": "austfonna-profile-2014-800MHz-mala-03", 
        r"\Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0186_A1": "austfonna-profile-2014-800MHz-mala-04",
        r"\Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0198_A1": "austfonna-profile-2014-800MHz-mala-05",
        r"\Austfonna\2014\Level0_COP_Malå_800MHz\DAT_0199_A1": "austfonna-profile-2014-800MHz-mala-06",

        # AUSTFONNA 2015
        r"\Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0001_A1-NW_Helvete": "austfonna-profile-2015-800MHz-mala-01", 
        r"\Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0002_A1-NW_Helvete": "austfonna-profile-2015-800MHz-mala-02",
        r"\Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0004_A1-NW_Helvete": "austfonna-profile-2015-800MHz-mala-03",
        r"\Austfonna\2015\Level0_COP_Malå_800MHz\DAT_0006_A1-150430_Eton": "austfonna-profile-2015-800MHz-mala-04",




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

