# Mark Yeo 1Mar14
# A program to fade smoothly between 3 LED's using PWM
# Edited from http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control


"""
Bugs:
- LED flickering during fades
- Program quitting randomly
"""

RED = 4
GREEN = 3
BLUE = 2


import RPi.GPIO as GPIO
from time import sleep



def setup():
    GPIO.setmode(GPIO.BCM)
    for colour in [RED, GREEN, BLUE]:
        GPIO.setup(colour, GPIO.OUT)
        GPIO.output(colour, True)


def fade(colFin, colInit, totalTime):
    col1 = GPIO.PWM(colInit, 100)
    col2 = GPIO.PWM(colFin, 100)
    pauseTime = totalTime/100.0 # .0 causes float division
    for i in range(0,101):
        col1.ChangeDutyCycle(100 - i)
        col2.ChangeDutyCycle(i)     
        #GPIO.PWM(colFin, 100).ChangeDutyCycle(i) # functional, but screws with colour order
        sleep(pauseTime)
      

# Main
setup()
red = GPIO.PWM(RED, 100)        # create object red for PWM on port RED at 100 Hertz
green = GPIO.PWM(GREEN, 100)
blue = GPIO.PWM(BLUE, 100)

red.start(100)                  # Turn off all LEDs (100 is LED off)
green.start(100)
blue.start(100)

intervalTime = 1                # Time taken to change between solid colours (seconds)
iteration = 0                   # For debugging - program quits unexpectedly

try:                            # 'try' is used to GPIO.cleanup() when program is interrupted
    while True:
        print "iteration: " + str(iteration)
        red.start(0)            # Turns on red only
        green.start(100)
        blue.start(100)
        fade(RED, GREEN, intervalTime)
        #print "RG done"
        red.start(100)
        green.start(0)
        blue.start(100)
        fade(GREEN, BLUE, intervalTime)
        #print "GB done"
        red.start(100)
        green.start(100)
        blue.start(0) 
        fade(BLUE, RED, intervalTime)
        #print "BR done"
        iteration += 1

except KeyboardInterrupt:
    red.stop()
    green.stop()
    blue.stop()
    GPIO.cleanup()              # clean up GPIO on CTRL+C exit

