# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:05:55 2018
Basic opening of webcam with text overlay example.
@author: Nick Southorn
"""

import cv2

def show_webcam(mirror=False):
    webcam = cv2.VideoCapture(0)
    while True:
        ret, image = webcam.read()
        if mirror:
            image = cv2.flip(image, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # Display text on image
        # image to write on, text, start co-ords, font, thickness, colour
        cv2.putText(image,'OpenCV Demo',(10,50), font, 2,(255,255,255),2,cv2.LINE_AA)
        
        # Draw a diagonal blue line with thickness of 5 px
        # image to draw on, start co-ords, end co-ords, thickness
        cv2.line(image,(0,0),(640,480),(255,0,0),5)
        
        # Draw a circle
        # image to draw on, co-ords, radius, colour thickness (-1 to fill)
        cv2.circle(image,(320,240), 80, (0,0,255),3)
        
        cv2.imshow('Orig Webcam', image)
        c=cv2.waitKey(1)
        if c == 27:
            break # Esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()            
    