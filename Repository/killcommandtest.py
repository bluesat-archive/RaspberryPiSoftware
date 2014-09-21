#!/usr/bin/python

# Make like a while(true) loop to
# read in stuff from Stdin (NEED TO KNOW FORMAT)
# Scratch most of this.
# Make a list of DTMF outputs to check against
# Check input against that
# Roll pin control into a function
# Call function that deals with error checking. (LATER)
# For now make an abort function "abort" when it receives expIn
# Jesus Take the Wheel!
from sys import stdin
import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BOARD) # PINS ARE LABALLED ACCORDING TO THE STUFF ON THE BOARD. NO MORE CONFUSION

testIn = [5,6,7,8,9,10,11,12] #This is a random test code I made
expIn = [1,2,9,5,1,2,9,5] #this is Jim's Birthday
oldIn = 0
countKill = 0
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
#Set a pin, this is the eject pin
eject = 7
GPIO.setup(eject, GPIO.OUT)
GPIO.output(eject,True) #active low, so it's by default high

#Set a pin, this is the test pin
#The test pin should be attached to a 
test = 11
GPIO.setup(test, GPIO.OUT)
GPIO.output(test,True) #active low once again

while (True):
    while(dtmfIn != expIn):
        string = stdin.readline()
        # remove the    'DTMF: ' bit
        if (string[0:6] != "DTMF: "):
            continue
        s = string[6] # this number may need changing
	print s
        newIn = dict1[s] # fix issue regarding newline
        if (newIn != oldIn):
            dtmfIn[countKill] = newIn
            countKill = countKill + 1
            oldIn = newIn
        if (countKill >= 8):
            countKill = 0
            print "checked"
            print dtmfIn
        if (dtmfIn == expIn):
            GPIO.output(eject,False)
            print('Eject')
        if (dtmfIn == testIn):
            GPIO.output(test,False)
            print('LED should light up')
   
GPIO.cleanup()
