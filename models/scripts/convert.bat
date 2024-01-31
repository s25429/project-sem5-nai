@echo off

rem Check if the notebook name is provided
if "%1" == "" (
    echo Please provide the notebook filename as an argument.
    exit /b 1
)

rem Get the notebook name from the command line argument
set "notebook_name=%1"

rem Convert the notebook to Python script
jupyter nbconvert --to=python --TagRemovePreprocessor.remove_input_tags='{"remove_input"}' "%notebook_name%.ipynb" --output "raw/%~dpn1.py"

echo Conversion complete: "%notebook_name%.ipynb" -> "raw/%~dpn1.py"