#!/bin/bash

echo -e "Hello! this is a shell script to help you get microsoft fonts straight from a Windows 10 ISO. \nThis can be used for any language."

[ "$EUID" -ne 0 ] && echo "Please run this script as root."
[ ! -x "$(command -v 7z)" ] && echo "You need 7z installed in order for the scipt to run"

echo enter iso file path:
read ISOPATH

7z e ${ISOPATH} sources/install.wim
7z e install.wim 1/Windows/{Fonts/"*".{ttf,ttc},System32/Licenses/neutral/"*"/"*"/license.rtf} -ofonts/
cp fonts/* /usr/share/fonts/TTF

rm -rf fonts/ install.wim
