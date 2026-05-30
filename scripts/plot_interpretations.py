from pathlib import Path
import numpy as np
import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt



def plot_interpretations():

    interpretations_path = Path(r"C:\Users\satuki\Downloads\interpretations-20260226T134319.zip")
    gdf = gp.read_file(interpretations_path)

    twtt = "twtt"                 
    easting = "easting"              
    northing = "northing"             
    distance = "distance"            
    year = "year"                      
    kind = "firn_ice_interface" 

if __name__ == "__main__":
    plot_interpretations()

                    

# # AOI bounding box (bottom-left and upper-right corners)
# xmin, ymin = 666830, 8880154  # bottom-left
# xmax, ymax = 666923, 8880220  # upper-right


# # Plot settings
# invert_yaxis = True     # Common for radar/TWTT plots (increasing TWTT downward)
# point_size = 16
# point_alpha = 0.85
# cmap_name = "cividis"   # dark blue -> yellow, perceptually uniform
