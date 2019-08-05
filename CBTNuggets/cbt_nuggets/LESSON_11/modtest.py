#!/usr/bin/python

'''
Name: modtest.py
Author: Nick Southorn
Purpose: Test out module imports
'''

def square(x):
    # Returns the square of a given integer
    return x * x

if __name__ == '__main__':
    print('Testing: square of 2 == ', square(2))
