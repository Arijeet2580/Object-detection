import cv2 as cv
import numpy as np

def rescale(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('img.jpg')
img= rescale(img)
print(img)

cv.imshow('Window', img)
cv.waitKey(0)
cv.destroyAllWindows()
