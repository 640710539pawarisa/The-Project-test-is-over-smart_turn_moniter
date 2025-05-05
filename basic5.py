#การเขียนภาพ basic5 (การ export รูปภาพ)

import cv2

#ex. อ่านภาพเข้ามาเป็นขาวดำ แล้ว export ออกมาเป็นสี 

img = cv2.imread("image/Klage.jpeg")  #อ่านภาพเข้ามา imread
imgresized = cv2.resize(img, (400,400)) #ปรับขนาดภาพ resize  เป็นขนาด 400x400
cv2.imshow("My Image", imgresized) #แสดงภาพ imshow


#การเขียนภาพ
cv2.imwrite("output.jpeg", imgresized)#เปลี่ยนชื่อไฟล์(เปลี่ยนชื่อภาพที่จะส่งออกไป)
#imwrite คือการ export รูปภาพ จะรับแค่2ค่า ต้องระบุด้วย ค่าที่ทั้ง2คือ ชื่อไฟล์(ชื่อภาพที่จพส่งออกไป) และภาพที่จะ export(ภาพที่จะส่งออกไป)
#เช่น imwrite(ชื่อไฟล์,ภาพที่จะส่งออกไป)
#runเสร็จจะได้ไฟล์ output.jpeg ออกมาเพิ่ม

#แสดงภาพ
cv2.waitKey(0) #รอให้ผู้ใช้งานกดปุ่มเพื่อปิดหน้าต่าง
cv2.destroyAllWindows() #ปิดหน้าต่าง ,คืนค่าเครื่อง
