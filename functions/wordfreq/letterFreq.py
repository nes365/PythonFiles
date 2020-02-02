#!/usr/bin/python
# create dictionary a-z
# set value of dictionary a=0, b=0 etc
# Open file

# for each line in file, 
# remove whitespace
# for each char, increment corresponding entry in dict

from string import ascii_lowercase
with open('input') as f:
	text = f.read().strip()
	dic = {}
	for x in ascii_lowercase:
		dic[x] = text.count(x)

# Print as a list (k = key, v = value)python 		
for k, v in dic.items():
	print k, v


#print dic
