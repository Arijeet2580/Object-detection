import cv2 as cv

def rescale(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('img/img.jpg')
img= rescale(img)

cv.imshow('Window', img)
cv.waitKey(0)
cv.destroyAllWindows()
choice= input ("Do you want to see the Numpy Array of the Image:(y/n) ")
if(choice=="y"):
    print(img)