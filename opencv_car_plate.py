import numpy as np
import cv2
import pytesseract

Number_cascade = cv2.CascadeClassifier(r'.\Cascades\haarcascades\haarcascade_russian_plate_number.xml')
cap = cv2.VideoCapture(0)
crop = 0
cropg = 0
while True:
    #img = cv2.imread(r'.\img\14.jpg')
    ret, img = cap.read()
    framecopy= img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayco = gray.copy()
    Number = Number_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in Number:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,20),2)

        cropg = grayco[y:y+w,x:x+h]
        cropg = cv2.resize(cropg,(200,100))

        crop = framecopy[y:y+h,x:x+w]
        crop = cv2.resize(crop,(300,100)) #x/y
    img[0:100, 0:300] = crop    #y/x
    cv2.imshow('OUT',img)
    #cv2.imshow('CropGray',crop)

    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()