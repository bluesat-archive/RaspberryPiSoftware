#!/bin/bash
sudo minicom -b 115200 -D /dev/ttyUSB0 -C /home/data1.txt
echo "Logging"
