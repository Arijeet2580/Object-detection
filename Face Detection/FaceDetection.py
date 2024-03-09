import cv2 as cv

face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv.imread('OpenCV/img.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)  #As This xml file works only on grayscale file
faces=face_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces : #Four Points to forming the Rectangle
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)

cv.imshow('Frames',img)
cv.waitKey(0)
cv.destroyAllWindows()
