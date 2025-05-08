#ตรวจจับดวงตาจากวีดีโอ basic23

import cv2 #เรียกใช้ cv2
import dlib #เรียกใช้ dlib
import numpy as np #เรียกใช้ numpy

cap = cv2.VideoCapture(0) #เปิดกล้อง