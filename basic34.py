#Mophological basic34

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/coins.jpg",0)#อ่านภาพ
thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)#ใช้ในการแปลงภาพเป็นภาพbinary ,img คือภาพที่เราอ่านมา ,
#170 คือค่าของ thresholdหรือค่ากลางหรือค่าจุดแบ่ง ,255 คือค่าของ maximum value, cv2.THRESH_BINARY คือค่าของ thresholding method 
# ,cv2.THRESH_BINARY_INVคือ สลับพื้นหลังเป็นสีดำเป็นสีขาว สลับจากcv2.THRESH_BINARY ที่เป็นปกติก่อนสลับสี

#แสดงผลแบบ matplotlib
title = ["ORIGINAL","THRESH"] #ตัวแปร title เก็บชื่อภาพ, "ORIGINAL" คือชื่อภาพตัวแรก , "THRESH" คือชื่อภาพตัวที่สอง
images = [img,result]#เก็บภาพที่ตัวแปร images

#แสดงผล
for i in range(len(images)):#range คือการวนลูป , len คือการหาความยาวของ images
    plt.subplot(1,2,i+1)#plt.subplot คือการแสดงภาพในหน้าต่าง ,แสดงตำแหน่งที่ 1เป็นต้นไป
    plt.imshow(images[i],cmap="gray")#แสดงภาพ
    plt.title(title[i])#แสดงชื่อ
    plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
plt.show()