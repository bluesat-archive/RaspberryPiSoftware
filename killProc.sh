#!/bin/sh

# Kills all the startup programs that have been invoked by master.sh


sudo pkill master.sh
sudo pkill manager
sudo pkill python

# Just in case

sudo pkill -9 rtl_fm
sudo pkill -9 signal_detect
sudo pkill -9 multimon_ng
