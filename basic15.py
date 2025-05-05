#แสดงพิกัดด้วย Mouse Event basic15  #คือเราจะทราบพิกัดเมาส์ที่กำลังคลิกในรูปภาพว่าอยู่พิกัดไหน
import cv2 #เรียกใช้ cv2

img = cv2.imread("image/jasentp.jpeg")
def clickPosition(event, x, y, flags, param):#ฟังก์ชันที่จะทำงาน ,flags คือสถานะของเมาส์หรือรูปแบบ ,param คือพารามิเตอร์
    #event คือเหตุการณ์ที่เกิดขึ้นว่าแบบ ตอนนี้เราคลิกเมาส์ซ่ายหรือขวา , def คือฟังก์ชัน ที่จะทำงาน def คือ define ,def clickPosition คือ ฟังก์ชันที่จะทำงาน
    if event == cv2.EVENT_LBUTTONDOWN:#ถ้าเหตุการณ์ที่เกิดขึ้นว่าแบบ ตอนนี้เราคลิกเมาส์ซ้าย, LBUTTONDOWN คือคลิกเมาส์ซ้าย
        
        text = str(x) + " , " + str(y)#text คือตัวแปรที่เก็บพิกัด x,y แบบ string
        
        #เลือกอย่างใดอย่างหนึ่งเพื่อแสดงข้อความ text ในภาพ
        
        # # Test ลองแสดงข้อความคำว่า "OK" ตรงพิกัดที่เราคลิกเมาส์ก่อนเช่น
        # cv2.putText(img, "OK", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), cv2.LINE_4)
        # cv2.imshow("Output", img)
        
        #แสดงพิกัดแกน x,y ตามตำแหน่งที่เราคลิกเมาส์
        cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), cv2.LINE_4)
        cv2.imshow("Output", img)

#แสดงภาพ
cv2.imshow("Output", img)#แสดงภาพ

#ทำงานกับ Mouse Event เราอยากให้มันแสดงพิกัดดแกน x,y ทีในรูปภาพผ่านเมาส์
#setMouseCallback(ภาพ หรือ window name,ฟังก์ชันที่จะทำงาน)
cv2.setMouseCallback("Output", clickPosition) #cilckPosition คือฟังก์ชันที่เราจะใช้ทำงาน
#window name คือชื่อหน้าต่างที่เราจะให้แสดงพิกัดด้วย Mouse Event ต้องเป็นชื่อเดียวกัน

cv2.waitKey(0)#รอให้ผู้ใช้งานกดปุ่มเพื่อปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง ,คืนค่าเครื่อง



