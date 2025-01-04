#!/bin/sh
source ~/.cache/wal/colors.sh

# Mapping from hex colors to ncmpcpp color names
declare -A color_map=(
  ["#000000"]="black"
  ["#800000"]="maroon"
  ["#008000"]="green"
  ["#808000"]="olive"
  ["#000080"]="navy"
  ["#800080"]="purple"
  ["#008080"]="teal"
  ["#c0c0c0"]="silver"
  ["#808080"]="gray"
  ["#ff0000"]="red"
  ["#00ff00"]="lime"
  ["#ffff00"]="yellow"
  ["#0000ff"]="blue"
  ["#ff00ff"]="fuchsia"
  ["#00ffff"]="aqua"
  ["#ffffff"]="white"
  # Add more mappings if needed
)

hex_to_name() {
  local hex=$1
  echo ${color_map[$hex]:-default_color}
}

echo "
# ncmpcpp color configuration file
mpd_music_dir = \"~/Music/\"
visualizer_in_stereo = \"yes\"
visualizer_data_source = \"/tmp/mpd.fifo\"
visualizer_output_name = \"my_fifo\"
progressbar_look = \"━━╸\"
visualizer_type = \"spectrum\"
visualizer_look = \"◆▋\"
message_delay_time = \"3\"
playlist_shorten_total_times = \"yes\"
playlist_display_mode = \"columns\"
browser_display_mode = \"columns\"
search_engine_display_mode = \"columns\"
playlist_editor_display_mode = \"columns\"
autocenter_mode = \"yes\"
centered_cursor = \"yes\"
user_interface = \"alternative\"
follow_now_playing_lyrics = \"yes\"
locked_screen_width_part = \"60\"
display_bitrate = \"yes\"
external_editor = \"nano\"
use_console_editor = \"yes\"
header_window_color = $(hex_to_name ${color1})
volume_color = $(hex_to_name ${color2})
state_line_color = $(hex_to_name ${color3})
state_flags_color = $(hex_to_name ${color4})
progressbar_color = $(hex_to_name ${color5})
statusbar_color = $(hex_to_name ${color6})
visualizer_color = $(hex_to_name ${color7})
mpd_host = \"127.0.0.1\"
mpd_port = \"6601\"
mouse_list
