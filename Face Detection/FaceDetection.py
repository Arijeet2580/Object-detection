import cv2 as cv
def rescale(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

img=cv.imread('img/face.jpg')
img=rescale(img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)  #As This xml file works only on grayscale file
faces=face_cascade.detectMultiScale(gray,1.1,4)
eyes=eye_cascade.detectMultiScale(gray,)
for(x,y,w,h) in faces : #Four Points to forming the Rectangle
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
    # As Eye can be present inside Face only decreasing time to find
    eye_gray=gray[y:y+h,x:x+w]
    eye_colored=img[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(eye_gray)
    for( ex,ey,ew,eh) in eyes:
        cv.rectangle(eye_colored,(ex,ey), (ex+ew,ey+eh),(0,255,0),5)
cv.imshow('Frames',img)
cv.waitKey(0)
cv.destroyAllWindows()
