#ตรวจจับใบหน้าจากวีดีโอ basic21

import cv2 #เรียกใช้ cv2
cap = cv2.VideoCapture("image/Rap_battle.mp4") #อ่านวีดีโอ

#นำคำสั่งจาก basic20 เพื่อตรวจจับใบหน้าจากภาพ
#อ่านไฟล์ สำหรับ classification
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")#ตรวจจับใบหน้า

#แสดงผลวีดีโอ
while (cap.isOpened()): #ใช้ while เพื่อให้หน้าต่างไม่ปิดอัตโนมัติ 
    check, frame = cap.read() #อ่านภาพจากวีดีโอ frame ต่อ frame , 1 ภาพก็เป็น 1 frame
    if check == True:
        #ถ้าอ่านได้จะเป็น True 
        #ต้องทำเป็นภาพ GrayScale เพื่อใช้ในการตรวจจับใบหน้า
        gray_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)#แปลงภาพจาก BGR เป็น GrayScale เพื่อใช้ในการตรวจจับใบหน้า ,frame คือภาพสี
        #จำแนกใบหน้า
        face_detect = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5) #ตรวจจับใบหน้า ,face_detect คือตัวแปรที่เก็บค่าของการตรวจจับใบหน้า
        #,face_cascade.detectMultiScale คือการใช้ตรวจจับใบหน้าจากภาพ GrayScale โดยเก็บไว้ในตัวแปร face_cascade ,scale_factor คือ การลดขนาดภาพ ,minNeighborคือ สร้างกล่องสี่เหลี่ยมที่ใบหน้าที่ใกล้เคียงที่ตวรจจับได้
        for (x, y, w, h) in face_detect: #วนลูปเพื่อแสดงตำแหน่งใบหน้าที่ตรวจพบ
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),thickness= 5) #แสดงตำแหน่งใบหน้าที่ตรวจพบ
            cv2.imshow("Output", frame) #แสดงภาพ
        if cv2.waitKey(1) & 0xFF == ord("q"): #ถ้ากด q ให้หน้าต่างปิดอัตโนมัติ
            break
    else:
        break
    
cap.release()#ปิดวีดีโอ
cv2.destroyAllWindows()#ปิดหน้าต่าง