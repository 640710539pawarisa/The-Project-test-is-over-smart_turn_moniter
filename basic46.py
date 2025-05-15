#ตรวจจับขอบภาพด้วย Canny Method basic46
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/coins.jpg",0)#อ่านภาพ
img =cv2.resize(img,(500,350))#ปรับขนาดภาพ
