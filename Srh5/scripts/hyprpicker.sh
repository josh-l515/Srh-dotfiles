#!/bin/bash
color=$(hyprpicker --format hex | tr -d '\n')
echo -n $color | wl-copy
