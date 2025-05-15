#ตรวจจับขอบภาพด้วย Sobel Method basic43
import cv2 #เรียกใช้ cv2
import matplotlib.pyplot as plt #เรียกใช้ matplotlib
import numpy as np

img = cv2.imread("image/coinsbritish.jpg",0)#อ่านภาพ
img = cv2.resize(img,(700,450))#ปรับขนาดภาพ

#ใช้ในการตรวจจับขอบภาพด้วย Sobel Method
#แนวแกน x หรือแนวนอน
sobalx = cv2.Sobel(img,-1,1,0,ksize=3) #cv2.Sobel (array รูปภาพ, ชนืดตัวแปรในอาเรย(ใส่-1),ขนาดตัวกรองแกน x,ขนาดตัวกรองแกน y)

#แนวแกน y หรือแนวตั้ง
sobaly = cv2.Sobel(img,-1,0,1,ksize=3)

#รวมแนวแกน x และ y 
sobelxy = cv2.bitwise_or(sobalx,sobaly)  #ใช้ bitwise_or เพื่อรวมแนวแกน x และ y

#แสดงภาพ
image = [img,sobalx,sobaly,sobelxy]
title = ["Original","Sobel X","Sobel Y","Sobel XY"]

for i in range(len(image)):#range คือการวนลูป , len คือการหาความยาวของ images
    plt.subplot(2,2,i+1)#plt.subplot คือการแสดงภาพในหน้าต่าง ,แสดงตำแหน่งที่ 1เป็นต้นไป,2 คือจํานวนแถว ,3 คือจํานวนคอลัมน์ จะได้ 4 ภาพ
    plt.imshow(image[i],cmap="gray")#แสดงภาพ
    plt.title(title[i])#แสดงชื่อ
    plt.xticks([])#ไม่แสดงตัวแปร x
    plt.yticks([])#ไม่แสดงตัวแปร y

plt.show()#แสดงภาพ