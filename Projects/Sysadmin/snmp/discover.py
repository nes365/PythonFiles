#!/usr/bin/env python
from processing import Process, Queue, Pool
import time
import subprocess
import sys
from snmp import Snmp
import pdb


q = Queue()
oq = Queue()
#ips = ["172.30.44.1","172.30.44.46","172.30.44.47"]
ips = ["192.168.1.1","192.168.1.67"]
num_workers = 10

class HostRecord(object):
	""" Record for hosts """
	def __init__(self, ip=None, mac=None, snmp_response=None):
		self.ip = ip
		self.mac = mac
		self.snmp_response = snmp_response
	def __repr__(self):
		return "[Host Record('%s','%s','%s')]" % (self.ip, self.mac, self.snmp_response)

	def f(i,q,oq):
		while True:
			time.sleep(.1)
			if q.empty():
				sys.exit()
				print "Process Number: %s Exit" % i
			ip = q.get()
			print "Process Number: %s" % i
			ret = subprocess.call("ping -c 1 %s" % ip, shell=True,stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)
			if ret == 0:
				print "%s: is alive" % ip
				oq.put(ip)
			else:
				print "Process Number: %s didn't find a response for %s " % (i, ip)
				pass
	
	def snmp_query(i,out):
		while True:
			time.sleep(.1)
			if out.empty():
				sys.exit()
				print "Process Number: %s" % i
			ipaddr = out.get()
			s = Snmp()
			h = HostRecord()
			h.ip = ipaddr
			h.snmp_response = s.query()
			print h
			return h
		try:
			q.putmany(ips)

		finally:
			for i in range(num_workers):
				p = Process(target=f, args=[i,q,oq])
				p.start()
			for i in range(num_workers):
				pp = Process(target=snmp_query, args=[i,oq])
				pp.start()
		
		print "main process joins on queue"
		
		p.join()
		while not oq.empty():
			print "Validated", oq.get()

		print "Main program finished"
