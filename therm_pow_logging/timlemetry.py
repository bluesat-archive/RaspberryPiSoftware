# timlemetry2.py - For thermal sensor logging.



# based on code created 08-11-14: Declan Walsh
# and brashly plagarised because I haven't touched python for ages and it's easier to modify existing code than write your own


# last updated 2014-12-5: Timothy Chin 



import time
from datetime import datetime

debug = 1


# opens the initialisation file
f_init = open('serials', 'r')

# retrieve the serials and their names from the serials file, then splits them into lines
init_str = f_init.read()
init_list = init_str.split('\n')
del init_list[len(init_list)-1]

if debug == 1:
	for a in init_list:
		print a

# populates a dictionary containing the names of each sensor and their unique serial number
d_serials = {}

for key in init_list:
	temp = key.split(' ')
	d_serials[temp[0]] = temp[1] #d_serials is the dictionary containing the serial numbers and their names
	if debug == 1:
		print temp[0] 
		print temp[1] 
		print temp[0], "written!"


l_serials = d_serials.keys() 
# l_serials is a list of the keys of the dictionary. the keys are always names, so this list will only contain
# the names of each sensor

f_init.close()


# test the dictionary and key list
if debug == 1:
	for name in l_serials:
		print name, ' : ', d_serials[name]


# opens the log file to be appended to.
file_object = open('telem_log', 'a')

# start the main loop
while True:

		# pulls in the neccessary data from sensors
		time0 = datetime.now()
		tempC = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3	
		timeStamp = time0.strftime("%Y/%m/%d %H:%M:%S:%f")
		count = count + 1
		
		# outputs the data to appropriate file
		if tempC > 40:
			# critical temp exceeded writes to critical file and normal file
			file_object_crit.write(repr(count) + ',' + repr(timeStamp) + ',' + repr(tempC) + '\n')
			file_object.write(repr(count) + ',' + repr(timeStamp) + ',' + repr(tempC) + '\n')
		else:
			# normal temp only writes to normal file
			file_object.write(repr(count) + ',' + repr(timeStamp) + ',' + repr(tempC) + '\n')
		print count

		# repeat logging after 1 second interval
		time.sleep(1)
	
