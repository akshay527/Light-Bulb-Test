import subprocess
import time

# A script created for performing the light bulb experiment to test the Wemos
# REQUIRES: A Wemos.txt file in the current directory containing the IP addresses of the Wemos to be tested
#	    The wemo_monitor.sh script (the script will need to be changed to log measurements to the current directory)

def ex(cmd):
	subprocess.call(cmd, shell=True)

with open("Wemos.txt") as f:
	numCombinations = int(raw_input("Number of Light Bulb Combinations? "))
	fline = f.readline()
	wemo = 1
	while fline:
		ex("echo " + fline.strip() + " > ~/myWemo.txt") # Places the IP address of the current Wemo into a file	
		ex("./wemo_monitor.sh start")
		time.sleep(60)
		for y in xrange(0, numCombinations):
			print "Insert Light Bulbs"
			x = raw_input("Filename for this Combination: ")
			time.sleep(30)
			ex("> energy.log")
			time.sleep(25)	
			ex("cp energy.log " + str(x))
		ex("./wemo_monitor.sh stop")
		wemo = wemo + 1
		fline = f.readline()
		if fline:
			y = raw_input("Insert Wemo " + str(wemo))
ex("rm ~/myWemo.txt") # Remove the ~/myWemo.txt needed by wemo_monitor.sh)
ex("./convert.sh") # Renames the files as necessary
