# Setting Up a Geospatial Python Environment with Conda

## **1. Install Anaconda**
Download and install **Anaconda** from [https://www.anaconda.com/](https://www.anaconda.com/).

## **2. Open the Terminal on Base (core)**
Ensure you start from the **base** environment before creating a new one.

## **3. Create a New Environment**
```bash
conda create -n geo_env python=3.10 gdal numpy pip setuptools -c conda-forge
```
🔹 **Note:** Check **GDAL** compatibility before installing:
```bash
conda search gdal -c conda-forge
```
This will list all available GDAL versions and compatible Python versions.

## **4. Test the Environment and Installed Versions**
```bash
conda activate geo_env
python --version  # Check installed Python version
# Expected output: Python 3.10.x

gdalinfo --version  # Check GDAL version
# Expected output: GDAL 3.10.x

python -c "from osgeo import gdal; print(gdal.VersionInfo())"
# Expected output: 3100200 (version code)
```

## **5. Configure Conda for Prioritized Forge Channel**
```bash
conda config --add channels conda-forge
conda config --env --set channel_priority strict
```

## **6. Install GeoPandas and Dependencies**
```bash
conda install geopandas gdal -c conda-forge
```
🔹 **Key Installed Packages:**
- **GeoPandas** (`geopandas-1.0.1`)
- **Pandas** (`pandas-2.2.3`)
- **Shapely** (`shapely-2.0.7`)
- **Pyproj** (`pyproj-3.7.1`)
- **Matplotlib** (`matplotlib-base-3.10.1`)
- **Folium** (`folium-0.19.5`)
- **Pyogrio** (`pyogrio-0.10.0`)

## **7. Test GeoPandas Installation**
```bash
python -c "import geopandas as gpd; print(gpd.__version__)"
```
Expected output: `1.0.1`

## **8. Install Raster Handling Packages**
```bash
conda install rasterstats rasterio netcdf4 xarray fiona -c conda-forge
```

## **9. Test Xarray Version**
```bash
python -c "import xarray as xr; print(xr.__version__)"
```
Expected output: `2025.3.0`

## **10. Install Interactive Python Environment (Jupyter & IPython)**
```bash
conda install jupyter ipython -c conda-forge
```

## **11. Link Conda Environment to Jupyter Notebook**
```bash
conda install ipykernel
python -m ipykernel install --user --name geo_env --display-name "Python (geo_env)"
```

## **12. Manage Jupyter Kernels**
List installed kernels:
```bash
jupyter kernelspec list
```
Uninstall a kernel (if needed):
```bash
jupyter kernelspec uninstall <kernel-name>
```

## **13. Supporting Packages for Visualization & Computation**
```bash
conda install seaborn matplotlib contextily dask -c conda-forge
```
🔹 **Optional Add-ons:**
- **rtree** – Improves spatial indexing for GeoPandas.
- **pyarrow** – Optimized file format support (Parquet & Feather).
- **hvplot** – Interactive plotting.
```bash
conda install rtree pyarrow hvplot -c conda-forge
```

## **14. Notes & Troubleshooting**
- Ensure the **batch file** (if used) points to the correct Conda environment - see the included activate.bat file as an example, as well as the notebook for testing the functionality of the installed packages.
- Even if Jupyter allows switching kernels, package paths are loaded from the starting environment, which can cause issues with:
  - `geopandas`, `pyproj`
  - `rasterio`, `gdal`
- To check if a package (e.g., `contextily`) is installed:
```bash
conda list contextily
python -c "import contextily; print(contextily.__version__)"
