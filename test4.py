from __future__ import print_function
import cv2 as cv
import argparse

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

   # faces = face_cascade.detectMultiScale(frame_gray)
   # body = body_cascade.detectMultiScale(frame_gray)
    #upper = upper_cascade.detectMultiScale(frame_gray)
    lower = lower_cascade.detectMultiScale(frame_gray)
   # for(x,y,w,h) in body:
    #    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
   # for(x2,y2,w2,h2) in upper:
       #  cv.rectangle(frame,(x2,y2),(x2+w2,y2+h2),(0,255,255),2)
    for(x3,y3,w3,h3) in lower:
         cv.rectangle(frame,(x3,y3),(x3+w3,y3+h3),(0,255,255),2)
   # for(x,y,w,h) in faces:
      #  center = (x +w//2, y + h//2)
     #   frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

    #    faceROI = frame_gray[y:y+h,x:x+h]

     #   eyes = eyes_cascade.detectMultiScale(faceROI)
     #   for(x2,y2,w2,h2) in eyes:
     #       eye_center = (x+x2+w2//2, y+y2+h2//2)
       #     radius = int(round((w2+h2)*0.25))
       #     frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)       

    cv.imshow('Capture - Face detection', frame)

#face_cascade = cv.CascadeClassifier()
#eyes_cascade = cv.CascadeClassifier()
#body_cascade = cv.CascadeClassifier()
#upper_cascade = cv.CascadeClassifier()
lower_cascade = cv.CascadeClassifier()

#if not upper_cascade.load(cv.samples.findFile('/opencv/haarcascade_upperbody.xml')):
    #print('--(!)Error loading upper cascade')
   # exit(0)
if not lower_cascade.load(cv.samples.findFile('/opencv/haarcascade_lowerbody.xml')):
    print('--(!)Error loading lower cascade')
    exit(0)
#if not body_cascade.load(cv.samples.findFile('/opencv/haarcascade_fullbody.xml')):
 #  print('--()Error loading body cascade')
  #  exit(0)
# if not face_cascade.load(cv.samples.findFile('/opencv/haarcascade_frontalface_alt.xml')):
#    print('--(!)Error loading face cascade')
#    exit(0)
# if not eyes_cascade.load(cv.samples.findFile('/opencv/haarcascade_eye_tree_eyeglasses.xml')):
#    print('--(!)Error loading eyes cascade')
#    exit(0)

cap = cv.VideoCapture(0)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break

    detectAndDisplay(frame)

    if cv.waitKey(1) == 27:
        break

