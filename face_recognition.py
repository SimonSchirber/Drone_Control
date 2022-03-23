import cv2
import numpy as np
from djitellopy import tello

drone = tello.Tello()
drone.connect()
drone.streamon()

cap = cv2.VideoCapture(0)
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0
w,h, = 360, 240

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/face_rec.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []

    for (x,y,w,h) in faces:
        rect = cv2.rectangle(img,(x,y), (x+w, y+h), (36,255,12), 2)
        cv2.putText(rect, 'Simon', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 1)
        
        cx = x + w //2
        cy = y + h //2
        area = w *h
        cv2.circle(img, (cx,cy), 5, (36,255,12), cv2.FILLED )
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    #check if empty/no one in fram
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0,0], 0]

def trackFace (drone, info, w, pid, pError):
    area = info[1]
    x,y = info[0]
    fb = 0
    ## how far away object is from center
    error = x-w//2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100,100))


    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20
    #drone.send_rc_control(0, fb, 0, speed)
    
    if x == 0:
        speed = 0
        error = 0
    
    return error

while True:
    _, img = cap.read()
    #img = cv2.resize(img, (w,h))
    img, info = findFace(img)
    pError = trackFace(None, info, w, pid, pError)
    cv2.imshow("Output", img)
    cv2.waitKey(1)