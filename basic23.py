#ตรวจจับดวงตาจากวีดีโอ basic23
import cv2 

cap = cv2.VideoCapture("image/nice.mp4") #อ่านวีดีโอ
#ลองวิดีโออื่น
#cap = cv2.VideoCapture("image/crying.mp4")
#cap = cv2.VideoCapture("image/ManCry.mp4")

#อ่านไฟล์ สำหรับ classification
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")#ตรวจจับดวงตา

while True:
    check, frame = cap.read()#รับภาพจากวีดีโอ frame ต่อ frame , 1 ภาพก็เป็น 1 frame
    if check == True:#ถ้าอ่านได้จะเป็น True
        #เปลี่ยนสีเป็น GrayScale
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #จำแนกใบหน้า
        eye_cascade_detect = eye_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)#scale_factor คือ การลดขนาดภาพ ,minNeighborคือ สร้างกล่องสี่เหลี่ยมที่ใบหน้าที่ใกล้เคียงที่ตวรจจับได้
        #แสดงตำแหน่งใบหน้าที่ตรวจพบ
        for (x,y,w,h) in eye_cascade_detect: 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness= 3)
            cv2.imshow("Output", frame) #แสดงภาพ
        if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:    
        break #ถ้าไม่ได้รับภาพจากวีดีโอจะ break

cap.release()#ปิดวีดีโอ
cv2.destroyAllWindows()#ปิดหน้าต่าง