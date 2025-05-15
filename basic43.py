# ตรวจจับขอบภาพ Edge Detection basic43
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/noisepic.jpg",0)#อ่านภาพ
img_resize = cv2.resize(img, (450,400))#ปรับขนาดภาพ