# Correct the code
import cv2 as cv

# Load cascade classifiers for face and eye detection
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Load the image and preprocess it
img = cv.imread('img/Face.jpg')
img = rescale(img, 2)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces and eyes in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    # Draw rectangle around detected face
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)
    # Extract the region of interest (ROI) for eyes within the detected face
    eye_gray = gray[y:y + h, x:x + w]
    eye_colored = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(eye_gray)
    # Draw rectangle around detected eyes
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(eye_colored, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

# Display the processed image
cv.imshow('Frames', img)
cv.waitKey(0)
cv.destroyAllWindows()

