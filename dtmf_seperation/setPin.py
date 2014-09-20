#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BOARD) # PINS ARE LABALLED ACCORDING TO THE STUFF ON THE BOARD. NO MORE CONFUSIOn


#the command line argument is in the form fo "pinnumber pinstate"

EjectPin = int(sys.argv[1])
Pinstate =  int(sys.argv[2])

if (Pinstate == 0):
	Pinstate = False
else:
	Pinstate = True

if EjectPin > 30 :
	print "invalid pinnumber"

#configuring eject pin
GPIO.setup(EjectPin, GPIO.OUT);

GPIO.output(EjectPin, Pinstate);
