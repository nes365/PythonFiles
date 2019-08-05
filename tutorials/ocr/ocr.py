#!/usr/bin/python
#ins = open( "sourcetext", "r")
#array = []
#for line in ins:
#		array.append( line )
#ins.close

f = open('sourcetext')
lines = f.readlines()
f.close()


# print array
# Create an empty dictionary
CharDict = {}
# Create a dictionary of letter frequency
for char in lines:
	if char not in CharDict.keys():
		CharDict[char] = 1
	else:
		CharDict[char] += 1
# Create a list of items to remove
removeList = []
for key in CharDict:
	if CharDict[key] > 40: 
		removeList += key

# Remove items froms string
for char in removeList:
	lines = lines.replace( char, "" )

print lines,

