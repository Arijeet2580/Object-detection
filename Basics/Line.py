import cv2 as cv
import numpy as np

def click_event(event,x,y,flags,param):
    if(event == cv.EVENT_LBUTTONDOWN):
        cv.imshow('image',img)
        cv.circle(img,(x,y),3,(0,0,255),-1)
        # 3px point like -1 fills the circle with the given color
        points.append((x,y))
        if len(points)>=2:
            cv.line(img,points[-1],points[-2],(255,0,0),5)
        cv.imshow('image',img)


img=np.zeros((500,500,3),dtype="uint8")
cv.imshow('image',img)
points=[]
cv.setMouseCallback('image',click_event)

cv.waitKey(0)
cv.destroyAllWindows()

