#!/usr/bin/python

import time,os,re,json
from urllib2 import urlopen

# Update stored IP address with current IP address
def updateStoredIP(filename):

	# Get current public IP address
	try:
		currentIP = urlopen('http://ip.42.pl/raw').read()
	except:
		try:
			ipinfo = urlopen('http://ip138.com/ip2city.asp').read()
			currentIP = re.search('\d+\.\d+\.\d+\.\d+',ipinfo).group(0)
		except:
			return

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
		os.system('git add '+filename)
		os.system('git commit -m "Update IP address"')
		os.system('git push -u origin master')

while 1:
	updateStoredIP('IP.md')

	# check interval is 5 seconds
	time.sleep(5)
