#การสร้าง color Trackbar เบื้องต้น basic26

import cv2#เรียกใช้ cv2

import numpy #เรียกใช้ numpy

img = cv2.imread("image/Klage.jpeg") #อ่านภาพ
# img = numpy.zeros([500,500,3], numpy.uint8)#สร้างภาพขึ้นมาเองโดยไม่อ่านภาพอื่นเข้ามา (ลองทำ)