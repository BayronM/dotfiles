# -*- coding: utf-8 -*-
import os
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
from qtile_bar import widgets_list_center, widgets_left_right

##layouts
from libqtile.layout import xmonad, stack, columns, max, zoomy


mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"  # terminal
myBrowser = "brave"  # browser


keys = [
    ### The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launches My Terminal"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn(
            "rofi -show drun -theme ~/.config/rofi/launchers/type-1/style-7.rasi"
        ),
        desc="Run Launcher",
    ),
    Key(["control", "shift"], "q", lazy.shutdown()),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill active window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key(
        ["control", "shift"],
        "e",
        lazy.spawn("emacsclient -c -a emacs"),
        desc="Doom Emacs",
    ),
    ### Switch focus to specific monitor (out of three)
    Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    Key([mod], "r", lazy.to_screen(2), desc="Keyboard focus to monitor 3"),
    # Screenshot bindings
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Screenshot"),
    # Keyboard layout
    Key(
        [mod],
        "i",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    ### Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    ### Treetab controls
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.move_left(),
        desc="Move up a section in treetab",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.move_right(),
        desc="Move down a section in treetab",
    ),
    ### Window controls
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"
    ),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="normalize window size ratios"),
    Key(
        [mod],
        "XF86AudioLowerVolume",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "XF86AudioRaiseVolume",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key(
        [mod],
        "XF86AudioMute",
        lazy.layout.normalize(),
        desc="normalize window size ratios",
    ),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    ### Stack controls
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # media keys
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 2%-"),
        desc="Lower Volume by 2%",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 2%+"),
        desc="Raise Volume by 2%",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer sset Master 1+ toggle"),
        desc="Mute/Unmute Volume",
    ),
    # Doom Emacs
    # Control + Shift + e to open Doom Emacs
    Key(
        ["control", "shift"],
        "e",
        lazy.spawn("emacsclient -c -a emacs"),
        desc="Doom Emacs",
    ),
    # open an doom emacs org file in a specific group
    # Control + Shift + o to open an org file in a specific group
    Key(
        ["control", "shift"],
        "o",
        lazy.spawn("emacsclient -c -a emacs ~/org/notes.org"),
        desc="Doom Emacs Org File",
    ),
]

groups = [
    Group("", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("", layout="monadtall"),
    Group("󰭹", layout="monadtall"),
    Group(
        "",
        layout="monadtall",
        matches=[
            Match(wm_class="Deezer"),
            Match(wm_class="Spotify"),
            Match(wm_class="youtube-music"),
        ],
    ),
    Group("󰎁", layout="monadtall"),
    Group("󰊢", layout="monadtall", persist=False),
]

dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "#43d902",
    "border_normal": "#1D2330",
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    stack.Stack(stacks=2, **layout_theme),
    columns.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    zoomy.Zoomy(**layout_theme),
    xmonad.MonadTall(**layout_theme),
    max.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(**layout_theme),
    # layout.Floating(**layout_theme),
]


def init_screens():
    return [
        Screen(
            top=bar.Bar(widgets=widgets_list_center(), opacity=0.85, size=32, margin=6)
        ),
        Screen(top=bar.Bar(widgets=widgets_left_right(), opacity=1.0, size=20)),
        Screen(top=bar.Bar(widgets=widgets_left_right(), opacity=1.0, size=20)),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = widgets_list_center()
    widgets_screen1 = widgets_left_right()
    widgets_screen2 = widgets_left_right()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


# open an app in a specific group
def spawn_app_in_group(app_name, group_name):
    lazy.spawn(app_name)
    lazy.window.togroup(group_name)


mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])
    spawn_app_in_group("emacscilent -c -a emacs ~/org/notes.org", "Org⁴")


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
