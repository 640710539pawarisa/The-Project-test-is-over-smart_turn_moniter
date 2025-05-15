#ตรวจจับขอบภาพด้วย Sobel Method basic44

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/coins.jpg",0)#อ่านภาพ
img =cv2.resize(img,(500,350))#ปรับขนาดภาพ