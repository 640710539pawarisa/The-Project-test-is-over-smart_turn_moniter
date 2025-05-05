#อ่านรูปภาพ  basic1

import cv2
#img คือ ตัวแปรที่สร้างไว้เก็บรูป

#ส่วนของการอ่านรูปเข้ามา
img = cv2.imread("image/Klage.jpeg") 
print(type(img.ndim)) #เช็คว่ามีกี่มิติ ใช้ .ndim , เช็คว่า ชนิดอะไร ใช้ .dtype หรือ print(type(img)) 
print(img)

#ต่อมาส่วนของแสดงรูปภาพ

