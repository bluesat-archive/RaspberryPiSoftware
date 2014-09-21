#!/bin/bash
echo "Starting Namuru Logger"
sudo minicom -b 115200 -D /dev/ttyUSB0 -C logs/namuru_$(date +%F_%H:%M:%S).log
echo "Namuru logger has stopped"
