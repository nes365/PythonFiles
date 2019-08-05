#!/usr/bin/python

'''
The first unassigned string in a module 
is the docstring. What you see above 
is a "exec/hack (hashbang)", that enables
if1.py instead of typing python if1.py
on a *nix system.
'''

num = input("Enter an integer: ")
num = int(num)

if num < 0:
    print("The absolute value of", num, "is", -num)
else:
    print("The absolute value of", num, "is", num)

