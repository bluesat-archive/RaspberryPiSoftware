#!/bin/bash
sudo rtl_fm -f $1 -M fm -s 260k -r 22050 -g 15 | multimon-ng -t raw /dev/stdin -a DTMF 
# >(aplay -r 22050 -f S16_LE -c 1 -q -V mono -D sysdefault:CARD=ALSA) 
#| multimon -t raw /dev/stdin -a DTMF
# | python killCommand1.py
