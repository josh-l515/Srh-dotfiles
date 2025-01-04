#!/bin/bash

# Check for updates and count the number of lines (packages needing updates)
updates=$(checkupdates 2>/dev/null | wc -l)

# If you use yay for AUR packages as well
aur_updates=$(yay -Qum 2>/dev/null | wc -l)

# Display the total number of updates (including AUR)
echo $((updates + aur_updates))
