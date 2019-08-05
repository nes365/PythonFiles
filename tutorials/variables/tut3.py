#!/usr/bin/python
# List tutorial
# Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

# The values stored in a list can be accessed using the slice operator ( [ ] and [ : ] ) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus ( + ) sign is the list concatenation operator, and the asterisk ( * ) is the repetition operator

list = [ 'abcd', 786, 2.23, 'nick', 70.2 ]
tinylist = [ 123, 'nick' ]

print list		# Prints complete list
print list[0]		# Prints first element of the list
print list[1:3]		# Prints elements starting from 2nd till 3rd
print list[2:]		# Prints elements starting from 3rd element
print tinylist * 2	# Prints tiny list 2 times
print list + tinylist   # Prints concatenated lists
