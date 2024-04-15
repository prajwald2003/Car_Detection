# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

# capture frames from a video
cap = cv2.VideoCapture('video1.avi')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, aaa = cap.read()
	
    # convert to gray scale of each frames

    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(aaa, 1.1, 1)
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(aaa,(x,y),(x+w,y+h),(0,255,255),5)

    # Display frames in a window
    cv2.imshow('video2', aaa)

    #Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
# De-allocate any associated memory usage
cv2.destroyAllWindows()
