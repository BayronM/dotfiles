import os
import socket

from libqtile import qtile
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration

import subprocess

MY_TERM = "alacritty"
spawn_nvidia_GPU_utilization = (
    "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits"
)


colors = [
    ["#282c34", "#282c34"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#0563b5", "#0563b5"],
    ["#46d9ff", "#46d9ff"],
    ["#ffffff", "#ffffff"],
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

font_defaults = dict(
    font="ShureTechMono Nerd Font Bold",
    fontsize=13,
)
font_defaults = font_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration(
            radius=4,
            filled=True,
            padding_y=3,
            group=True,
            line_color="#07f537",
            line_width=2,
        )
    ],
    "padding": 5,
}

decoration_layout = {
    "decorations": [
        RectDecoration(colour="#004040", radius=4, filled=True, padding_y=4, group=True)
    ],
    "padding": 1,
}


def widgets_list_center():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.Image(
            filename="~/.config/qtile/img/arch_logo.png",
            scale=True,
            mouse_callbacks={"Button1": lazy.spawn("oblogout")},
            background=colors[0],
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            margin_y=3,
            margin_x=1,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=True,
            fontshadow=colors[0],
            highlight_color=colors[1],
            highlight_method="block",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
            **font_defaults,
        ),
        widget.TextBox(
            text="|",
            background=colors[0],
            foreground="#474747",
            **font_defaults,
        ),
        widget.CurrentLayoutIcon(
            foreground=colors[2],
            background=colors[0],
            scale=0.5,
            **decoration_layout,
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[0],
            **font_defaults,
            **decoration_layout,
        ),
        widget.TextBox(
            text="|",
            background=colors[0],
            foreground="#474747",
            **font_defaults,
        ),
        widget.WindowName(
            foreground=colors[6], background=colors[0], padding=0, **font_defaults
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.Systray(background=colors[0], **font_defaults),
        widget.KeyboardLayout(
            background=colors[0],
            **font_defaults,
            configured_keyboards=["us", "latam"],
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.CPU(
            background=colors[0],
            **font_defaults,
            **decoration_group,
        ),
        widget.ThermalSensor(
            **font_defaults,
            **decoration_group,
            background=colors[0],
            tag_sensor="Package id 0",
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.NvidiaSensors(
            format="GPU {temp}°C",
            background=colors[0],
            **font_defaults,
            **decoration_group,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    MY_TERM + " -e watch -n 1 nvidia-smi"
                )
            },
        ),
        widget.GenPollText(
            func=lambda: subprocess.check_output(
                spawn_nvidia_GPU_utilization, shell=True
            )
            .decode("utf-8")
            .splitlines()[0]
            + "%",
            update_interval=5,
            background=colors[0],
            **font_defaults,
            **decoration_group,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    MY_TERM + " -e watch -n 1 nvidia-smi"
                )
            },
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.Memory(
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(MY_TERM + " -e btop")},
            format="RAM {MemUsed: .0f} MB/{MemTotal: .0f} MB",
            background=colors[0],
            **font_defaults,
            **decoration_group,
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.Clock(
            format="%B %d - %H:%M ",
            background=colors[0],
            **font_defaults,
            **decoration_group,
        ),
    ]
    return widgets_list


def widgets_left_right():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(MY_TERM)},
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="block",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=colors[0],
            foreground="#474747",
            padding=2,
            fontsize=14,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.7,
        ),
        widget.CurrentLayout(foreground=colors[2], background=colors[0], padding=5),
        widget.TextBox(
            text="|",
            background=colors[0],
            foreground="#474747",
            padding=2,
            fontsize=14,
        ),
        widget.WindowName(foreground=colors[6], background=colors[0], padding=0),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.Mpris2(scroll_chars=30, background=colors[0]),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="Updates: {updates} ",
            foreground=colors[5],
            colour_have_updates=colors[5],
            colour_no_updates=colors[5],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(MY_TERM + " -e sudo pacman -Syu")
            },
            padding=5,
            background=colors[0],
            decorations=[
                BorderDecoration(
                    colour=colors[5],
                    border_width=[0, 0, 2, 0],
                    padding_x=5,
                    padding_y=None,
                )
            ],
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.Pomodoro(background=colors[0]),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.Clock(
            foreground="#ffffff",
            background=colors[0],
            format="%A, %B %d - %H:%M ",
            decorations=[
                BorderDecoration(
                    colour="#ffffff",
                    border_width=[0, 0, 2, 0],
                    padding_x=5,
                    padding_y=None,
                )
            ],
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
    ]
    return widgets_list
