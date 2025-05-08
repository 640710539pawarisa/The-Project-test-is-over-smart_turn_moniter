#ตรวจจับใบหน้าจากวีดีโอ basic21

import cv2#เรียกใช้ cv2

import numpy #เรียกใช้ numpy

cap = cv2.VideoCapture(0) #เปิดกล้อง
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#ตรวจจับใบหน้า