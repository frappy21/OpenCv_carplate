import numpy as np
import cv2
import PIL
import pytesseract
import os.path


Number_cascade = cv2.CascadeClassifier(r'.\Cascades\haarcascades\haarcascade_russian_plate_number.xml')
#cap = cv2.VideoCapture(0)
crop = 0
cropg = 0
while True:
    img = cv2.imread(r'.\img\13.jpg')
    #ret, img = cap.read()
    framecopy= img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    grayco = gray.copy()
    Number = Number_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in Number:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,20),2)

        cropg = grayco[y:y+h,x:x+w]
        cropg = cv2.resize(cropg,(300,100))

        crop = framecopy[y:y+h,x:x+w]
        crop = cv2.resize(crop,(300,100)) #x/y
    
    
    img[0:100, 0:300] = crop    #y/x

    ret,conv = cv2.threshold(cropg, 113, 255, 0)
    text = pytesseract.image_to_string(conv,"eng")
    cv2.imshow('OUT',img)
    cv2.imshow('BnW',conv)
    cv2.imshow('hui', color)
    

    if os.path.exists("./out/"+text+".jpg") != 1:
       cv2.imwrite("./out/"+text+".jpg", conv)
       print(text)


    if cv2.waitKey(1)==ord("q"):
        break

#cap.release()
cv2.destroyAllWindows()