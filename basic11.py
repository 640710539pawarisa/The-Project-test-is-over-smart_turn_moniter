##วาดเส้นสี่เหลี่ยมใส่ภาพนิ่ง,วีดิโอ  basic10
import cv2 
img = cv2.imread("image/Klage.jpeg")#อ่านภาพเข้ามา

#กำหนดขนาดภาพ
imgresize = cv2.resize(img, (700,700))#ความกว้าง,ความสูง

#วาดเส้นสี่เหลี่ยม
#rectangle (ภาพ , จุดเริ่มต้น(x , y) , จุดสิ้นสุด(x , y) , สี (BGR), ความหนา) #สีเป็น BGR คือ blue , green , red
