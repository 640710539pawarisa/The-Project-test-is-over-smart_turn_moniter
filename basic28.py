#ฟังก์ชัน Thresholding basic28
import cv2 

gray_img = cv2.imread("image/gradient.jpeg")#อ่านภาพ
gray_img =cv2.resize(gray_img,(250,250))#ปรับขนาดภาพ

#ทำภาพเทาเป็นภาพขาวดำด้วย คำสั่ง cv2.threshold******

#แบบ 1 cv2.THRESH_BINARY
thresh, result1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
#อธิบายส่วนต่างๆ*************
# cv2.threshold คือฟังก์ชันที่ใช้ในการแปลงภาพเป็นภาพเทา,thresh คือดึงมาจากค่ากลางที่เราระบุเช่น 128 
#, result คือภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ binary แล้วมาเก็บในตัวแปร result 
# ,gray_img คือภาพเดิม, 128 คือค่าของ thresholdหรือค่ากลางหรือค่าจุดแบ่ง
# , 255 คือค่าของ maximum value, cv2.THRESH_BINARY คือค่าของ thresholding method
print(thresh)

#แบบ 2 cv2.THRESH_BINARY_INV
thresh, result2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)

#แบบ 3 cv2.THRESH_TRUNC
thresh, result3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)

#แบบ 4 cv2.THRESH_TOZERO
thresh, result4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)

#แบบ 5 cv2.THRESH_TOZERO_INV
thresh, result5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

#แสดงภาพ
cv2.imshow("Original",gray_img)
cv2.imshow("BINARY",result1)
cv2.imshow("BINARY_INV",result2)
cv2.imshow("TRUNC",result3)
cv2.imshow("TOZERO",result4)
cv2.imshow("TOZERO_INV",result5)
cv2.waitKey(0)#รอให้ผู้ใช้งานกดปุ่มเพื่อปิดหน้าต่าง
cv2.destroyAllWindowns()#ปิดหน้าต่าง,คืนค่าเครื่อง

