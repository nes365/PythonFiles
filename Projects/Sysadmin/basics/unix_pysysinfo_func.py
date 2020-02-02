#!/usr/bin/env python
# A system information gathering script
import subprocess

def uname_func():
	uname="uname"
	uname_arg="-a"
	print("Gathering system information with %s command:\n" % uname)
	subprocess.call([uname, uname_arg])


def disk_func():
	diskspace="df"
	diskspace_arg="-h"
	print("Gathering diskspace information with %s command:\n" % diskspace)
	subprocess.call([diskspace, diskspace_arg])

# Main function which calls other functions

def main():
	uname_func()
	disk_func()

# Any code that you indent underneath this statement gets run only when it is executed from the command line.
# So when you import it as a module it doesn't run main()

if __name__ == "__main__":
	main()
