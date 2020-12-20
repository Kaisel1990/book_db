import cv2
import sys
from BarcodeTools import *
import time


def getBookData():
    
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    maxScanTime = 7.0
    startTime = time.time() 
    Continue = True
    
    while (time.time() - startTime < maxScanTime) and (Continue == True):
        
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        
        bookInfo, Scan = decode(frame)
        Continue = (bookInfo == [])
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
    return bookInfo

def getBookDataISBN(ISBN):
	
	bookInfo = getDataFromISBN(ISBN)
	
	return bookInfo
