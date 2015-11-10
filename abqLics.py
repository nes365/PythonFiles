#!/usr/bin/python
import os
import sys
import math

cores=float(raw_input("Enter number of cores: ")) 
licsReq = (5 * math.pow(cores,0.422))
licsReq=math.floor(licsReq)
print "Licenses required: ", licsReq
