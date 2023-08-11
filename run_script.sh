#!/bin/bash

# Read folder paths from folder_paths.txt
IFS=$'\n' read -d '' -r -a folder_paths < folder_paths.txt

# Loop through the folder paths and run the Python script for each folder
for folder_path in "${folder_paths[@]}"; do
    echo "Processing folder: $folder_path"
    output_csv="average_spectrogram_$(basename "$folder_path").csv"
    python your_python_script.py --folder "$folder_path" --output "$output_csv"
done
