#ตรวจจับใบหน้าและดวงตา จากภาพ basic24
import cv2

img = cv2.imread("image/myface.jpg") #อ่านภาพ
img = cv2.resize(img,(400,500))#ปรับขนาดภาพ

#อ่านไฟล์ สำหรับ classification
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")#ตรวจจับใบหน้า
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")#ตรวจจับดวงตา

#อ่านไฟล์ xml
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")#ตรวจจับใบหน้า
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")#ตรวจจับดวงตา

#ก่อนเราจะแยกใบหน้า อันดับแรกเราต้องภาพสีของเราเป็นภาพ GrayScale ก่อน
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#คือเป็นการแปลงภาพให้เป็นภาพ GrayScale โดยเก็บไว้ในตัวแปร gray_img

#ตรวจจับใบหน้า
face_detect = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=3)#ตรวจจับใบหน้า ,face_detect คือตัวแปรที่เก็บค่าของการตรวจจับใบหน้า
#,detectMultiScale คือการใช้ตรวจจับใบหน้าจากภาพ GrayScale โดยเก็บไว้ในตัวแปร face_detect ,scale_factor คือ การลดขนาดภาพ
# ,minNeighborคือ สร้างกล่องสี่เหลี่ยมที่ใบหน้าที่ใกล้เคียงที่ตวรจจับได้
    
#ตรวจจับดวงตา 
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors =2)#ตรวจจับดวงตา, eye_detect คือตัวแปรที่เก็บค่าของการตรวจจับดวงตา,
#,detectMultiScale คือการใช้ตรวจจับดวงตาจากภาพ GrayScale โดยเก็บไว้ในตัวแปร eye_detect
# ,scale_factor คือ การลดขนาดภาพ
# ,minNeighborคือ สร้างกล่องสี่เหลี่ยมที่ใบหน้าที่ใกล้เคียงที่ตวรจจับได้

#*************************
# ทำloopซ้อนloop เพื่อแสดงตำแหน่งใบหน้าและดวงตาที่ตรวจพบ 
# วนลูปในตัวแปร face_detectและ eye_detect โดยตัวแปร x,y,w,h และ a,b,c,d คือตัวแปรที่เก็บค่าของตำแหน่งใบหน้าและดวงตาไม่ให้ซ้ำกัน***

for(x,y,w,h) in eye_detect: #วนลูปเพื่อแสดงตำแหน่งดวงตาที่ตรวจพบ
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness= 5)   #แสดงตำแหน่งดวงตาที่ตรวจพบ
    for (a,b,c,d) in face_detect: #วนลูปเพื่อแสดงตำแหน่งใบหน้าที่ตรวจพบ
        cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,0),thickness= 5) #แสดงตำแหน่งใบหน้าที่ตรวจพบ
    
#แสดงภาพ
cv2.imshow("Original",img)#แสดงภาพต้นฉบับ
cv2.imshow("Result",gray_img)#แสดงภาพ GrayScale
cv2.waitKey(0)#รอปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง
#จำแนกใบหน้าจากภาพ GrayScale
