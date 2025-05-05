#แสดงวันเวลาในกล้อง/วิดีโอ  basic14
import cv2 #เรียกใช้งาน opencv
import datetime #เช็ควันเวลา

#ระหว่างการเปิดกล้อง/วิดีโอ ต้องเปิดเลือกทำอย่างใดอย่างหนึ่ง แล้วใส่ชื่อวีดีโอ และมันจะแสดงวันเวลาในหน้าต่าง
#เปิดวีดีโอ
cap = cv2.VideoCapture("image/videotestt.mp4") #เปิดวีดีโอ

#เปิดกล้อง
cap = cv2.VideoCapture(2)

while (cap.isOpened()):#เปิดกล้อง
    check, frame = cap.read() #อ่านภาพจากกล้อง frame ต่อ frame , 1 ภาพก็เป็น 1 frame 
    #check คือเช็คว่าอ่านภาพได้ไหม ,ถ้าไม่อ่านได้จะเป็น False ,frame คือภาพ แล้วใส่ชื่อวีดีโอ
    if check == True:
        currrntDate = str(datetime.datetime.now()) #เช็ควันเวลา , currrntDate คือตัวแปรที่เก็บวันเวลาปัจจุบัน 
        #str คือการแปลงเป็นข้อความ ,datetime.datetime.now() คือวันเวลาปัจจุบัน
        #แสดงข้อความ
        # putText(ภาพ ,ข้อความ ,พิกัดที่จะแสดงข้อความ(x,y) , font , ขนาดข้อความ, สี , thickness หรือ ความหนา)
        #หรือสรุปง่ายๆ คือ putText(ภาพ,ข้อความ,ตําแหน่ง,ฟอนต์,ขนาด,สี,ความหนา)
        cv2.putText(frame, currrntDate, (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), cv2.LINE_4) # สีดำ คือ (0,0,0) ,type เป็น cv2.LINE_4
        cv2.imshow("Output", frame) #แสดงภาพ #"Output" คือชื่อหน้าต่าง หรือ window , frame คือภาพ
        if cv2.waitKey(10) & 0xFF == ord("q"): #ถ้ากด q ให้หน้าต่างปิดอัตโนมัติ
            break
    else:    
        break 

cap.release() #ปิดกล้อง
cv2.destroyAllWindows() #ปิดหน้าต่าง