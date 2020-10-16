import cv2

#read image
#img = cv2.imread("resource/blurred.png") # read image
#cv2.imshow("image", img)
#cv2.waitKey(0)

#read video
#cap = cv2.VideoCapture("resource/video.mp4")
#while True:
#	success, img = cap.read()
#	cv2.imshow("Video", img)
#	if cv2.waitKey(1) & 0xFF == ord('q'):
#		break

#read webcam
cam = cv2.VideoCapture(0) #webcam id = 0 (defualt, front webcam)
cam.set(3, 640) # width
cam.set(4, 480) # height
cam.set(10, 50) # brightness
while True:
	success, img = cam.read()
	cv2.imshow("Video", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break