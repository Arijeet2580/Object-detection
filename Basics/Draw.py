import cv2 as cv


def rescale(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('img/img.jpg')
img_rescaled = rescale(img)
cv.line(img_rescaled,(0,0),(255,255),(147,96,10),10)
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img_rescaled,"Mango",(147,247),font,5,(255,0,255),10)
cv.imshow('Window', img_rescaled)
cv.waitKey(0)
cv.destroyAllWindows()
