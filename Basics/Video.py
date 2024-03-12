import cv2 as cv

capture = cv.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
	
    if not ret:  
        print('Video Ended')
        break
	
    cv.imshow('Video', frame)
    if (cv.waitKey(20) & 0xFF) == ord('q'):  
        break

capture.release()
cv.destroyAllWindows()
