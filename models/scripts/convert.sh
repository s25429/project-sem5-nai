#!/bin/bash

# Check if the notebook name is provided
if [ -z "$1" ]; then
    echo "Please provide the notebook filename as an argument."
    exit 1
fi

# Get the notebook name from the command line argument
notebook_name="$1"

jupyter nbconvert --to=python --TagRemovePreprocessor.remove_input_tags='{"remove_input"}' "$notebook_name" --output "raw/${notebook_name%.ipynb}.py"

echo "Conversion complete: $notebook_name -> raw/${notebook_name%.ipynb}.py"