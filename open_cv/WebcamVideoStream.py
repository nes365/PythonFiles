# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 07:21:49 2018

@author: southorn
"""

from threading import thread
import cv2

class WebcamVideoStream:
    def __init__(self, src=0):
        # initialise the video camera stream and read the 
        # first frame from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        
        # Initialise the variable used to indicate if the 
        # thread should be stopped
        self.stopped = False
        
    def start(self):
        # Start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self
    
    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the thread indicator variable is set, stop the thread
            if self.stopped:
                return
            
            # Otherwise read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
            
    def read(self):
        # Return the frame most recently read
        return self.frame
    
    def stop(self):
        # Indicate that the thread should be stopped
        self.stopped = True
        