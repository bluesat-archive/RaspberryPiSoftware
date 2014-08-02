#!/bin/bash
sudo rtl_fm -f $1 -M fm -s260k -r 22050 -g 50 | multimon -t raw /dev/stdin -a DTMF | python killCommand1.py
