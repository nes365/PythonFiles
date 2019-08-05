#!/usr/bin/python
# Dictionary tutorial

# Python's dictionaries are kind of hash table type. 
# They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
# A dictionary key can be almost any Python type, but are usually numbers or strings. 
# Values, on the other hand, can be any arbitrary Python object.
# Dictionaries are enclosed by curly braces ( { } ) and values can be assigned and accessed using square braces ( [] ).

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code': '6589', 'dept': 'sales'}

print dict['one']		# Prints value for 'one' key
print dict[2]			# Prints value for 2 key 
print tinydict			# Prints complete dictionary
print tinydict.keys()		# Prints all the keys
print tinydict.values()		# Prints all the values


