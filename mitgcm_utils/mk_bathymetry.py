
import argparse
from pathlib import Path

import xarray as xr 
import xesmf as xe

import numpy as np
import matplotlib.pyplot as plt
import f90nml
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.colors as mcolors

def plot_bathy(lat, lon, z):
    ax = plt.axes(projection=ccrs.PlateCarree())
    levels = list(np.linspace(-3000,-200,10))[:-1] + list(np.linspace(-200,0,21))
    levels = [ -0.0000001 if item == 0.0 else item for item in levels ]

    cmap=plt.cm.jet
    norm = mcolors.BoundaryNorm(boundaries=levels, ncolors=cmap.N)

    cs=ax.contourf(lon,lat,z,levels=levels,cmap=cmap,norm=norm,transform=ccrs.PlateCarree(),extend='max')
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False

    plt.colorbar(cs)

    plt.savefig('bathymetry.png')


parser = argparse.ArgumentParser()

parser.add_argument(
    "--wrf_geo", 
    help="Path of WRF geo_em file", 
    required=True
    )
parser.add_argument(
    "--input_bathy", 
    help="Path input bathymetry file",
    required=True
    )

args = parser.parse_args()

wrf_geo=Path(args.wrf_geo)
input_bathy=Path(args.input_bathy)

ds_geo = xr.open_dataset(wrf_geo)
ds_input_bathy = xr.open_dataset(input_bathy)
input_bathy = ds_input_bathy['z']

XLAT_M = ds_geo['XLAT_M'][0,:,0]
XLONG_M = ds_geo['XLONG_M'][0,0,:]

print(XLAT_M.values)
print(XLONG_M.values)

grid_out = xr.Dataset(
    {
        "lat": (["lat"], XLAT_M.values, {"units": "degrees_north"}),
        "lon": (["lon"], XLONG_M.values, {"units": "degrees_east"}),
    }
)
regridder = xe.Regridder(ds_input_bathy, grid_out, "conservative")

dr_out = regridder(input_bathy, keep_attrs=True)

plot_bathy(XLAT_M, XLONG_M, dr_out)


