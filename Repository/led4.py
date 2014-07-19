# 19Apr14
# A program to mimic a simple battery-switch-LED circuit
# The LED switches on and off on input pulses
# The operation of this circuit depends on the switch being active high or low.

import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

#Defines the GPIO inputs/outputs
switch = 2
led = 3

# initialises GPIO pina
GPIO.setup(switch, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)


prev_input = 0
i = 0
while True:
    input1 = GPIO.input(switch) #defines the swtich pin as input

    if (prev_input and (not input1)): 
        i+= 1
        print i
        GPIO.output(led, i%2) #odd numbers turn it on, even turn it off

#    if (input1):
#        GPIO.output(led, False)
    
    prev_input = input1
    time.sleep(0.05) #wait 0.05s

