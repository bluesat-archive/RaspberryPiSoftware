#This program tests for separation of the dyneema. A circuit connecting pins 7 and 11 with a ground pin can be found in Drive/2ndBalloon/System/Separation Mechanism Casing

#To do:	Implement time stamping
#	Implement datawrite to sd card
#	Add to existing dtmf program
#Last updated: 2/11/14 by Tom Dixon

import RPi.GPIO as GPIO
import time
from datetime import datetime
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
sigout = 12
sigin = 11
GPIO.setup(sigout,GPIO.OUT)
GPIO.setup(sigin,GPIO.IN)
GPIO.output(sigout,1)
print("Separation Mechanism activated at " + str(datetime.now()))
n = 0
while n < 20:
	if GPIO.input(sigin) == False:
		print("Separation confirmed at " + str(datetime.now()))
		break
	n = n+1
	time.sleep(2)
if n == 20:
	print("Timeout occured at " + str(datetime.now()))
GPIO.output(sigout,0)

GPIO.cleanup()
