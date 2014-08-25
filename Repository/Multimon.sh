#!/bin/bash
sudo multimon -a DTMF -a SCOPE -t raw ./soundfifo.raw
#lets you open the pipe in multimon. This has to run at the same
#time as SDRPiping.sh
