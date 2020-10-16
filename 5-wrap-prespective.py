import cv2
import numpy as np

img = cv2.imread("resource/cards.jpg")

width, height = 250, 350	#output size
pts1 = np.float32([[457,100], [600,160], [352,280], [525,370]]) #point of object edge
pts2 = np.float32([[0,0], [width,0], [0, height], [width,height]]) #new point object
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)