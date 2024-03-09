import cv2 as cv
import numpy as np

def click_event(event,x,y,flags,param):
    if(event == cv.EVENT_LBUTTONDOWN):
        print(x,',',y)
        font=cv.FONT_HERSHEY_SIMPLEX
        text=str(x)+','+str(y)
        cv.putText(img,text,(x,y),font,0.6,(255,0,255),2)
        cv.imshow('image',img)
    if(event == cv.EVENT_RBUTTONDOWN):
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv.FONT_HERSHEY_SIMPLEX
        text=str(blue)+','+str(green)+','+str(red)
        cv.putText(img,text,(x,y),font,0.6,(255,255,0),2)
        cv.imshow('image',img)        

img=np.zeros((500,500,3),dtype="uint8")
img =cv.imread('img.jpg')
cv.imshow('image',img)

cv.setMouseCallback('image',click_event)

cv.waitKey(0)
cv.destroyAllWindows()

