# Mark Yeo 22Feb14
# A program to cycle through RGB LEDs


import time
import RPIO

# Constants matching to GPIO pin #
OFF = 0
RED = 4
GREEN = 3
BLUE = 2


# Fn's
def pinSetup():
	for i in [RED,GREEN,BLUE]:
		RPIO.setup(i,RPIO.OUT)
		RPIO.output(i,True)

def setLedColour(colGivn):
	if colGivn == OFF:
		for i in [RED,GREEN,BLUE]:
			RPIO.output(i, True)
	elif colGivn == RED or colGivn == GREEN or colGivn == BLUE:
		setLedColour(OFF)
		RPIO.output(colGivn, False)
	else:
		pass #do nothing

def finish():
	setLedColour(OFF)
	RPIO.cleanup()

# Main
pinSetup()

for count in range(0,10):
	setLedColour(RED)
	time.sleep(0.2)
	setLedColour(GREEN)
	time.sleep(0.2)

	setLedColour(BLUE)
	time.sleep(0.2)
finish()



#difference |.| RPIO & GPIO?

