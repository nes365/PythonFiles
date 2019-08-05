#/usr/bin/python
import urllib, re
import pickle
test = pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
print test


def print_line(pair_list):
	print ''.join(pair[0] * pair[1] for pair in pair_list)

for pair_list in test:
	print_line(pair_list)
