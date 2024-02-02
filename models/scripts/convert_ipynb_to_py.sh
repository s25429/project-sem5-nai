#!/bin/bash

mkdir -p raw

# Iterate through all .ipynb files in the current directory
for notebook in *.ipynb; do
    # Get the notebook name without extension
    notebook_name="${notebook%.ipynb}"

    jupyter nbconvert --to=python "$notebook" --output "raw/${notebook_name}.py"

    echo "$notebook -> raw/${notebook_name}.py"
done
