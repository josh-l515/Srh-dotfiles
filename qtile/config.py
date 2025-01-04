# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess
import datetime
from libqtile import hook
from libqtile import bar, layout, qtile, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from pathlib import Path


mod = "mod4"
terminal = "kitty"
web_browser = 'microsoft-edge-stable'
file_manager = 'nemo'
rofi = "rofi -show drun"
# Get home path
home = str(Path.home())

Colors  = [
    ["#ffffff", "#ffffff"], # bg
    ["#f8f8f2", "#f8f8f2"], # fg
    ["#000000", "#000000"], # black
    ["#0b9b4e", "#0b9b4e"], # green1
    ["#087329", "#087329"], # shadowgree1
    ["#f1fa8c", "#f1fa8c"], # color04
    ["#bd93f9", "#bd93f9"], # color05
    ["#ff79c6", "#ff79c6"], # color06
    ["#28ee8e", "#18ee8e"], # color07
    ["#0000007c", "#0000007c"]  # color15
    ]
Fonts = [
    "FiraCode Nerd Font",       # Fuente 0
    "Iosevka Nerd Font",        # Fuente 1
    "Terminess Nerd Font",      # Fuente 2 
    "Hack Nerd Font",           # Fuente 3
]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    #General
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(web_browser), desc="Launch Web Browser"),
    # Key([mod], "r", lazy.spawn(os.path.expanduser('~/.config/rofi/launchers/type-3/launcher.sh')), desc="Launch rofi menu"),
    #dmenu integration
    Key([mod], 'r', lazy.run_extension(extension.DmenuRun())),
    Key(["shift", mod], "s", lazy.spawn(os.path.expanduser('~/.config/Srh5/scripts/flameshot.sh')), desc="Launch screenshot on x11"),
    Key([mod, "shift"],"Return", lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch nautilus file managermm"),
    Key([mod], "g", lazy.spawn("microsoft-edge-stable --app=https://chatgpt.com/"), desc="Launch chatgpt"),

    Key([mod], "w", lazy.spawn("microsoft-edge-stable --app=https://web.whatsapp.com/"), desc="Launch whatsapp"),
    Key([mod], "y", lazy.spawn("microsoft-edge-stable --app=https://www.youtube.com"), desc="Launch youtube"),    
    Key([mod], "j", lazy.spawn("microsoft-edge-stable --app=https://www.notion.so/"), desc="Launch youtube"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "v", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "x", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "s", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.spawn("betterlockscreen -l"), desc="betterlockscreen"),

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -q s +1%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -q s 1%-")),

    #Audio
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), desc="Mute/Unmute Volume"),   

    #Media
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),

]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = { 
    "border_width": 1,
    "margin": 3,
    "border_focus": "FFFFFF",
    "border_normal": "#424242",
    "single_border_width": 2,
}


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Floating()

]

widget_defaults = dict(
    # font=Fonts[0],
    fontsize=13,
    padding=0,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        # wallpaper='~/Pictures/b-015.jpeg',
        # wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.TextBox(
                    # background="#ffffff.4",
                    text="󰌠",
                    foreground="#ffffff",
                    fontsize=20,
                    padding=6,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(home+ "/.config/rofi/launchers/type-3/launcher.sh")},
                ),
                widget.TextBox(
                    text ='Josh 󰇙',
                    foreground = Colors[0],
                    padding=4,
                    fontsize=14,
                    mouse_callbacks={ "Button1": lambda: qtile.cmd_spawn("kitty -T 'Josh' --hold -e /home/joshl515/.config/Srh5/scripts/josh.sh")}
                ),
                widget.GroupBox(
                    margin_y = 5,
                    margin_x = 1,
                    padding_y = 0,
                    padding_x = 1,
                    borderwidth = 3,
                    active = Colors[6],
                    inactive = Colors[1],
                    highlight_color = Colors[9],
                    highlight_method = "line",
                    this_current_screen_border = Colors[6],
                    this_screen_border = Colors[0],
                ),
                widget.Spacer(length=4),
                widget.Image(
                    filename = "~/.config/Srh5/icons/ai-icon-20.png",
                    scale = "False",
                    margin =2,
                    padding = 2,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("brave --app=https://chat.openai.com")},
                ),
                widget.TextBox(
                    text=" ",
                    foreground="#ffffff",
                    margin=2,
                    padding=2,
                    fontsize=14,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(web_browser)}
                ),
                widget.TextBox(
                    text=" ",
                    foreground="#ffffff",
                    margin=2,
                    padding=2,
                    fontsize=14,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(file_manager)}
                ),
                widget.Prompt(),
                widget.Spacer(length=4),
                widget.WindowName(
                    # font=Fonts[0],
                    foreground = Colors[0],
                    max_chars = 80
                ),
                widget.Volume(
                    padding=2,
                    font=Fonts[1],
                    fmt='{}',
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")}
                ),
                widget.Memory(
                    padding=0,    
                    font=Fonts[1],
                    #foreground = Colors[8],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
                    # measure_mem='G',
                    fmt='{} ',

                ),
                widget.CPU(
                    padding=0,
                    font=Fonts[1],
                    format= '{freq_current}GHz {load_percent}%',
                    fmt = '{} ',
                ),
                widget.DF(
                    padding=0,
                    font=Fonts[1],
                    visible_on_warn=False,
                    format="{uf}{m} ({r:.0f}%)",
                    fmt = '{}  ',
                ),
                widget.Battery(
                    padding=0,
                    font=Fonts[1],
                    foreground=Colors[1],
                    format='{percent:2.0%}',
                    fmt='{} '
                ),
                widget.Wlan(
                    padding=0,
                    font=Fonts[1],
                    format='{essid}{percent:2.0%} ',
                    interface="wlo1",
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("nm-connection-editor")},
                ),
                widget.Systray(
                    padding=4,
                    icon_size=15,
                    # padding=4,
                ),
                # widget.TextBox(    
                #     text="",
                #     padding=5,
                #     fontsize=14,
                #     mouse_callbacks={
                #         "Button1": lambda: qtile.cmd_spawn(home + "/.config/scripts/redshift.sh"),
                #         "Button3": lambda: qtile.cmd_spawn(home + "/.config/scripts/redshift_off.sh")
                #     },
                # ),
                # widget.Image(
                #     filename = "~/.config/icons/ui.png",
                #     margin=3,
                #     margin_x=0,
                #     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(home + "/.config/scripts/flameshot.sh")},
                # ),
                widget.Image(
                    filename = "~/.config/Srh5/icons/color-picker-20.png",
                    margin =4,
                    margin_x=1,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn('gcolor3')},
                ),                
                widget.Image(
                    filename = "~/.config/Srh5/icons/ui-20.png",
                    margin=3,
                    margin_x=1,
                    mouse_callbacks={                    #
                        "Button1": lambda: qtile.cmd_spawn(home + "/.config/Srh5/scripts/redshift.sh"),
                        "Button3": lambda: qtile.cmd_spawn(home + "/.config/Srh5/scripts/redshift_off.sh")
                    },
                ),

                widget.Image(
                    filename = "~/.config/Srh5/icons/select-20.png",
                    margin=5,
                    margin_x=1,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(home + "/.config/Srh5/scripts/flameshot.sh")},
                ),
               widget.TextBox(    
                    text="󰸉",
                    padding=5,
                    fontsize=14,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("nitrogen")},
                ),
                widget.TextBox(    
                    text="󰐥",
                    padding=5,
                    fontsize=17,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("betterlockscreen -l")},
                ),
                widget.Spacer(length=2),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                #widget.StatusNotifier(),
                widget.CurrentLayout(
                    fmt='[{}]',
                    # font='Iosevka',
                    padding=2,
                    fontsize=14
                ),
                widget.Clock(
                    fontsize=15,
                    padding=0,
                    format="%I:%M %p",
                    # mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("brave --app=https://calendar.google.com")},
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("microsoft-edge-stable --app=https://calendar.google.com"),
                        "Button3": lazy.spawn("kitty -T 'Terminal-Calendar' --hold  -e cal")
                    },
                ),
                widget.Countdown(
                    padding=4,
                    font=Fonts[2],
                    fontsize=18,
                    date=datetime.datetime(2025, 1, 8, 22, 0, 0, 182727),
                    foreground = Colors[3],
                    fontshadow=Colors[8],
                    format='{D}•{H}•{M}•{S}',
                ),

            ],
            22,
            background="#0000007c",
            opacity=1,
            # border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False


floating_layout = layout.Floating(
    border_width=1,
    border_focus= "33ccffee",
    border_normal="FFFFFF",

    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="nm-connection-editor"),
        Match(wm_class="nwg-look"),
        Match(wm_class="Lxappearance"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="GParted"),
        Match(wm_class="Nitrogen"),
        Match(wm_class="Blueman-manager"),
        Match(wm_class="calendar.google.com"),
        Match(wm_class="Terminal-Calendar"),
        Match(wm_class="Josh"),
        Match(wm_class="fr.handbrake.ghb"),
        Match(wm_class="timeshift-gtk"),
        Match(wm_class="java"),
        Match(wm_class="qalculate-gtk"),
        Match(wm_class="virt-manager"),
        Match(wm_class="nl.hjdskes.gcolor3"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# HOOK startup
@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])

@hook.subscribe.client_new
def center_floating_win(window):
    wm_name = window.cmd_inspect()["name"]
    if wm_name == "Josh":
        window.toggle_floating()
        window.cmd_set_size_floating(800, 600)
        window.cmd_set_position_floating((1366 - 301) // 2, (768 - 227) // 2)


@hook.subscribe.client_new
def center_floating_brave(window):
    wm_class = window.window.get_wm_class()
    wm_name = window.cmd_inspect()["name"]

    # Check if the new window is Brave and the Google Calendar page
    if wm_class and "Microsoft-edge" in wm_class and "calendar.google.com" in wm_name:
        window.toggle_floating()  # Enable floating mode
        window.cmd_set_size_floating(900, 600)  # Set size (width=800, height=600)
        # Set position for a 1920x1080 screen, adjust as needed
        window.cmd_set_position_floating((1920 - 800) // 2, (1080 - 600) // 2)  # Centered


@hook.subscribe.client_new
def position_kitty_top_right(window):
    wm_class = window.window.get_wm_class()
    wm_name = window.cmd_inspect()["name"]

    # Check if it's the Kitty terminal with the specific title
    if wm_class and "kitty" in wm_class and wm_name == "Terminal-Calendar":
        window.toggle_floating()  # Make it float
        window.cmd_set_size_floating(301, 227)  # Set size to 800x600

        # Position the window in the top-right corner on a 1920x1080 screen
        window.cmd_set_position_floating(0, 0)  # Top-right corner















