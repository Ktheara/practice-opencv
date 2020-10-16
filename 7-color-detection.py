import cv2
import numpy as np

def empty(a):
	pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 840,300)
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 255, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)

cam = cv2.VideoCapture(0) #webcam id = 0 (defualt, front webcam)
cam.set(3, 720) # width
cam.set(4, 480) # height
cam.set(10, 50) # brightness



while True:
	success, img = cam.read()
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
	h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
	s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
	s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
	v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
	v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
	print(h_min, h_max, s_min, s_max, v_min, v_max)
	#From track bar
	#lower_range = np.array([h_min, s_min, v_min])	#56, 107, 58 #RED
	#upper_range = np.array([h_max, s_max, v_max])	#179, 255, 255 #RED
	#Red detection
	lower_range = np.array([56, 107, 58])
	upper_range = np.array([179, 255, 255])
	mask = cv2.inRange(imgHSV,lower_range, upper_range)	
	imgResult = cv2.bitwise_and(img, img, mask=mask)
	cv2.imshow('Original', img)
	cv2.imshow('HSV', imgHSV)
	cv2.imshow('mask', mask)
	cv2.imshow('Result', imgResult)
	cv2.waitKey(1)