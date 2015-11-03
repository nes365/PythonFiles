# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 15:47:02 2014

@author: NSouthor
"""

# Define the function with def
# parameters held in parens
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
    
    
def fahr_to_celsius(temp):
    return ((temp -32) / 1.8 )
    
def celsius_to_fahr(temp):
    return ((temp *1.8) + 32)

# making use of the functions
print 'freezing point of water:', fahr_to_kelvin(32),'K'
print 'boiling point of water:', fahr_to_kelvin(212),'K'
print 'freezing point of water:', fahr_to_celsius(32),'C'
print 'boiling point of water:', fahr_to_celsius(212),'C'
print 'freezing point of water:', celsius_to_fahr(0),'F'
print 'boiling point of water:', celsius_to_fahr(100),'F'

# different types of number formats
# this will just display an integer value (rounded down)
print '10/3 is:', 10/3 # will display 10/3 = 3

# if eith part of the division is a float, the result will be shown as a float
print '10.0/3 is:', 10.0/3 # will display 10.0/3 is 3.33333333333 
print '10/3.0 is:', 10/3.0 # will display 10/3.0 is 3.33333333333

# or you can specify a float
print 'float(10)/3 is:', float(10)/3 # will display float(10)/3 is: 3.33333333333

# this can be applied to variables
a=10
b=3
print 'a/b is:', a/b # will display a/b is: 3
print 'float(a)/b is:', float(a)/b # will display float(a)/b is: 3.33333333333


# applying this to our original function

def fahr_to_kelvin(temp):
    return ((temp - 32) * (5.0/9.0)) + 273.15


def kelvin_to_celsius(temp):
    return temp - 273.15

print 'absolute zero in celcius is:', kelvin_to_celsius(0.0)

def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result=kelvin_to_celsius(temp_k)
    return result
    
print 'freezing point of water in Celsius:', fahr_to_celsius(32.0)

# Playing with text

# Function called fence which wraps text a with text b
def fence(a,b):
    return b + a + b

print fence('name', '*')

# function called outer which displays the first and last chars in a string

def outer(text):
    a=text[0]
    b=text[-1]
    return a,b
        
print outer('nicholas')
    

import numpy as np

def span(a):
    diff = a.max() - a.min()
    return diff
    
data
    
    
    
    




















































