#ตรวจจับกลุ่มวัตถุจากสี basic19

import cv2
import numpy as np

img = cv2.imread("image/rainbow_ball.jpg")


#ตรวจจับกลุ่มวัตถุจากสี   
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()