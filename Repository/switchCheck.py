# 19Apr14
# Testing switch input

#import RPIO
import time

switch = 2

def pinSetup():
    GPIO.setup(switch, GPIO.IN)

while True:
    if (GPIO.input(switch)):
        print "BOOOM\n"
    else:
        print "switch off\n"

