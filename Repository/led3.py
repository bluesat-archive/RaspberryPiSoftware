# 19Apr14
# A program to mimic a simple battery-switch-LED circuit

import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

led = 3
switch = 14
mode = False

GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

GPIO.output(led, True) 

prev_input = 0
i = 1

GPIO.output(led, False) 


while True:
    input1 = GPIO.input(switch)
#    print input1
    if (prev_input and (not input1)):
#        print "Button Pressed"
        mode = not mode
        
        if ( mode == True):
            GPIO.output(led, True)

    prev_input = input1
    time.sleep(1)
    GPIO.output(led ,False) 
    
    GPIO.cleanup()
