import cv2
import numpy as np

img = cv2.imread("resource/rgb-model.jpg")

print(img.shape)

imgResize = cv2.resize(img,(500, 400)) #width, height
imgCrop = imgResize[0:300, 100:400] #height, width (y1:y2, x1:x2)

#cv2.imshow("original",img)
cv2.imshow("resized", imgResize)
cv2.imshow("cropped", imgCrop)
cv2.waitKey(0)
