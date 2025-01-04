#!/bin/bash
#                _ _
# __      ____ _| | |_ __   __ _ _ __   ___ _ __
# \ \ /\ / / _` | | | '_ \ / _` | '_ \ / _ \ '__|
#  \ V  V / (_| | | | |_) | (_| | |_) |  __/ |
#   \_/\_/ \__,_|_|_| .__/ \__,_| .__/ \___|_|
#                   |_|         |_|
#
# -----------------------------------------------------
# Check to use wallpaper cache
# -----------------------------------------------------

# Leer la configuración de Waypaper para obtener la ruta del wallpaper actual
WAYPAPER_CONFIG="$HOME/.config/waypaper/config.ini"
WALLPAPER=$(grep '^wallpaper =' "$WAYPAPER_CONFIG" | cut -d'=' -f2 | xargs)
CACHE_DIR="$HOME/.cache/wallpapers"

# Create the cache directory if it doesn't exist
mkdir -p "$CACHE_DIR"

# Expandir la ruta
WALLPAPER=$(eval echo $WALLPAPER)
wal -i "$WALLPAPER" -q

# Copy the current wallpaper to the cache directory
CACHE_CURRENT_WALLPAPER="$CACHE_DIR/current_wallpaper.png"
magick "$WALLPAPER" "$CACHE_CURRENT_WALLPAPER"
echo ":: Current wallpaper copied to cache: $CACHE_CURRENT_WALLPAPER"
