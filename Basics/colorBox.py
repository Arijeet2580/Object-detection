import numpy as np
import cv2 as cv

def func(x):
    print(x)

img=np.zeros((500,500,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B','image',0,255,func)
cv.createTrackbar('G','image',0,255,func)
cv.createTrackbar('R','image',0,255,func)
cv.createTrackbar('Switch','image',0,1,func)

while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF
    if(k==32):   #Click space to Escape
        break
    
    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    r=cv.getTrackbarPos('R','image')
    s=cv.getTrackbarPos('Switch','image')

    if(s==0):
        img[:]=0
    else:
        img[:]=[b,g,r]

cv.destroyAllWindows
