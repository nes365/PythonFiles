# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:34:21 2015

@author: nsouthor
"""

import serial
found = False
for i in range(64):
    try:
        ser = serial.Serial(i)
        ser.close()
        print ("Found COM"), i+1
        found=True
    except serial.serialutil.SerialException:
        pass
    
if not found:
    print ("No ports found")
      