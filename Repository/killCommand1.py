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
dtmfIn = [0,0,0,0,0,0,0,0]

dict1 = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,    
    'D': 13,
    '*': 14,
    '#': 15
}

#Set a pin, whichever...
eject = 3

GPIO.setup(eject, GPIO.OUT)
GPIO.output(eject,True) #active low, so it's by default high

while (True):
    while(dtmfIn != expIn): 
       string = raw_input()
       # remove the 'DTMF: ' bit 
       s = string[6] # this number may need changing  
       newIn = dict1[s] # fix issue regarding newline
       if (newIn != oldIn):
           dtmfIn[count] = newIn
           count = count + 1
           oldIn = newIn
       if (count >= 8):
           count = 0
           print "checked"
           print dtmfIn
           if (dtmfIn == expIn):
               GPIO.output(eject,False)
               GPIO.cleanup()
               print('Eject')
