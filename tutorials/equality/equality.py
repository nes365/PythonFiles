#!/usr/bin/python
import re
import urllib
import string
page = urllib.urlopen(
    "http://www.pythonchallenge.com/pc/def/equality.html").read()
output = ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', page))
print(output)
