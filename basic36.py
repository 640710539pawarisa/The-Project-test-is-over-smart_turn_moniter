#Erosion Morphological (การลดขนาดพื้นที่ หรือ การกร่อนภาพ) basic36
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image/coins2.jpg",0)#อ่านภาพ
img=cv2.resize(img,(400,400))#ปรับขนาดภาพ

thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)#ใช้ในการแปลงภาพเป็นภาพbinary ,img คือภาพที่เราอ่านมา 
#,result เอาไว้เก็บภาพที่แปลงเป็นภาพbinary,thresh เอาไว้เก็บค่า threshold value 

#สร้างกลุ่มเลข 1 
#เพิ่มส่วนนี้ ***การขยายพื้นที่ 
#ตัวกรองข้อมูล ใช้ในการขยายพื้นที่ เช่นสร้างกลุ่มเลข 1 ขนาด 5x5
kernel = np.ones((5,5),np.uint8)#สร้าง kernel , ใช้สําหรับการขยายพื้นที่, ตัวเลขในอาเรย์คือ ขนาดของ kernel, np.uint8 คือ ชนิดของ kernel

#การขยายภาพ
dilation = cv2.dilate(result,kernel,iterations=2)#ใช้ในการขยายพื้นที่, img คือภาพที่เราอ่านมา,dilation เอาไว้เก็บภาพที่ขยายพื้นที่แล้ว,
#kernel คือ kernel ที่ใช้ในการขยายพื้นที่, 2 คือจํานวนที่ใช้ในการขยายพื้นที่ หรือทำซ้ำ 2รอบ ,กรอง2 รอบ

#การกร่อนภาพ*******เพิ่มส่วนนี้
erosion = cv2.erode(result,kernel,iterations=5)#ใช้ในการกร่อนภาพ, img คือภาพที่เราอ่านมา,erosion เอาไว้เก็บภาพที่กร่อนแล้ว,
#kernel คือ kernel ที่ใช้ในการกร่อนภาพ, 5 คือจํานวนที่ใช้ในการกร่อนภาพ หรือทำซ้ำ 7รอบ

#เพิ่ม***ในส่วนของ การกร่อนภาพเข้าไปด้วย 
title = ["ORIGINAL","THRESH","DILATION","EROSION"]#ตัวแปร title เก็บชื่อภาพ, "Original" คือชื่อภาพตัวแรก , "Dilation" คือชื่อภาพตัวที่สอง
images = [img,result,dilation,erosion]#เก็บภาพที่ตัวแปร images, img คือภาพที่เราอ่านมา, img_dilation คือภาพที่เราขยายพื้นที่แล้ว

for i in range(len(images)):#range คือการวนลูป , len คือการหาความยาวของ images
    plt.subplot(2,2,i+1)#plt.subplot คือการแสดงภาพในหน้าต่าง ,แสดงตำแหน่งที่ 1เป็นต้นไป ,2 คือจํานวนแถว ,2 คือจํานวนคอลัมน์ จะได้ 4 ภาพพอดี
    plt.imshow(images[i],cmap="gray")#แสดงภาพ
    plt.title(title[i])#แสดงชื่อ
    plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
plt.show()#แสดงภาพ