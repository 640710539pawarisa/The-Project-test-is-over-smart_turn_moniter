#ตรวจจับดวงตาจากภาพนิ่ง basic22

import cv2 

img = cv2.imread("image/myface.jpg") #อ่านภาพ
img = cv2.resize(img,(400,500))#ปรับขนาดภาพ

#อ่านไฟล์ สำหรับ classification
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")#ตรวจจับดวงตา

#แสดงผลวีดีโอ
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#จำแนกดวงตาจากภาพ GrayScale
scaleFactor = 1.1
minNeighbors = 3
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbors)

#แสดงตำแหน่งดวงตาที่ตรวจพบ
for (x,y,w,h) in eye_detect: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness= 5)#แสดงตำแหน่งดวงตาที่ตรวจพบ
    
#แสดงภาพ
cv2.imshow("Original",img)#แสดงภาพต้นฉบับ
cv2.waitKey(0)#รอปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง