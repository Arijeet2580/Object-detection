import cv2 as cv
import datetime 
cap = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
"""
cap.set(cv.CAP_PROP_FRAME_WIDTH, 3000) Updates the Width to fit the given Resolution
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 300)

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

"""
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(cv.CAP_PROP_FRAME_WIDTH)) + ' Height: ' + str(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        date=str(datetime.datetime.now())
        frame = cv.putText(frame,"Click q to stop Recording",(10,25),font,0.6,(0,255,255),2,cv.LINE_AA)
        frame = cv.putText(frame, text, (10, 50), font, 0.6, (0, 255, 255), 2, cv.LINE_AA)
        frame = cv.putText(frame, date, (10, 75), font, 0.6, (0, 255, 255), 2, cv.LINE_AA)
        cv.imshow('frame', frame)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
