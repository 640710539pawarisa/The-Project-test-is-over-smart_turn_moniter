#การสร้าง color Trackbar เบื้องต้น basic26 คือ ใช้ trackbar 
# เพื่อเลือกสีหรือค่าสีของภาพหน้าต่างโปรแกรมของเรา เช่นสีแดง สีเขียว สีน้ําเงิน เผื่อเราอยากสีมาผสมกกัน
#เผื่อเราอยากเอาสีมาผสมกกัน โดยให้เรากำหนดค่าแต่ละสีที่จะเอาผสมกัน

#****สรุปคือการใช้ trackbar เพื่อผสมสีในจานผสมสีที่สร้างขึ้นมาเอง************

import cv2#เรียกใช้ cv2
import numpy #เรียกใช้ numpyเพื่อสร้างภาพขึ้นมา

#ทำภาพสีดำ ขึ้นมา
img = numpy.zeros((200,250,3), numpy.uint8)#ภาพที่แสดงออกมาเป็นสีดำ เราจะถือว่าจานสีที่เราจะใช้ผสมสี

#ส่วนผสมสีจะใช้ trackbar
cv2.namedWindow("Color Trackbar")#สร้างหน้าต่างชื่อ Color Trackbar

#callback function ที่ข้างในส่งค่า slider ที่มีชื่อ ว่า Value
def display(value):#ฟังก์ชันที่จะทำงาน
    pass #ในกรณีถ้าไม่อยากให้มัน printอะไรแต่อยากให้มันทำงานอยู่
    # print(value)
#*****ส่วนของการทำงาน คือถ้ามีการเปลี่ยนแปลงค่าใน trackbar แต่ละตัว จะมาเรียกทำงานในฟังก์ชันนี้

#เริ่มต้นสร้าง trackbar Slider
cv2.createTrackbar("Blue","Color Trackbar",0,255,display)#display คือ callback function
#สร้างตัวแปรเพื่อเก็บค่าสีที่เราจะใช้ผสมสี, ชื่อตัวแปร,ชื่อหน้าต่าง,ค่าเริ่มต้น(valueหรือminimum),ค่าสูงสุด(maximum),ฟังก์ชันที่จะทำงาน(onchange หรืออีเวนที่จะเกิดขึ้นเมื่อเราsiderตัวtrackbar) 
cv2.createTrackbar("Green","Color Trackbar",0,255,display)
cv2.createTrackbar("Red","Color Trackbar",0,255,display)

#ถัดมาต้องการเอาค่าที่ได้จาก trackbar ที่เราคลิกเลือกมา มาใช้ไปผสมในภาพสีดำที่สร้างขึ้นมา
#*******โดยเราจะทำโดยการเราจะไปดึงเอาค่าที่ได้จาก trackbar แต่ละตัว(เช่น สีน้ำเงิน,สีเขียว,สีแดงตรงที่เราเริ่มต้นสร้าง trackbar) มาใช้ผสมเป็นรูปตามสี

#ใช้งานแบบloop while เพราะเราจะใแสดงผลเป็นรูปภาพและเปลี่ยนเปลี่ยนค่าในTrackbar และแสดงผลแบบ real time
while True:
    cv2.imshow("Color Trackbar",img)
    #เราจะเอาค่าที่ได้จาก trackbar มาใช้ไปเปลี่ยนสีในภาพ
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    #****ส่วนที่ผสมใส่จานสี จาก trackbar
    #ดึงค่าจาก trackbar
    blue = cv2.getTrackbarPos("Blue","Color Trackbar")#คือดึงค่าสีน้ำเงิน ,(ชื่อtrackbar,ชื่อหน้าต่างที่อยากใช้งาน)แล้วเราใส่ตัวแปร ชื่อ blue
    green = cv2.getTrackbarPos("Green","Color Trackbar")#คือดึงค่าสีเขียว ,(ชื่อtrackbar,ชื่อหน้าต่างที่อยากใช้งาน)แล้วเราใส่ตัวแปร ชื่อ green
    red = cv2.getTrackbarPos("Red","Color Trackbar")#คือดึงค่าสีแดง ,(ชื่อtrackbar,ชื่อหน้าต่างที่อยากใช้งาน)แล้วเราใส่ตัวแปร ชื่อ red
    
    #ถัดมาเราจะนำมากำหนดใส่รูปภาพของเรา ,note : img[:] คือกำหนดอาเรย์ในทุกๆตัวตั้งแต่ตัวแรกจนถึงตัวสุดท้าย
    img[:] = [blue,green,red]
    

cv2.destroyAllWindows#ปิดหน้าต่าง