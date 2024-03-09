import cv2 as cv

capture = cv.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    
    if ret:
        cv.imshow('video', frame)
        
        if cv.waitKey(20) & 0xFF ==ord("q"):
            break

capture.release()
cv.destroyAllWindows()
