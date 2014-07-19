#!usr/bin/python
# Make like a while(true) loop to
# read in stuff from Stdin (NEED TO KNOW FORMAT)
# Scratch most of this.
# Make a list of DTMF outputs to check against
# Check input against that
# Roll pin control into a function
# Call function that deals with error checking. (LATER)
# For now make an abort function "abort" when it receives expIn
# Jesus Take the Wheel!


import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

expIn = [1,2,9,5,1,2,9,5] #this is Jim's Birthday
oldIn = 0
count = 0

#Set a pin, whichever...
eject = 3

GPIO.setup(eject, GPIO.OUT)
GPIO.output(eject,True) #active low, so it's by default high

while(count < len(expIn)): #watch that out by one error
    #Wait???
    string = map(str, raw_input().split())
    newIn = [int(s) for s in string if (s.isdigit())]
    if (newIn != oldIn):
        if(newIn[0] == expIn[count]):
            count = count + 1
            print('Expected')
        else:
            count = 0
            print('Not expected')
    oldIn = newIn

GPIO.output(eject,False)
GPIO.cleanup()

print('Eject')
