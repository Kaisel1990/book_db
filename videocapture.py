import cv2
import sys
from BarcodeTools import *
import time


def getBookData():
    
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    maxScanTime = 5.0
    startTime = time.time() 
    Continue = True
    
    while (time.time() - startTime < maxScanTime) and (Continue == True):
        
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        bookInfo, Scan = decode(frame)
        #~ display(frame, decodedObjects)
        Continue = (bookInfo == [])
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
