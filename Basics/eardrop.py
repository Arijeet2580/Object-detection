import cv2 as cv
import numpy as np

def click_event(event,x,y,flags,param):
    if(event == cv.EVENT_LBUTTONDOWN):
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv.circle(img,(x,y),3,(0,255,0),-1)
        colorImage=np.zeros((512,512,3),dtype="uint8")
        colorImage[:]=blue,green,red
        cv.imshow('color',colorImage)

img=np.zeros((500,500,3),dtype="uint8")
cv.imshow('image',img)
points=[]
cv.setMouseCallback('image',click_event)

cv.waitKey(0)
cv.destroyAllWindows()

