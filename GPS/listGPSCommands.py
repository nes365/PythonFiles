# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:35:29 2015

@author: NSouthor
"""

def listGPSCommands(data):
    """ Counts the number of times a GPS command is observed.
    Returns a dictionary object """
    
    gpsCmds=dict()
    for row in data:
        try:
            gpsCmds[row[0]] +=1
        except KeyError:
            gpsCmds[row[0]] =1
            
    return gpsCmds
    

    