# Mark Yeo 1Mar14
# A program to fade smoothly between 3 LED's using PWM
# Edited from http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control


RED = 4
GREEN = 3
BLUE = 2


import RPi.GPIO as GPIO
from time import sleep



def setup():
    GPIO.setmode(GPIO.BCM)    # orig GPIO.setmode(GPIO.BCM)
    for colour in [RED, GREEN, BLUE]:
        GPIO.setup(colour, GPIO.OUT)
        GPIO.output(colour, True)


def fade(colFin, colInit, totalTime):
    col1 = GPIO.PWM(colInit, 100)
    col2 = GPIO.PWM(colFin, 100)
    pauseTime = 0.1 #totalTime/100
    for i in range(0,101):      # 101 because it stops when it finishes 100
        col1.ChangeDutyCycle(100 - i)
        col2.ChangeDutyCycle(i)
        sleep(pauseTime)
    #print "finished one cycle"



"""
fade(colInit, colFin, totalTime):
    pauseTime = totalTime/100
    for i in range(0,101):              # 101 because it stops when it finishes 100
        GPIO.PWM(colInit, 100).ChangeDutyCycle(i)
        GPIO.PWM(colFin, 100).ChangeDutyCycle(100 - i)
        sleep(pauseTime)

"""

setup()
# Necessary? (included in fade())
red = GPIO.PWM(RED, 100)        # create object red for PWM on port RED at 100 Hertz
green = GPIO.PWM(GREEN, 100)    # how to incorporate into setup()? [how to pass arrays in/out of fn's?]
blue = GPIO.PWM(BLUE, 100)


red.start(100)                    # red on 0% duty cycle (off)
green.start(100)
blue.start(100)                # green on 100% (fully on)

intervalTime = 1                # Time to change between solid colours


try:                            # 'try' is used to GPIO.cleanup() when program is interrupted
    while True:
        blue.start(100)
        fade(RED, GREEN, intervalTime)
        print "from red to green done"
        red.start(100)                    # red on 0% duty cycle (off)
        fade(GREEN, BLUE, intervalTime)
        print "GB done"
        green.start(100)
        fade(BLUE, RED, intervalTime)
        print "BR done"

except KeyboardInterrupt:
    red.stop()                  # stop the white PWM output
    green.stop()
    blue.stop()
    GPIO.cleanup()              # clean up GPIO on CTRL+C exit

