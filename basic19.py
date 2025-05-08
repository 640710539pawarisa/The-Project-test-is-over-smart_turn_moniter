#ตรวจจับกลุ่มวัตถุจากสี basic19

import cv2
import numpy as np

img = cv2.imread("image/RGB.png")

#ตรวจจับกลุ่มวัตถุจากสี
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0,0,0])
upper = np.array([255,255,255])

mask = cv2.inRange(img_hsv, lower, upper)

cv2.imshow("Output", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()