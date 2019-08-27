# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:49:56 2018
Basic opening of webcam.
Esc to exit
@author: Nick Southorn
"""

import cv2

def show_webcam(mirror=False):
    webcam = cv2.VideoCapture(0)
    while True:
        ret, image = webcam.read()
        if mirror:
            image = cv2.flip(image, 1)
        cv2.imshow('My_webcam', image)
        if cv2.waitKey(1) == 27:
            break # Esc to quit
        if  cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.imshow('My_webcam', image)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image,'OpenCV Demo',(10,50), font, 2,(255,255,255),2,cv2.LINE_AA)
                
            
    cv2.destroyAllWindows()



def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()            
    