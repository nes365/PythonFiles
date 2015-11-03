@@ -1,12 +0,0 @@
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 11:21:52 2015

@author: nsouthor
"""

def center(data, desired=0.0):
    '''Return a new array containing the original data centered around the desired value (0 by default)
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    
    return (data - data.mean()) + desired
\ No newline at end of file