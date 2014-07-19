# 19Apr14
# A program to mimic a simple battery-switch-LED circuit


import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

switch = 2
led = 3


GPIO.setup(switch, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)


prev_input = 0
i = 0
while True:
    input1 = GPIO.input(switch)

    if (prev_input and (not input1)):
        i+= 1
        print i
        GPIO.output(led, True)

    if (input1):
        GPIO.output(led, False)
    
    prev_input = input1
    time.sleep(0.05)

