#Mean Filter ตัวกรองค่าเฉลี่ย basic40
import cv2
import numpy as np #ใช้สําหรับการคํานวณ หรือเอามากรองภาพเอา noise ออก
import matplotlib.pyplot as plt #ใช้สําหรับการแสดงผล

img = cv2.imread("image/noisepic.jpg",0)#อ่านภาพ
img_resize = cv2.resize(img, (450,400))#ปรับขนาดภาพ