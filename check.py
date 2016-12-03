#!/usr/bin/python

import time,os
from urllib2 import urlopen

# Reference :
# http://stackoverflow.com/questions/9481419/how-can-i-get-the-public-ip-using-python2-7

# Update stored IP address with current IP address
def updateStoredIP(filename):

	# Get current public IP address
	currentIP = urlopen('http://ip.42.pl/raw').read()

	# Get stored public IP address
	IPFile = open(filename)
	storedIP = IPFile.readline()
	IPFile.close()

	# Check the change
	if storedIP.find(currentIP) < 0:

		# Update stored IP address
		IPFile = open(filename, 'w')
		IPFile.write(currentIP)
		IPFile.close()
		print 'IP address has been udpated : '+currentIP

		# Commit to Github
		os.system('git commit -m "Update IP address"')
		os.system('git push -u origin master')

while 1:
	updateStoredIP('IP.md')

	# check interval is 5 seconds
	time.sleep(5)
