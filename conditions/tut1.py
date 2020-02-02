#!/usr/bin/python

import math
import os
import sys


var = 100
if (var == 100):
    print("Value of expression is 100")

print("Goodbye!")


print(sys.version)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


name = input("Your Name? ")
print("Hello, ", name)
