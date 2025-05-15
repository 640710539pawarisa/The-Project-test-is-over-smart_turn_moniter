#Gaussian Filter ตัวกรองเกาส์เซียน basic42
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame,(5,5),0)
    cv2.imshow("Output",frame)