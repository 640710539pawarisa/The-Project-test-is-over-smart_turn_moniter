#Dilation Morphological basic35
import cv2
import numpy as np

img = cv2.imread("image/ballcolor.jpg")#อ่านภาพ
img=cv2.resize(img,(400,400))#ปรับขนาดภาพ