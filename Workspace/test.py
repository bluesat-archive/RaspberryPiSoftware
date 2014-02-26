#test by Y.Kang

import RPIO
import time

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPOI.setup(4, GPIO.OUT)

def select (i)
	if i!=0:
		RPIO.OUT(i,False)
	else:
		RPIO.OUT(i,True)



def getColour (i)
	colour = raw_input( "Enter colour:")
	
	if colour == 'O':
		i = 0
	elif colour == 'B'|| colour == 'b':
		i = 2
	elif colour == 'G'|| colour == 'g':
		i = 3
	elif colour == 'R'|| colour == 'r':
		i = 4
	else:
		print "invalid input"

	select (i)
