import numpy as np
import cv2

Number_cascade = cv2.CascadeClassifier(r'C:\Users\Frappy\Documents\python\Cascades\haarcascades\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
crop = 0
cropg = 0
while True:
    
    ret, img = cap.read()
    framecopy= img.copy()
    xzx = (10)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayco = gray.copy()
    Number = Number_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in Number:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,20),2)

        cropg = grayco[y:y+w,x:x+h]
        cropg = cv2.resize(cropg,(128,128))

        crop = framecopy[y:y+w,x:x+h]
        crop = cv2.resize(crop,(128,128))
    img[0:128, 0:128] = crop

    cv2.imwrite(r'C:\Users\Frappy\Documents\python\img.jpg', cropg)

    cv2.imshow('OUT',img)
    cv2.imshow('CropGray',cropg)

    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()