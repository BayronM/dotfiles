import os
import socket
import copy

from libqtile import qtile
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration
from qtile_extras.popup.templates.mpris2 import DEFAULT_LAYOUT
from qtile_extras.widget.groupbox2 import GroupBoxRule


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
    ["#636363", "#636363"],
    ["#46d9ff", "#46d9ff"],
    ["#ffffff", "#ffffff"],
]

color_palette = [
    "#577590",
    "#43aa8b",
    "#90be6d",
    "#f9c74f",
    "#f8961e",
    "#f9844a",
    "#f94144",
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

font_defaults = dict(
    font="ShureTechMono Nerd Font Bold",
    fontsize=13,
)
font_defaults = font_defaults.copy()
font_groupbox = font_defaults.copy()
font_groupbox["fontsize"] = 20
font_groupbox["font"] = "ShureTechMono Nerd Font"

decoration_defaults = {
    "decorations": [
        RectDecoration(
            radius=4,
            filled=True,
            padding_y=5,
            group=True,
        )
    ],
    "padding": 5,
}

decoration_cpu = copy.deepcopy(decoration_defaults)
decoration_cpu["decorations"][0].colour = color_palette[0]

decoration_gpu = copy.deepcopy(decoration_defaults)
decoration_gpu["decorations"][0].colour = color_palette[1]

decoration_memory = copy.deepcopy(decoration_defaults)
decoration_memory["decorations"][0].colour = color_palette[2]

decoration_clock = copy.deepcopy(decoration_defaults)
decoration_clock["decorations"][0].colour = colors[0]


background_default = dict(
    background=colors[0],
)


groupbox_rules = [
    GroupBoxRule(
        block_colour="#98be65",
        block_corner_radius=4,
        box_size=30,
    ).when(screen=GroupBoxRule.SCREEN_THIS),
    GroupBoxRule(block_colour="#118ab2", block_corner_radius=4, box_size=30).when(
        screen=GroupBoxRule.SCREEN_OTHER
    ),
    GroupBoxRule(text_colour="#ffffff").when(occupied=True),
    GroupBoxRule(text_colour="#363636").when(occupied=False),
]


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
        widget.GroupBox2(
            padding_x=6,
            **font_groupbox,
            background=colors[0],
            rules=groupbox_rules,
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.TaskList(
            background=colors[0],
            borderwidth=0,
            margin=3,
            padding=5,
            highlight_method="block",
            stretch=True,
            **font_defaults,
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.Mpris2(
            name="Youtube Music",
            objname="org.mpris.MediaPlayer2.YoutubeMusic",
            popup_layout=DEFAULT_LAYOUT,
            **font_defaults,
            background=colors[0],
            scroll=True,
            width=150,
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.Systray(background=colors[0], **font_defaults),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.KeyboardLayout(
            background=colors[0],
            **font_defaults,
            configured_keyboards=["us", "latam"],
            **decoration_defaults,
        ),
        widget.CurrentLayoutIcon(
            foreground=colors[2],
            background=colors[0],
            scale=0.5,
            **decoration_defaults,
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.CPU(
            background=colors[0],
            **font_defaults,
            **decoration_cpu,
        ),
        widget.ThermalSensor(
            **font_defaults,
            **decoration_cpu,
            background=colors[0],
            tag_sensor="Package id 0",
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.NvidiaSensors(
            format="GPU {temp}°C",
            background=colors[0],
            **font_defaults,
            **decoration_gpu,
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
            **decoration_gpu,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    MY_TERM + " -e watch -n 1 nvidia-smi"
                )
            },
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.Memory(
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(MY_TERM + " -e btop")},
            format=" {MemUsed: .00f} MB/{MemTotal: .0f} MB",
            background=colors[0],
            measure_mem="M",
            **font_defaults,
            **decoration_memory,
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.AnalogueClock(
            **font_defaults,
            **background_default,
            second_size=1,
            second_length=0.9,
            minute_length=0.9,
            adjust_y=-6,
            face_shape="circle",
            face_color=colors[0],
            margin=10,
        ),
        widget.Clock(
            format="%B %d - %H:%M ",
            **background_default,
            **font_defaults,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0],
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
            fontsize=15,
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
            **font_defaults,
            **decoration_clock,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0],
        ),
    ]
    return widgets_list
