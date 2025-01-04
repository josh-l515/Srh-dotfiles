#!/bin/bash

# Directory where wallpapers are stored
WALLPAPER_DIR="$HOME/Pictures/wallpapers"
CACHE_DIR="$HOME/.cache/wallpapers"

# Create the cache directory if it doesn't exist
mkdir -p "$CACHE_DIR"

# Select a random wallpaper
DIR_CONTENTS=("$WALLPAPER_DIR"/*)
RANDOM_WALLPAPER="${DIR_CONTENTS[RANDOM % ${#DIR_CONTENTS[@]}]}"
echo ":: Selected wallpaper: $RANDOM_WALLPAPER"

# Change wallpaper using swww
swww img "$RANDOM_WALLPAPER" --transition-fps 30 --transition-type any --transition-duration 2

# Generate Pywal colorscheme
wal -i "$RANDOM_WALLPAPER" -q

# Store current wallpaper in cache directory
CURRENT_WALLPAPER=$(cat "$HOME/.cache/wal/wal")
echo ":: Path of current wallpaper from wal: $CURRENT_WALLPAPER"

# Copy the current wallpaper to the cache directory
CACHE_CURRENT_WALLPAPER="$CACHE_DIR/current_wallpaper.png"
magick "$CURRENT_WALLPAPER" "$CACHE_CURRENT_WALLPAPER"
echo ":: Current wallpaper copied to cache: $CACHE_CURRENT_WALLPAPER"

# Crop the wallpaper to a square size of 600x600
CROPPED_WALLPAPER="$CACHE_DIR/current_wallpaper_cropped.png"
magick "$CURRENT_WALLPAPER" -gravity center -crop 600x600+0+0 +repage "$CROPPED_WALLPAPER"
echo ":: Cropped wallpaper created: $CROPPED_WALLPAPER"

# Create a blurred version of the wallpaper
BLURRED_WALLPAPER="$CACHE_DIR/blurred_wallpaper.png"
BLUR="20x10" # Adjust the blur strength as needed
magick "$CROPPED_WALLPAPER" -blur "$BLUR" "$BLURRED_WALLPAPER"
echo ":: Blurred wallpaper created: $BLURRED_WALLPAPER"

# Update Rofi .rasi file
ROFI_RASI_FILE="$CACHE_DIR/current-wallpaper.rasi"
echo "* { current-wallpaper: url('$BLURRED_WALLPAPER'); }" >"$ROFI_RASI_FILE"
echo ":: Rofi .rasi file content:"
cat "$ROFI_RASI_FILE"
echo ":: Rofi .rasi file created: $ROFI_RASI_FILE"

# Check if the .rasi file was created successfully
if [ -f "$ROFI_RASI_FILE" ]; then
  echo ":: Verified: $ROFI_RASI_FILE exists."
else
  echo ":: Error: $ROFI_RASI_FILE was not created."
fi

# Clean up old wallpapers in cache directory (keep the latest one)
ls -t "$CACHE_DIR" | grep -v "$(basename "$CACHE_CURRENT_WALLPAPER")" | grep -v "$(basename "$CROPPED_WALLPAPER")" | grep -v "$(basename "$BLURRED_WALLPAPER")" | grep -v "$(basename "$ROFI_RASI_FILE")" | xargs -I {} rm "$CACHE_DIR"/{} || true
echo ":: Old wallpapers cleaned up."

echo "Wallpaper changed successfully and Pywal colorscheme generated."
