#!/usr/bin/python

import thread
import subprocess

#def namuruLog():
#    subprocess.call("./namuruLog.sh")
#    return
#    
#def DTMF():
#    subprocess.call("/home/pi/playRadio.sh") #Careful m8. change this to 
    # something else like DTMF.sh or whatever
#    return

def runProg(threadname, string):
    subprocess.call(string, shell=True)
    return

try:
    thread.start_new_thread(runProg,("Thread 1", "/home/pi/RaspberryPiSoftware/Repository/namuruLog.sh",))
    thread.start_new_thread(runProg("Thread 2", "/home/pi/playRadio.sh",) )
except:
    print "U wot m8"
