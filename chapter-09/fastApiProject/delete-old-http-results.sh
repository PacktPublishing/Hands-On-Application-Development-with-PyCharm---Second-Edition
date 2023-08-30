#!/bin/bash

folder="$(pwd)"  # Make sure you set the working directory in the run config!

# Get all JSON files except the last 25
readarray -t filesToDelete < <(find "$folder" -type f -name "*.json" -printf '%T@ %p\n' | sort -n | head -n -5 | awk '{gsub(/^[^ ]+ /, ""); print}')

# Delete the files
for file in "${filesToDelete[@]}"; do
  rm "$file"
done
