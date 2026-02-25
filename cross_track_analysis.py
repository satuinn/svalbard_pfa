import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial

from pathlib import Path

def cross_track(
        old_fp: Path = Path(r"C:\Users\satuki\svalbard_pfa\picks\all_picks_amu2006.geojson"), 
        new_fp: Path = Path(r"C:\Users\satuki\svalbard_pfa\picks\amu2025\all_picks_amu2025.geojson"),
        unit: str = "m"):
    
    if unit == "m":
        col = "pfa_depth"
    elif unit == "ns":
        col = "pfa_twt"
        

    old = gpd.read_file(old_fp)
    old["pfa_twt"] = old["return-time"]
    old["pfa_depth"] = old["pfa_twt"] * 0.19 / 2

    new = gpd.read_file(new_fp)

    tree = scipy.spatial.KDTree(
        np.transpose([old.geometry.x, old.geometry.y])
    )

    distances, indices = tree.query(new[["easting", "northing"]])

    distance_mask = distances < 65 # 50

    intersections = new[distance_mask].rename(columns={col: f"new_{col}"})

    intersections[f"old_{col}"] = old[col].values[indices[distance_mask]]

    intersections[f"{col}_diff"] = intersections[f"old_{col}"] - intersections[f"new_{col}"]

    intersections.to_file("PFA_AMU_differences_65.geojson")

    fig = plt.figure()

    axes = fig.subplots(2, 1, sharex=True, height_ratios=[0.2, 0.8])

    if unit == "ns":
        bins = np.linspace(-20, 80, 50)
    elif unit == "m":
        bins = np.linspace(-2, 8, 50)

    
    axes[0].hist(intersections[f"{col}_diff"], bins=bins)

    elevation = intersections["altitude"] + 30

    points = axes[1].scatter(intersections[f"{col}_diff"], elevation, edgecolors="none", s=7, c=intersections[f"new_{col}"])
    inset = axes[1].inset_axes([0.6, 0.5, 0.3, 0.4])
    inset.set_axis_off()
    cbar = plt.colorbar(mappable=points,ax=inset, aspect=10)
    if unit == "ns":
        cbar.set_label("Modern TWT (ns)")
        axes[1].set_xlabel("TWT difference (ns)")
    elif unit == "m":
        cbar.set_label("Depth in 2025 (m)")
        axes[1].set_xlabel("Depth difference (m)")
    axes[1].set_ylabel("Elevation (m)")
    plt.tight_layout()
    plt.savefig("cross_track_analysis_65.jpeg", dpi=400)
    plt.show()
    
    return
    
    plt.show()
    

    print(new)

if __name__ == "__main__":
    cross_track()