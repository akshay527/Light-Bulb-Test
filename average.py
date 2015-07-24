#!/env/python
import sys
import subprocess

# This script takes a logfile as a command line argument  and computes averages for sets of data points

# The logfile should be formatted as follows:
#  <data point>
#  <data point>
#  <data point>
      . . .
#  <data point>

# <insert blank line>

#  <data point>
#  <data point>
#  <data point>
      . . .
#  <data point>

logFile = sys.argv[1]
f = open(logFile) # Opens the log file containing the measurement data
fline = f.readline() # Reads the first line of the file
ftotal = 0 # Intializes total
fcount = 0 # Initialize line/measurement count
avg = "" # Initializes the avg
while fline: # While there are more lines in the file to be read
        try:
		ftotal = ftotal + float(fline) # Adds the measurement data on the given line to the total 
        	fcount = fcount + 1 # Increments the line/measurement count
		fline = f.readline() # Reads the next line
		if fcount > 0: # Ensures no division by 0 error occurs (ie Ensures there is measurement data)
        		avg = str( ftotal / fcount) # Sets CPU to be the average CPU utilization
        	else: # There are no measurements
 	        	avg = "-1"
	except: # When the program encounters a blank line, it throws an exception
		fcount = 0 # Reset the line/measurement count to 0 
		ftotal = 0 # Reset the total to 0
		fline = f.readline() # Reads the next line
		subprocess.call("echo " + avg + " >> tmp", shell = True) # Creates a temporary file containing the data
		avg = "" # Resets the avg
f = open("tmp")
fline = f.readline()
while fline:
	try:
		print(float(fline)) # Prints the averages
		fline = f.readline()
	except:
		fline = f.readline()
subprocess.call("rm tmp", shell = True) # Removes the temporary file
