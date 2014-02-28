#test by Y.Kang

import RPIO
import time

RPIO.setup(2, RPIO.OUT)
RPIO.setup(3, RPIO.OUT)
RPIO.setup(4, RPIO.OUT)

#def select (i):
#	if i!= 0:
#		RPIO.OUT(i,False)
#	else:
#		RPIO.OUT(i,True)

#initializing all leds to be off

try:
      while True:
	      colour = raw_input( "Enter colour:")
	      if colour == 'O':
		      i = 0
	      elif colour == 'B':
		      RPIO.OUT(2, False)
	      elif colour == 'G':
		      RPIO.OUT(3, False)
	      elif colour == 'R':
		      RPIO.OUT(4, False)
	      else:
		      print "invalid input"; i = -1



except KeyboardInterrupt:
      for i in range(2,5):
            RPIO.OUTPUT(i, True)
      RPIO.cleanup()

