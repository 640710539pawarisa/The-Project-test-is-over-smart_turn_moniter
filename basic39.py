#คอนโวลูชั่นภาพด้วย Filter2D (Convolution)basic39
import cv2
import numpy as np #ใช้สําหรับการคํานวณ หรือเอามากรองภาพเอา noise ออก
import matplotlib.pyplot as plt #ใช้สําหรับการแสดงผล

img = cv2.imread("image/noisepic.jpg",0)#อ่านภาพ
img_resize = cv2.resize(img, (450,400))#ปรับขนาดภาพ

#********
# kernel = np.ones((3,3),np.float32)/9
#ตัวกรองขนาด 3x3
#คำอธิบาย : สร้าง kernel , ใช้สําหรับการคํานวณ หรือเอามากรองภาพเอา noise ออก ,np.one คือ ขนาดของ kernel,
# np.float32 คือ ชนิดของ kernel ,/9 คือ ค่าที่ใช้ในการคํานวณ เพราะมันเป็นขนาดของ kernel เป็น 3x3

#ใช้ในการคํานวณ หรือเอามากรองภาพเอา noise ออก ขนาด 5x5
#****
# kernel = np.ones((5,5),np.float32)/25

#ใส่ filter ให้ภาพ ******ใช้ในการคํานวณ หรือเอามากรองภาพเอา noise ออก ,ตัวแปร convo เอาไว้เก็บภาพที่คํานวณแล้ว
# convo1= cv2.filter2D(img_resize,-1,kernel) 
#********
#ลองเอาค่า kernel ออกแล้ว ใส่ตตัวคำนวณภาพเพื่อเอาnoiseออกลงไปเลย  ขนาด 3x3
convo1 = cv2.filter2D(img_resize,-1,np.ones((3,3),np.float32)/9) #convo เอาไว้เก็บภาพที่คํานวณแล้ว

#ลองเอาค่า kernel ออกแล้ว ใส่ตัวคำนวณภาพเพื่อเอาnoiseออกลงไปเลย  ขนาด 5x5
convo2 = cv2.filter2D(img_resize,-1,np.ones((5,5),np.float32)/25)

#แสดงผลลัพธ์โดยเราจะนำมาเปรียบเทียบกับภาพที่เราอ่านมาหรือภาพต้นฉบับ โดยจะสร้างlistขี้นมา2ก้อนเพื่อเก็บผลลัพธ์และหัวข้อของผลลัพธ์
title = ["ORIGINAL","CONVOLUTION 3x3","CONVOLUTION 5x5"]
images = [img_resize,convo1,convo2]

#สร้าง for loop เพื่อวนลูปแสดงผล
for i in range(len(images)):#range คือการวนลูป , len คือทำซ้ำตามความยาวของ images
    plt.subplot(1,3,i+1)#plt.subplot คือการแสดงภาพในหน้าต่าง ,แสดงตำแหน่งที่ 1เป็นต้นไป ,1 คือจํานวนแถว ,3 คือจํานวนคอลัมน์ จะได้ 3 ภาพ
    plt.imshow(images[i],cmap="gray")#แสดงภาพ
    plt.title(title[i])#แสดงชื่อ
    plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
plt.show()#แสดงภาพ



