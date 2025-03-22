REM # https://medium.com/@smallgateanalytics/jupyter-launch-button-2942cba6a7bd
REM # D:\GeoSpatial\anaconda3\envs\geo_project1 <conda info>

REM # set a new window:
REM # change the anaconda link for another link (user dependend)
set new_window="https://nb.anaconda.cloud/jupyterhub/user/ab7bb8b7-2cef-4699-98ae-2ecc7ccee791/lab?redirects=1"
REM set new_window="https://google.com"

call D:\GeoSpatial\anaconda3\Scripts\activate.bat
call activate geo_env_20250322

REM # A batch file to run Jupyter notebook  on the current folder 
cd E:\
cd E:\Projects\

start chrome --new-window "%new_window%"

call jupyter lab --notebook-dir="E:/Projects/"

pause