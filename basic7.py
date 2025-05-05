#เปิดวีดีโอด้วย opencv

import cv2

cap = cv2.VideoCapture("image/videotestt.mp4") #เปิดวีดีโอด้วย opencv ที่ตำแหน่งที่เก็บวีดีโอไว้ แล้วใส่ชื่อวีดีโอ

while (cap.isOpened()):#ใช้ while เพื่อให้หน้าต่างไม่ปิดอัตโนมัติ ,cap.isOpened() คือเช็คว่ากล้องเปิดไหม หรือ วีดีโอเปิดไหม หรือสามารถเปิดได้ไหมไม่มีข้อผิดพลาดเกิดขั้น สรุปคือเปิดใช้งาน
    check, frame = cap.read()#รับภาพจากวีดีโอ frame ต่อ frame , 1 ภาพก็เป็น 1 frame
    cv2.imshow("Output", frame)
    
    if check == True:
        cv2.imshow("Output", frame) #แสดงภาพ
        if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:    
        break #ถ้าไม่ได้รับภาพจากวีดีโอจะ break
    
cap.release()#ปิดวีดีโอ
cv2.destroyAllWindows()#ปิดหน้าต่าง ,คืนค่าเครื่อง