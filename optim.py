
import cv2
import PIL


Number_cascade = cv2.CascadeClassifier(r'.\Cascades\haarcascades\haarcascade_russian_plate_number.xml')
#cap = cv2.VideoCapture(0)
crop = 0
cropg = 0
while True:
    img = cv2.imread(r'.\img\13.jpg')
    back = cv2.imread(r'.\img\back.jpg')
    #ret, img = cap.read()
    framecopy= img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    grayco = gray.copy()
    Number = Number_cascade.detectMultiScale(gray, 1.3, 5)



    for (x,y,w,h) in Number:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)

        cropg = grayco[y:y+h,x:x+w]
        cropg = cv2.resize(cropg,(300,100))

        crop = framecopy[y:y+h,x:x+w]
        crop = cv2.resize(crop,(300,100)) #x/y
    
    
    img[0:100, 0:300] = crop    #y/x

    ret,conv = cv2.threshold(cropg, 113, 255, 0)
    

    #resized = cv2.resize(img,(900,599))
    resized = cv2.resize(img,(800,532))


    #back[0:599, 250:1150] = resized
    back[0:532, 0:800] = resized
    cv2.putText(back, "some shitty text like speed or another))", (220, 550),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 255, 255), 1) 



    #cv2.imshow('OUT',img) #original size
    cv2.imshow('B&W',conv) #black n white plate only
    #cv2.imshow('color', color) #some shit
    #cv2.imshow('res', resized) #cropped
    cv2.imshow('black', back)
    if cv2.waitKey(1)==ord("q"):
        break

#cap.release()
cv2.destroyAllWindows()