#!/bin/bash
echo "Logging"
sudo minicom -b 115200 -D /dev/ttyUSB0 -C /home/data6.txt
