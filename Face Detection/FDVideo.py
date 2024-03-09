import cv2 as cv

face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

capture = cv.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)  #As This xml file works only on grayscale file
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces : #Four Points to forming the Rectangle
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)
        # As Eye can be present inside Face only decreasing time to find
        eye_gray=gray[y:y+h,x:x+w]
        eye_colored=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(eye_gray)
        
        for( ex,ey,ew,eh) in eyes:
            cv.rectangle(eye_colored,(ex,ey), (ex+ew,ey+eh),(0,255,0),5)

    if ret:
        cv.imshow('video', frame)
        
        if cv.waitKey(20) & 0xFF ==ord("q"):
            break

capture.release()
cv.destroyAllWindows()
