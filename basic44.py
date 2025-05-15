#ตรวจจับขอบภาพด้วย Laplacian Method basic44
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/coinsbritish.jpg",0)#อ่านภาพ
img =cv2.resize(img,(500,350))#ปรับขนาดภาพ

#ใช้ในการตรวจจับขอบภาพด้วย Laplacian Method
laplacian = cv2.Laplacian(img,-1)#cv2.Laplacian (array รูปภาพ, ชนืดตัวแปรในอาเรย(ใส่-1))

cv2.imshow("Original",img)#แสดงภาพ, "Original" คือชื่อภาพตัวแรก, img คือภาพที่เราอ่านมา
cv2.imshow("Laplacian",laplacian)#แสดงภาพ, "Original" คือชื่อภาพตัวแรก , "Laplacian" คือชื่อภาพตัวที่สอง

cv2.waitKey(0)#รอให้ผู้ใช้งานกดปุ่มเพื่อปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง