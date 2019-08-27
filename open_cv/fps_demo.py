# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 07:33:52 2018

@author: southorn
"""

from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100, help="# of frames to loop over in FPS test")
ap.add_argument("-d", "--display", type=int, default=-1, help="Wether or not frames should be displayed")
args = vars(ap.parse_args())

# Grab a pointer to the video stream and initialise the FPS counter
print("[INFO] sampling frames from the webcam...")
stream = cv2.VideoCapture(0)
fps = FPS().start()

# Loop over some frames
while fps._numFrames < args["num_frames"]:
# Grab the frame from the stream and resize it to have a max
# width of 400 pixels
    (grabbed, frame) = stream.read()
  #  frame = imutils.resize(frame, width=400)

# Check to see if the frame should be displayed to our stream
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
    
# Update the FPS counter
    fps.update()
    
# Stop the timer and display FPS information
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx FPS: {:.2f}".format(fps.fps()))
    
# Cleanup
    stream.release()
    cv2.destroyAllWindows()
    
    
# Create a threaded video stream, allow the camera sensor to warm up,
# and start the FPS counter
print("[INFO] sampling THREADED frames from the webcam...")
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()

# Loop over some frames, this time using the threaded stream
while fps._numFrames < args["num_frames"]:
    # Grab the frame from the threaded video stream and resize
    # to have a max width of 400 pixels
    frame = vs.read()
   # frame = imutils.resize(frame, width=400)
    
    # Check to see if the frame should be displayed to our screen
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
    # Update the FPS counter
    fps.update()
    
# Stop the timer and display FPS information 
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx FPS: {:.2f}".format(fps.elapsed()))

# Cleanup
cv2.destroyAllWindows()
vs.stop()
