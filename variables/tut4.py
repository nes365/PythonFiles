#!/usr/bin/python
# Tuple tutorial

# A tuple is another sequence data type that is similar to the list. A tuple consists of values seperated by commas.
# Unlike lists, tuples are enclosed within parentheses
# The main differences between lists and tuples are: Lists are enclosed in [] and their elements and size can be changed.
# Tuples are enclosed in () and cannot be updated. Tuples can be thought of as read-only lists.

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists
