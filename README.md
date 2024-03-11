# Object-detection

### Applied  Haar Cascade Classifier: 
Haar Cascade is a feature-based object detection algorithm used to identify objects within images.
It relies on Haar-like features and employs a cascade classifier comprising multiple stages, each containing weak learners trained on positive and negative images. 

This machine learning approach facilitates the detection of objects by analyzing image features and patterns.

```
face=cv.CascadeClassifier('Data.xml')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)  
faces=face_cascade.detectMultiScale(gray,1.1,4)
# faces=face.detectMultiScale(image,scaleFactor,minNeighbours)
```
1. DetectMultiScale() Function takes Gray Image , scaleFactor and MinNeighbours

- Gray takes the Gray Scale Image that can be changed using cvtColor function that changes BGR image to GrayScale Image.

- (1.1)ScaleFactor specifies how much Image size is reduced at each Image scale

- (4)MinNeighbours specifies how many neighbours each candidate rectangle should be retained.



### The Code developed is general to be used with any classifiers:
Ease with Adaptability with the Plastic Data model from the Project of the Face Detection


1. The Above code is flexible to be used with any classifier with Little bit Modification.
	
2. Working on Image contours for Further Improvisation of the Data Model 

## Basic Problems and Solutions that can be faced by Beginners


### Reading Images

```
img=cv.imread('image/path.jpg')
```

- It allows to read Images from file path as Arguements
- If Image loading is Succesful returns a Numpy Array
- If Image loading is Unsuccesful returns none

```
cv.imshow('Window',img)
```

- Used to Display an Image in a window.
- Takes Arguement Window name and image to be displayed


```
	cv.waitKey(0)
	k=cv.waitKey(0) & 0xFF 
	if (k== ord('d')){
		break
	}
	cv.destroyAllWindows()
```


- "0" arguement represents infinite delay
- Makes window to be remain open until the user presses any key
- returns ASCII code it can be made so that when clicked the specified key it will move to next Line
- ord('d') returns ASCII Code of the character 'd'
- Destroy Function deletes or closes all the Window Present.


### Reading Video

```
capture=cv.VideoCapture('path.mp4')
while capture.isOpened():
	isTrue,frame = capture.read()
	cv.imshow('Video',frame)
	if(cv.waitKey(0) & 0xFF == ord('q'))
		break
capture.release()
cv.destroyAllWindows()
```

- VideoCapture function takes the Arguement as Video Path or 0 that means reference to Laptop Webcam
- isOpened returns True if Reference is taken properly
- Reads the Video in Small bits of Image in While loop till its True
- Stops the Video Display when the Ord('q') is clicked

* Problem :
1. Gives -215 Assertion Error, It means it ran out of the Frames from the Video 
	To Solve this:
```
	if  not isTrue is none:
		print('Video Ended')
		break
	cv.imshow('Video',frame)
	if(cv.waitKey(20) & 0xFF == ord('q')):
		break
	
```	
### Resizing and Rescaling Frames

1. Frame.shape[1] = Actual Width of the Frame
2. Frame.shape[0] = Actual height of the Frame

```
	def rescale(frame,scale):
		width=int(frame.shape[1]*scale)
		height=int(frame.shape[0]*scale)
		dimensions=(width,height)
		return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
```

1. resize Function takes arguement for frames, dimensions in tuples and Interpolation(Optional Arguement) used to construct new data points within the range of tje discrete set of Known data points

2. cv.INTER_AREA: Refers to resampling using pixel Area relation




### Problem:
Stuck in Finding useful pre-trained haar cascade model for the Plastic Detection
If we are  to go for Custom trained Model it will take a huge data barrier to pass on  Because without a vast amount of data needed it will not be useful for proper detection.

GitHub Link : Added all my projects done in Object Detection in One Link From Basic Project to the General Haar Cascade Project done on Face detection which Can be further modified to set as a General Object Detection Model

GitHub Link: https://github.com/Arijeet2580/Object-detection



### References
1. https://medium.com/@vipulgote4/guide-to-make-custom-haar-cascade-xml-file-for-object-detection-with-opencv-6932e22c3f0e
2. https://stackoverflow.com/questions/2000816/how-to-create-haar-cascade-xml-file-to-use-in-opencv
3. https://johnallen.github.io/opencv-object-detection-tutorial/
4. https://machinelearningmastery.com/training-a-haar-cascade-object-detector-in-opencv/
5. https://www.analyticsvidhya.com/blog/2022/04/object-detection-using-haar-cascade-opencv/
6. https://github.com/opencv/opencv/tree/4.x/data/haarcascades
7. https://github.com/benjamrio/sort-it/blob/main/detection/haarcascade_detection.py


