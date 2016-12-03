#!/usr/bin/python

import time,os,re,sys,json
from urllib2 import urlopen

# Reference :
# http://stackoverflow.com/questions/9481419/how-can-i-get-the-public-ip-using-python2-7
# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

class TerminalTextStyle:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
			print TerminalTextStyle.WARNING + "Can't connect to internet" + TerminalTextStyle.ENDC
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

		print TerminalTextStyle.WARNING + 'IP address has been udpated : '+currentIP + TerminalTextStyle.ENDC

		# Commit to Github
		os.system('git add '+filename)
		os.system('git commit -m "Update IP address"')
		os.system('git push -u origin master')
	else:
		# If internet is OK and IP is not changed, terminal will display : ......
		print TerminalTextStyle.OKGREEN + "." + TerminalTextStyle.ENDC,
		sys.stdout.flush()

while 1:
	updateStoredIP('IP.md')

	# check interval is 5 seconds
	time.sleep(5)
