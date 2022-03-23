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