#!/bin/bash
#  ____                               _           _
# / ___|  ___ _ __ ___  ___ _ __  ___| |__   ___ | |_
# \___ \ / __| '__/ _ \/ _ \ '_ \/ __| '_ \ / _ \| __|
#  ___) | (__| | |  __/  __/ | | \__ \ | | | (_) | |_
# |____/ \___|_|  \___|\___|_| |_|___/_| |_|\___/ \__|
#
#
# by Josh and ChatGPT (2024)
# -----------------------------------------------------

# Define the save directory
SAVE_DIR="$HOME/Pictures/screenshots"
mkdir -p "$SAVE_DIR"

# Generate a timestamped filename
FILENAME="screenshot_$(date +%Y%m%d_%H%M%S).png"

# Take a screenshot of a selected area, save it, and copy it to the clipboard
flameshot gui -p "$SAVE_DIR/$FILENAME" &&
  xclip -selection clipboard -t image/png -i "$SAVE_DIR/$FILENAME"
