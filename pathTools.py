# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:50:16 2015

@author: Nick Southorn
"""

import os

print("Current working directory")
print(os.getcwd() + "\n")

print("Absolute path")
print(__file__ + "\n")

print("Absolute path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, file = os.path.split(full_path)
print(path + ' --> ' + file + "\n")

print("This file directory only")
print(os.path.dirname(full_path))
