# Object-detection

### Applied  Haar Cascade Classifier: 
Haar Cascade is a feature-based object detection algorithm used to identify objects within images.
It relies on Haar-like features and employs a cascade classifier comprising multiple stages, each containing weak learners trained on positive and negative images. 

This machine learning approach facilitates the detection of objects by analyzing image features and patterns.


### The Code developed is general to be used with any classifiers:
Ease with Adaptability with the Plastic Data model from the Project of the Face Detection


1. The Above code is flexible to be used with any classifier with Little bit Modification.
	
2. Working on Image contours for Further Improvisation of the Data Model 

<code>
	img=cv.imread('image/path.jpg')
</code>
- It allows to read Images from file path as Arguement
- If Image loading is Succesful returns a Numpy Array
- If Image loading is Unsuccesful returns none

<code>
	cv.imshow('Window',img)
</code>

- Used to Display an Image in a window.
- Takes Arguement Window name and image to be displayed
  

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


