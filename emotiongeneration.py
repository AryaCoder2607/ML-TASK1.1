import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from deepface import DeepFace

faceCascade=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')#detects face ,non machine learning
cam=cv.VideoCapture(0)#webcam

while True:
    check, frame = cam.read()#stores frame
    ret,frame=cam.read()#reads the frame 
    result=DeepFace.analyze(frame,actions=['emotion'])#analyzes your face
    img = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    faces=faceCascade.detectMultiScale(img,1.1,4)   
    for(x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    font = cv.FONT_HERSHEY_SIMPLEX   
    cv.putText(img,result['dominant_emotion'],(50,70),font,3,(255,0,0),2,cv.LINE_4)
   
    cv.imshow('video', img)
    if cv.waitKey(1)& 0xFF==ord('q'):
        break

   
cam.release()

cv.destroyAllWindows()