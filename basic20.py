#ตรวจจับใบหน้าจากภาพ  basic20

import cv2 
import numpy 

img = cv2.imread("image/face.jpg") #อ่านภาพ
img = cv2.resize(img,(400,500))#ปรับขนาดภาพ

#อ่านไฟล์ สำหรับ classification
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")#ตรวจจับใบหน้า
#cv2.CascadeClassifier V คือการเรียกใช้ คลาสที่ใช้โหลดและใช้งานตัวตรวจจับวัตถุ (Object Detector) ซึ่งในกรณีนี้คือการตรวจจับ ใบหน้า (Face Detection) 
# -ต่อ...ด้วยวิธีที่เรียกว่า Haar Cascade Classifier
#face_cascade คือตัวแปรที่เก็บค่าของการตรวจจับใบหน้า

#ก่อนเราจะแยกใบหน้า อันดับแรกเราต้องภาพสีของเราเป็ยภาพ GrayScale ก่อน
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#คือเป็นการแปลงภาพให้เป็นภาพ GrayScale โดยเก็บไว้ในตัวแปร gray_img

#เราจะเอาภาพ gray_img ที่เราได้แปลงมาเป็นภาพ GrayScale แล้ว มาใช้ในการตรวจจับใบหน้า

#จำแนกใบหน้าจากภาพ GrayScale
#note :
# | พารามิเตอร์          | ความหมายแบบละเอียด                                                                                                                                                                                              
# | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# | `gray_img`        | ภาพต้นฉบับที่แปลงเป็นภาพขาวดำแล้ว (`cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`) เพราะ Haar Cascade ทำงานกับภาพขาวดำ                                                                                                 
# | `scaleFactor=1.1` | บอกให้ตัวตรวจจับ **ลดขนาดภาพลงกี่เท่าในการค้นหาใบหน้าในหลายระดับขนาด (multi-scale)**<br>เช่น 1.1 = ลดขนาดลง 10% ในแต่ละขั้น 
# ---เพื่อหาว่ามีใบหน้าในขนาดเล็กลงไหม<br> **ค่าเล็กเกินจะช้า** / ค่าใหญ่เกินจะพลาดวัตถุ 
# | `minNeighbors=5`  | **จำนวนกล่องที่ต้องตรวจพบใกล้กันก่อนจะถือว่าเป็นใบหน้าจริง**<br>ค่ามาก = เข้มงวด (แม่นแต่พลาดได้) <br> ค่าน้อย = ใจดี 
# ---(อาจตรวจผิดว่าเป็นหน้า)                                                                   
# | **ผลลัพธ์**        | คืนค่าลิสต์ของตำแหน่งใบหน้าที่พบในรูปแบบ (x, y, w, h)                                                                                                                                                           
# สรุป คือการค้นหาใบหน้าหลายขนาดในภาพขาวดำ โดย:

# scaleFactor = ควบคุมการลดขนาดทีละขั้น

# minNeighbors = ควบคุมความแม่นยำ/ความเข้มงวด

# ผลลัพธ์คือ list ของตำแหน่งใบหน้าที่ตรวจพบ

#******** จำแนกใบหน้าใช้แค่ 3 คำสั่งนี้ โค้ด 3บรรทัดนี้


scaleFactor = 1.1  #คือ กำหนดย่อขนาดภาพให้เป็นสัดส่วน  เช่น 1.1 = ลดขนาดลง 10%
#(1.1 คือค่า default)ปรับเปลี่ยนค่าไก้แต่ห้ามค่าต่ำกว่านี้
minNeighbors = 3 #คือ กำหนด ค่า test hoding (คือค่าที่ใช้ตรวจสอบส่วนของภาพ GrayScale)โดยจะทำการสร้าง 4เหลี่ยมผืนผ้าหรือกล่อง
#และคำนวณพื้นที่ในการตรวจจับใบหน้าออกมา ว่าเจอจำนวนเท่าไหร่ ,Neighbors คือ เพื่อนบ้าน ที่อยู่ใกล้กัน หรือใกล้เคียงกัน แบบเจอซ้ำๆ 
# โดยเราจะกำหนดว่าเราเจอซ้ำๆ = 3 ก็จะนับเป็นใบหน้า โดยจะนับจากภาพ GrayScale
#(3 คือค่า default)ปรับเปลี่ยนค่าไก้แต่ห้ามค่าต่ำกว่านี้
face_detected = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbors)#ตรวจจับใบหน้าจากภาพ GrayScale  
# - ต่อ ..... และเก็บไว้ในตัวแปร face_detected
# note : face_cascade.detectMultiScale คือการใช้ตรวจจับใบหน้าจากภาพ GrayScale โดยเก็บไว้ในตัวแปร face_cascade
# เพิ่มเติม ; .detectMultiScale คือ วิธีการตรวจสอบใบหน้าตามค่าที่เราระบุเข้าไป หรือตามภาพ GrayScale ที่เราระบุเข้าไป


#*****

#แสดงตำแหน่งใบหน้าที่ตรวจพบ
for (x, y, w, h) in face_detected: 
    #วนลูปเพื่อแสดงตำแหน่งใบหน้าที่ตรวจพบ x คือตำแหน่งที่เริ่มต้น y คือตำแหน่งที่สิ้นสุด w คือความกว้าง h คือความสูง ในตำแหน่งที่เจอใบหน้า
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness= 2)
    #อธิบาย คือ สร้างภาพกราฟิกเป็นกล่องสี่เหลี่ยมในตำแหน่งที่เจอใบหน้า และ img คือภาพสี เริ่มต้นมุมบนซ้าย (x,y) สิ้นสุดมุมล่างขวา (x+w,y+h)
    #,สีเขียว,ความหนา 2 (thickness คือความหนา)

#แสดงภาพ
cv2.imshow("Original", img)#แสดงภาพต้นฉบับ
cv2.imshow("Result", gray_img)#แสดงภาพ GrayScale
cv2.waitKey(0)#รอปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง


