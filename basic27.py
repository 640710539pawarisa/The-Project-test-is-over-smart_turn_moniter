#แสดงผลภาพด้วย Matplotlib basic27

import cv2#เรียกใช้ cv2 
#แสดงผลภาพด้วย Matplotlib
import matplotlib.pyplot as plt #เรียกใช้ matplotlib ที่ตั้งชื่อว่า plt
img = cv2.imread("image/Klage.jpeg")#อ่านภาพ

#แสดงภาพแบบ OpenCV
cv2.imshow("Output", img)#Output คือชื่อหน้าต่าง,img คือชื่อภาพของเรา

#แปลง channel สี จาก BGR เป็น RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#แสดงภาพแบบ Matplotlib
plt.imshow(img)
plt.show()


#สรุป*****
#การแสดงผลภาพในหน้าต่างด้วย OpenCV จะแสดงสีด้วย BGR
#การแสดงผลภาพในหน้าต่างด้วย Matplotlib จะแสดงสีด้วย RGB 
#เราเลยต้องมีการสลับchannelสีก่อน 