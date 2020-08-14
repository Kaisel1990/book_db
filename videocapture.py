import cv2
import sys
from main import *


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


Scan = True
while Scan:
    
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    decodedObjects, Scan = decode(frame)
    display(frame, decodedObjects)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
