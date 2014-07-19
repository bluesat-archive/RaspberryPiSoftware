# 19Apr14
# [Not working] A program to mimic a simple battery-switch-LED circuit


import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

led = 3
switch = 14

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
        GPIO.output(led, True) 
        i *= 2
        print i
    prev_input = input1
    time.sleep(1)
    GPIO.output(led ,False) 
    
    GPIO.cleanup()
