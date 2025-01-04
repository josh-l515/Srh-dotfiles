#!/bin/bash
#  ____                               _           _
# / ___|  ___ _ __ ___  ___ _ __  ___| |__   ___ | |_
# \___ \ / __| '__/ _ \/ _ \ '_ \/ __| '_ \ / _ \| __|
#  ___) | (__| | |  __/  __/ | | \__ \ | | | (_) | |_
# |____/ \___|_|  \___|\___|_| |_|___/_| |_|\___/ \__|
#
#
# by Josh D. and chatGpt (2024)
# -----------------------------------------------------

# Set the directory where you want to save the screenshots
SCREENSHOT_DIR="$HOME/Pictures/Screenshots"

# Ensure the directory exists
mkdir -p "$SCREENSHOT_DIR"

# Generate a timestamp for the screenshot filename
TIMESTAMP=$(date +'%Y-%m-%d_%H-%M-%S')

# Define the file path for the screenshot
FILE_PATH="$SCREENSHOT_DIR/screenshot_$TIMESTAMP.png"

# Use grimblast to capture the selected area and copy it to the clipboard while saving it to a file
grimblast copysave area "$FILE_PATH" --notify

# Notify the user
notify-send "Screenshot taken" "Saved to $FILE_PATH and copied to clipboard."
