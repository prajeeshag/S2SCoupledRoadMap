import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

ds = xr.open_dataset("geo_em.d01.nc")

islake = ds.attrs["ISLAKE"]
iswater = ds.attrs["ISWATER"]

lulc = ds["LU_INDEX"]

lake = lulc.copy()
water = lulc.copy()

lake.values[lake.values != islake] = np.nan

water.values[water.values != iswater] = np.nan

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 10))

lake.plot(ax=ax[0])
water.plot(ax=ax[1])

plt.savefig("lake_water.png")
