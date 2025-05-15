#ตรวจจับขอบภาพด้วย Canny Method  ** ได้รับความนิยมมาก basic45
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/coinsbritish.jpg",0)#อ่านภาพ
img =cv2.resize(img,(700,550))#ปรับขนาดภาพ

#ใช้ในการตรวจจับขอบภาพด้วย Canny Method
canny = cv2.Canny(img,100,200)
#cv2.Canny (array รูปภาพ,ค่าของ threshold1,ค่าของ threshold2) ,ค่า threshold1 คือค่าของขอบภาพแรก ,ค่า threshold2 คือค่าของขอบภาพที่สอง
#ค่า threshold1,2 เราจะกำหนดเอง

cv2.imshow("Original",img)#แสดงภาพ, "Original" คือชื่อภาพตัวแรก, img คือภาพที่เราอ่านมา
cv2.imshow("Canny",canny)#แสดงภาพ, "Original" คือชื่อภาพตัวแรก , "Canny" คือชื่อภาพตัวที่สอง

cv2.waitKey(0)#รอให้ผู้ใช้งานกดปุ่มเพื่อปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง