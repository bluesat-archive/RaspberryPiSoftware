import RPIO
import time

RPIO.setup(2, RPIO.OUT)
RPIO.setup(3, RPIO.OUT)
RPIO.setup(4, RPIO.OUT)

for i in [2,3,4]:
	RPIO.output(i, True)
#comment

try:
      while True:
	      for i in [2,3,4]:
		      print "turning on GPIO{number}".format(number=i)
		      RPIO.output(i, False)
		      time.sleep(1)
		      RPIO.output(i, True)

except KeyboardInterrupt:   
      for i in [2,3,4]:
            RPIO.output(i,True)
      RPIO.cleanup()


