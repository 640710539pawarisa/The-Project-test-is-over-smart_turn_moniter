#การบันทึกวีดีโอ
import cv2

cap = cv2.VideoCapture(2) #เปิดกล้อง
#recap วนเช็คกล้อง 3 ตัว ได้ 0 คือกล้อง snapcam ไม่ควรใช้, 1 คือกล้อง  notebook  2 คือกล้อง webcam

# fourcc = cv2.VideoWriter_fourcc(*'XVID') #กําหนดรูปแบบวีดีโอ
# บางเครื่องไม่รองรับ 'XVID' ให้ลองเปลี่ยนเป็น 'MJPG' เช่น:
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

result = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480)) #กําหนดชื่อวีดีโอ และขนาดวีดีโอ ,result คือตัวแปรที่บันทึกวีดีโอ

while (cap.isOpened()):#ใช้ while เพื่อให้หน้าต่างไม่ปิดอัตโนมัติ,เปิดกล้อง
    check, frame = cap.read() #อ่านภาพจากกล้อง
    
    if check == True:
        cv2.imshow("Output", frame) #แสดงภาพ
        result.write(frame) #บันทึกภาพ
        if cv2.waitKey(1) & 0xFF == ord("q"): #ถ้ากด q ให้หน้าต่างปิดอัตโนมัติ
            break

result.release() #ปิดวีดีโอ ,รวบรวมไฟล์วีดีโอ
cap.release() #ปิดกล้อง 
cv2.destroyAllWindows() #ปิดหน้าต่าง