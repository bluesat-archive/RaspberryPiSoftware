#!/bin/sh

cd /home/pi/balloon_launch


cd dtmf_seperation 
./manager &

cd ../therm_pow_logging
sudo python timlemetry.py &




#cd ..
#namuru/namuruLog.sh

