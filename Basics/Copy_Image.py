import cv2  as cv
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv.FONT_HERSHEY_SIMPLEX
        text = str(y) + ',' + str(x)          # As the Value given is in y,x not x,y
        cv.putText(img, text, (x, y), font, 0.6, (255, 0, 255), 2)
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ',' + str(green) + ',' + str(red)
        cv.putText(img, text, (x, y), font, 0.6, (255, 255, 0), 2)
        cv.imshow('image', img)


def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('img.jpg')
img = rescale(img)

a=input("Enter y if you want to copy")
if a=='y':
    tv= img[540:648,257:333]
    img[289:397,134:210] = tv

cv.imshow("image", img)

cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()