#!/usr/bin/env python

# Simple script to show error messages in the RANCID logs. 
# Logs are saved in /usr/local/rancidv/var/logs (hardcoded here)

import os

logPath = "/usr/local/rancid/var/logs/"
os.chdir(logPath)

files = sorted(os.listdir(logPath), key=os.path.getctime)

newest = files[-1]

print "\nErrors in log file: ", newest
print "===============================================\n"
for line in open(newest):
	if "Error" in line:
		print line


