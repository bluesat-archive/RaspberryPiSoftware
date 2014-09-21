#!/bin/bash
#while [ 1 ]; do
#    multimonout=$(sudo multimon -a DTMF -t raw ./soundfifo.raw)
#    echo $multimonout
#done
sudo multimon -a DTMF -t raw ./soundfifo.raw #> multimon.log


 # >  sudo ./killcommandtest.py
# sudo  python ./killcommandtest.py
#lets you open the pipe in multimon. This has to run at the same
#time as SDRPiping.sh
