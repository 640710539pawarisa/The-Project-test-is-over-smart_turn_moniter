#การใช้งาน Adaptive Threshlod หรือ  Adaptive Thresholding ** มันคือ thresholding อีกประเภทนึง basic32
import cv2 

img = cv2.imread("image/map2.jpg",0)#อ่านภาพ
img =cv2.resize(img,(500,350))#ปรับขนาดภาพ

#แบบแรก
thresh , result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)#ใช้ฟังก์ชัน threshold ในการแปลงภาพเป็นภาพbinary,
#img คือภาพที่เราอ่านมา , 128 คือค่าของ thresholdหรือค่ากลางหรือค่าจุดแบ่ง
# , 255 คือค่าของ maximum value, cv2.THRESH_BINARY คือค่าของ thresholding method,thresh เอาไว้เก็บค่า threshold value หรือค่ากลาง


#แบบสอง
#Adaptive Mean
result2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
#ใช้ฟังก์ชัน adaptive threshold ในการแปลงภาพเป็นภาพbinary,
#img คือภาพที่เราอ่านมา , 255 คือค่าของ maximum value, cv2.ADAPTIVE_THRESH_MEAN_C คือค่าของ adaptive thresholding method
# , cv2.THRESH_BINARY คือค่าของ thresholding type เราเลือกแบบ binary , 3 คือค่าของ block size,  1 คือค่าของ constant 
#***ผลลัพธ์ที่เกิดขึ้นหลังใช้ Adaptive Thresholding เราจะเอามาเก็บในตัวแปร result2 

#ลองทำ adaptive thresholding แบบอื่นๆ
#แบบ Adaptive Gaussian
result3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow("THRESH",result)#แสดงภาพ
cv2.imshow("MEAN",result2)#แสดงภาพ
cv2.imshow("GAUSSIAN",result3)#แสดงภาพ
cv2.waitKey(0)#รอให้กดปุ่ม
cv2.destroyAllWindows()#ปิดหน้าต่าง

