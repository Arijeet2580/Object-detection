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

print("Click Esc to Close the Window")
while(1):
    cv.imshow('image',img)
    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    r=cv.getTrackbarPos('R','image')
    s=cv.getTrackbarPos('Switch','image')

    if(s==0):
        img[:]=0
    else:
        img[:]=[b,g,r]

    k = cv.waitKey(1) 
    if k == 27:  # Esc key
        break

cv.destroyAllWindows
