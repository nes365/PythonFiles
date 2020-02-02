# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:49:56 2018
Same as open_webcam_basic but converts the captured image to grey
@author: Nick Southorn
"""
import cv2

def show_webcam(mirror=False):
    webcam = cv2.VideoCapture(0)
    
    while True:
        ret, image = webcam.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if mirror:
            gray = cv2.flip(gray, 1)
        cv2.imshow('My_webcam', gray)
        if cv2.waitKey(1) == 27:
            break # Esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()            
    