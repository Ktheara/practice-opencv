import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (0,0), (300,400),(70,0,250),1) # start, end, color, thickness
cv2.rectangle(img,(150,50), (340, 400), (0, 250, 0), 1)
cv2.circle(img, (250, 250), 100, (250, 150, 0), 1)
cv2.putText(img, "OPENCV", (200, 450), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,150,150), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)