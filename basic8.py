#video GrayScale Mode basic8 เปลี่ยนภาพสีเป็น GrayScale
import cv2

cap = cv2.VideoCapture(2) #เปิดกล้อง
#recap วนเช็คกล้อง 3 ตัว ได้ 0 คือกล้อง snapcam ไม่ควรใช้, 1 คือกล้อง  notebook  2 คือกล้อง webcam

while (cap.isOpened()):
    check, frame = cap.read() #อ่านภาพจากกล้อง
    
    if check == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #แสดงภาพ จากภาพสีเป็นภาพgrayScale เก็บลงตัวแปร gray
        cv2.imshow("Output", gray)#แสดงภาพ
        if cv2.waitKey(1) & 0xFF == ord("q"): #ถ้ากด q ให้หน้าต่างปิดอัตโนมัติ
            break
    else:    
        break 

cap.release() #ปิดกล้อง
cv2.destroyAllWindows() #ปิดหน้าต่าง