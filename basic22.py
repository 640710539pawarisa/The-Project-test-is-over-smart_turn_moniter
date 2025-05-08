#ตรวจจับดวงตาจากภาพ basic22

import cv2 #เรียกใช้ cv2
import numpy #เรียกใช้ numpy

img = cv2.imread("image/face.jpg") #อ่านภาพ
img=cv2.resize(img,(400,400))#ปรับขนาดภาพ