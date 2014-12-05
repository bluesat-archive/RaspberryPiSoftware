# timlemetry2.py - For thermal sensor logging.



# based on code created 08-11-14: Declan Walsh
# and brashly plagarised because I haven't touched python for ages and it's easier to modify existing code than write your own


# last updated 2014-12-5: Timothy Chin 



import time
from datetime import datetime

debug = 0


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

# close the init file
f_init.close()


# test the dictionary and key list
if debug == 1:
	for name in l_serials:
		print name, ' : ', d_serials[name]

# opens the log files to be appended to for each sensor
d_logs = {}

for name in l_serials:
	d_logs[name] = open('logs/' + name + '_log', 'a')

# start the main loop
while True:

	# loop to go through each sensor individually and retrieve its data
	for name in l_serials:
		address = '/sys/bus/w1/devices/' + d_serials[name] + '/w1_slave'
		if debug == 1:
			print "address is " + address
		
		# get the current time
		time0 = datetime.now()

		# get the response from the sensor
		sens_data = open(address).read()
		if debug == 1:
			print sens_data

		# seperate the fluff from the numbers
		tempC = sens_data.split(' t=')[1]

		timeStamp = time0.strftime("%Y-%m-%d %H:%M:%S:%f")
		d_logs[name].write(timeStamp + ',' + name + '=' + tempC)
		if debug == 1:
			print timeStamp + ' ' + name + '=' + tempC

	# repeat logging after 1 second interval
	time.sleep(1)
	
