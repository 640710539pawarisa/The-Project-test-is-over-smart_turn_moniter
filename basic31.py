#ปรับค่า Threshold ด้วย Trackbar basic31
#**โดยอ้างอิงมาจากโปรแกรมแต่งภาพ photoshop ในเรื่องของ threshold คือการแปลงภาพสี เป็น ภาพbinary โดยกำหนดค่าของ threshold
#ถัดมาเราจะควบคุมค่าของ threshold Value หรือ threshold  level ด้วย trackbar หรือ slider
import cv2
def display(value):
    pass

cv2.namedWindow("Output")#สร้างหน้าต่างชื่อ Output
cv2.createTrackbar("value","Output",128,255,display)
#display คือ callback function, 128 คือค่าเริ่มต้นของ trackbar, 255 คือค่าสูงสุดของ trackbar, และค่าที่ได้จาก trackbar จะถูกส่งเข้าไปในฟังก์ชัน display

while True:
    gray_img = cv2.imread("image/ant.jpg",0)#อ่านภาพ , 0 คือแปลงภาพเป็น grayscale แล้วเก็บไว้ในตัวแปรชื่อ gray_img
    gray_img =cv2.resize(gray_img,(400,250))#ปรับขนาดภาพ
    
    #เพิ่มส่วนนี้***การใส่ค่า threshold คือการกำหนดค่า threshold value
    thresh_value = cv2.getTrackbarPos("value","Output")#ดึงค่าที่ได้จาก trackbar มาใส่ในตัวแปรชื่อ thresh_value,
    # "value" คือชื่อ trackbar, "Output" คือชื่อหน้าต่างที่อยากใช้งาน
    thresh , result = cv2.threshold(gray_img,thresh_value,255,cv2.THRESH_BINARY)#ใช้ฟังก์ชัน threshold ในการแปลงภาพเป็นภาพbinary ,
    #gray_img คือภาพที่เราอ่านมา , thresh_value คือค่าของ threshold value ที่ได้จาก trackbar, 255 คือค่าของ maximum value, 
    # cv2.THRESH_BINARY คือค่าของ thresholding method , result คือภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ binary แล้วมาเก็บในตัวแปร result,
    #,thresh เอาไว้เก็บค่า threshold value ที่เรากำหนดไว้ใน trackbar
    
    #แสดงภาพ
    if cv2.waitKey(1) &0xFF == ord("q"):
        break
    cv2.imshow("Output",result)#แสดงภาพ
    
cv2.destroyAllWindows()#ปิดหน้าต่าง,คืนค่าเครื่อง