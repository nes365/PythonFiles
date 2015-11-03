# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:44:00 2015

@author: NSouthor
"""

from pylab import *

# Constant definitions
NMI = 1852.0
# hard coded for the moment
#data = "C:\\Users\\nsouthor\\Documents\\GitHub\\PythonFiles\\GPS\\data\\gps-03-11-15.csv"


def processGPSData(data):
    """ Processes GPS data, NMEA 0183 format, 
    
        Returns a tuple of arrays: latitude, longitude, velocity [km/h],
        time [sec] and number of satellites.
        See also: http://www.gpsinformation.org/dale/nmea.htm. """
        
    latitude  = []
    longitude = []
    velocity  = []
    t_seconds = []
    num_sats  = []
    
    for row in data:
            if row[0] == '$GPGSV':
                num_sats.append(float(row[3]))
            elif row [0] == '$GPRMC':
                t_seconds.append(float(row[1][0:2])*3600 + float(row[1][2:4])*60 + float(row[1][4:6]))
                latitude.append(float(row[3][0:2]) + float(row[3][2:])/60.0)
                longitude.append((float(row[5][0:3]) + float(row[5][3:])/60.0))
                velocity.append(float(row[7])*NMI/1000.0)
                
    return (array(latitude), array(longitude). array(velocity), array(t_seconds), array(num_sats))
    
    