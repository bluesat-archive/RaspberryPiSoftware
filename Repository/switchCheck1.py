# 19Apr14
# A program to test switch input

import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

import time

switch = 2

GPIO.setup(switch, GPIO.IN)

while True:
    if (not GPIO.input(switch)):
        print "BOOM\n"
      
    else:
        print "Why hasn't the bank blown up yet\n"
    time.sleep(0.1)

