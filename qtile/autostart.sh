#!/bin/sh
feh --bg-scale ~/.config/img/fondo.jpg &
picom -b --backend glx --config ~/.config/picom/picom.conf &
flameshot &
/usr/bin/emacs --daemon &
