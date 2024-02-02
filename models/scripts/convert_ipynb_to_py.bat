@echo off

if not exist raw mkdir raw

rem Iterate through all .ipynb files in the current directory
for %%i in (*.ipynb) do (
    rem Get the notebook name without extension
    set "notebook_name=%%~ni"

    jupyter nbconvert --to=python "%%i" --output "raw\!notebook_name!.py"

    echo %%i -> raw\!notebook_name!.py
)