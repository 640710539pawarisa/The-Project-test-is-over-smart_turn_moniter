#ใส่ข้อความ text ในภาพ basic13
import cv2 #เรียกใช้ cv2

#อ่านภาพ
img = cv2.imread("image/Klage.jpeg")

#กำหนดขนาด
imgresize = cv2.resize(img, (700,700))

#วาดข้อความ text ในภาพ
# putText(ภาพ ,ข้อความ ,พิกัดที่จะแสดงข้อความ(x,y) , font , ขนาดข้อความ, สี , thickness หรือ ความหนา)
#หรือสรุปง่ายๆ คือ putText(ภาพ,ข้อความ,ตําแหน่ง,ฟอนต์,ขนาด,สี,ความหนา)

#มี font มากกว่า 1 ตัว ต้องใช้ cv2.FONT_HERSHEY_SIMPLEX 
#และ มี font ให้เลือกด้วยหลากหลายฟอนต์  มีในเว็บ opencv.org

#วาดข้อความ text ในภาพ

#note ถ้าต้องการย้ายตำแหน่งด้วยการเปลี่ยนเลขที่แกน x ,y

#font แบบ  cv2.FONT_HERSHEY_SIMPLEX ถ้าไม่อยากเขียนยาวๆให้ใส่เป็นเลข 0 แทนได้เช่น
#cv2.putText(imgresize, "Klage", (150,100), 0, 2.5, (0,0,255), cv2.LINE_AA)

#ความหนาเป็น cv2.LINE_AA มันคือเส้นขอบ แบบ LineTypes (cv::LINE_AA = 16)ตามในเว็บ opencv
cv2.putText(imgresize, "Klage", (150,100), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,255), cv2.LINE_AA)

#ความหนาเป็น cv2.LINE_AA มันคือเส้นขอบ แบบ LineTypes (cv::LINE_4 = 4)ตามในเว็บ opencv ม
#มี -1 คือ FILLED , 4 คือ LINE_4 , 8 คือ LINE_8 , 16 คือ LINE_AA

#cv2.putText(imgresize, "Klage", (150,100), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,255), -1)
#cv2.putText(imgresize, "Klage", (150,100), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,255), 4)
#cv2.putText(imgresize, "Klage", (150,100), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,255), 8)
#cv2.putText(imgresize, "Klage", (150,100), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,255), 16)


#ลองย้ายพิกัด ความหนา 5 (เรากำหนดเอง)
cv2.putText(imgresize, "Klage", (200,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 5)

#ถ้าตัวหนังสือหนาขึ้นต้องเปลี่ยน font เป็นอันอื่น เช่น cv2.FONT_HERSHEY_COMPLEX หรือ ใส่เป็นเลข 3 ก็ได้ เช่น
#cv2.putText(imgresize, "Klage", (300,300), 3, 2, (255,0,0), 5)
cv2.putText(imgresize, "Klage", (300,300), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 5)

#ถ้าต้องการเปลี่ยน font เป็นแบบอื่น เช่น cv2.FONT_HERSHEY_PLAIN หรือ ใส่เป็นเลข 1 ก็ได้ เช่น
#cv2.putText(imgresize, "Klage", (600,600), 1, 2, (255,0,0), 5)
cv2.putText(imgresize, "Klage", (600,600), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 5)

#ถ้าต้องการเปลี่ยน font เป็นแบบอื่น เช่น cv2.FONT_HERSHEY_DUPLEX หรือ ใส่เป็นเลข 2 ก็ได้ เช่น
#cv2.putText(imgresize, "Klage", (700,700), 2, 2, (255,0,0), 5)
cv2.putText(imgresize, "Klage", (700,700), cv2.FONT_HERSHEY_DUPLEX, 2, (0,255,0), 5)

#ลองเปลี่ยนข้อความในภาพเป็นอย่างอื่น
cv2.putText(imgresize, "Greek", (400,400), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 5)

#แสดงภาพ
cv2.imshow("Output", imgresize)
cv2.waitKey(0)#รอปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง