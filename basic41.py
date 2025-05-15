#Median Filter ตัวกรองค่ามัธยฐาน basic41
import cv2
import numpy as np #ใช้สําหรับการคํานวณ หรือเอามากรองภาพเอา noise ออก
import matplotlib.pyplot as plt #ใช้สําหรับการแสดงผล

#ภาพต้นฉบับ Original
img = cv2.imread("image/noisepic.jpg",0)#อ่านภาพ
img_resize = cv2.resize(img, (450,400))#ปรับขนาดภาพ

#เอา basic 39  ,basic 40 มาต่อยอด****

#แบบ filter
#ลองเอาค่า kernel ออกแล้ว ใส่ตัวคำนวณภาพเพื่อเอาnoiseออกลงไปเลย  ขนาด 5x5
filter2d = cv2.filter2D(img_resize,-1,np.ones((5,5),np.float32)/25)

#แบบ blur เราจะไม่ต้องเขียน ,np.ones((5,5),np.float32)/25
mean = cv2.blur(img_resize,(5,5)) #.blur คือตัวกรองค่าเฉลี่ย ,img_resize คือรูปภาพของเรา,(5,5) คือขนาดของ kernel แล้วมาเก็บในตัวแปร ชื่อว่า mean

#เพิ่มส่วนนี้***
#แบบ Median 
median_blur = cv2.medianBlur(img_resize,5)#medianBlur คือตัวกรองค่ามัธยฐาน ,img_resize คือรูปภาพของเรา,5 คือขนาดของ kernel

#แสดงผลลัพธ์โดยเราจะนำมาเปรียบเทียบกับภาพที่เราอ่านมาหรือภาพต้นฉบับ โดยจะสร้างlistขี้นมา2ก้อนเพื่อเก็บผลลัพธ์และหัวข้อของผลลัพธ์
title = ["ORIGINAL","FILTER2D","MEAN","MEDIAN BLUR"]
images = [img_resize,filter2d,mean,median_blur]

#สร้าง for loop เพื่อวนลูปแสดงผล
for i in range(len(images)):#range คือการวนลูป , len คือทำซ้ำตามความยาวของ images
    plt.subplot(2,2,i+1)#plt.subplot คือการแสดงภาพในหน้าต่าง ,แสดงตำแหน่งที่ 1เป็นต้นไป ,2 คือจํานวนแถว ,2 คือจํานวนคอลัมน์ จะได้ 4 ภาพ
    plt.imshow(images[i],cmap="gray")#แสดงภาพ
    plt.title(title[i])#แสดงชื่อ
    plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
plt.show()#แสดงภาพ

#ข้อเสียคือ ยิ่งใช้ขนาดตัวกรองใหญ่มากยิ่งเบลอมาก