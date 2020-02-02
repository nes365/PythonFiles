# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 07:12:08 2018
FPS Calculator
@author: southorn
"""

import datetime

class FPS:
    def __init__(self):
        # Store the start time, end time and number of frames
        # that were examined between the start and end intervals
        self._start = None
        self._end = None
        self._numFrames = 0
        
    def start(self):
        # Start the timer
        self._start = datetime.datetime.now()
        return self
    
    def stop(self):
        # Stop the timer
        self._end = datetime.datetime.now()
        
    def update(self):
        # Increment the total number of frames examined
        # during the start and end intervals
        self._numFrames += 1
        
    def elapsed(self):
        # Return the total number of seconds between the start
        # and end interval
        return (self._end - self._start).total_seconds()
    
    def fps(self):
        # Compute the (approximate) frames per second
        return self._numFrames / self.elapsed()