#!/bin/bash

# Set the directory where you want to save the screenshots
SCREENSHOT_DIR="$HOME/Pictures/Screenshots"

# Ensure the directory exists
mkdir -p "$SCREENSHOT_DIR"

# Generate a timestamp for the screenshot filename
TIMESTAMP=$(date +'%Y-%m-%d_%H-%M-%S')

# Define the file path for the screenshot
FILE_PATH="$SCREENSHOT_DIR/screenshot_$TIMESTAMP.png"

# Use scrot to capture the selected area and save it
scrot -s "$FILE_PATH" && xclip -selection clipboard -t image/png <"$FILE_PATH"

# Notify the user
notify-send "Screenshot taken" "Saved to $FILE_PATH and copied to clipboard."
