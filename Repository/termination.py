#!/usr/bin/python

''' figure out how to run apps in python
# figure out how to close apps
# figure out how to use a timer in python
# figure out how to 
'''

'''digitQueue[CODESIZE]

while (1)
{
 //run multimon.sh >output.file (not FIFO)
 //Kill multimon.sh
 //F = open(output.file)
 foreach DTMFdigit in F
 {
    digitQueue.add(DTMFdigit)
    digitQueue.isValidCode()
 }

}'''

''' SET UP TIME'''
import os
import subprocess
import signal 
from sys import stdin
import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BOARD) # PINS ARE LABALLED ACCORDING TO THE STUFF ON THE BOARD. NO MORE CONFUSION

testIn = [5,6,7,8,9,10,11,12] #This is a random test code I made
termIn = [1,2,9,5,1,2,9,5] #this is Jim's Birthday
countKill = 0
dtmfIn = [] #all digits from file
tempIn = []

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

''' FINISHED SET UP'''

while(True): #main loop
    proc1 = subprocess.Popen("sudo multimon -a DTMF -t raw ./soundfifo.raw > multimon.log", shell = True) # may to multithread
    proc2 = subprocess.Popen("sudo rtl_fm -M fm -f 436e6 -s 260k -r 22050 -g 50 ./soundfifo.raw", shell = True)
    
    time.sleep(30) #wait for 30 minutes 
    # close programs
    if (proc1.kill())
    {
        print "Error process not killed\n";
        break;
    }
    proc2.kill() #kill both processes
    F = open('multimon.log', 'r')
    for line in F: # now check numbers...
        if (line[0:6] != "DTMF: "):
            s = line[6]
            print s
            digit = dict1[s] # convert the character to a number
            if (prevDigit != digit):
                dtmfIn.append(digit) # put next digit at end of array
            prevDigit = digit # do this at the end of the loop
            
    # so now dtmfIn should contain all the digits from multimon.log
    i = 0
    for i in range(len(dtmfIn) - 8): # go through loop and check for codes
        tempIn = dtmfIn[i:i+8] # check your out by one error and syntax
        if (tempIn == termIn):
            GPIO.output(eject,False)
            print('Eject')
            break #if we hit the termination thing, we shouldn't do anything else
        if (tempIn == testIn):
            GPIO.output(test,False)
            print('LED should light up')

     
     
GPIO.cleanup()
