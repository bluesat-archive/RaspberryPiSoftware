# 19Apr14
# A program to test switch input, counting 2^(button presses)

import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
switch = 2
led = 3
GPIO.setup(switch, GPIO.IN)
prev_input = 0
i = 1
while True:
    input1 = GPIO.input(switch)
#    print input1
    if (prev_input and (not input1)):
#        print "Button Pressed"
        i *= 2
        if (i < 9000):
            print i
        elif (9000 < i < 20000):
            print ("its over 9000")
        elif (20000 < i < 1000000):
            print ("Why are you still doing this")
        elif(1000000 < i < 8000000):
            print ("you must be really, really bored")
        elif(8000000 < i < 16000000):
            print ("thats it I'm quitting on you")
        else:
            print ("okay.... I lied, keep pressing that button")
    prev_input = input1
    time.sleep(0.05)

