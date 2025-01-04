#!/bin/bash
dunst &
nitrogen --restore & # For wallpapers
picom &              # For transparency
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &  # Graphical authentication agent
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &
