#Demo basic17 แสดงภาพจากจุด pixel
#ใช้ควมารู้จาก basic16.py

import cv2#เรียกใช้ cv2

import numpy #เรียกใช้ numpy

img = cv2.imread("image/RBG.png") #อ่านภาพ

#ปรับขนาดภาพ
imgresize = cv2.resize(img,(600,600))#ความกว้าง,ความสูง

def clickPosition(event, x, y, flags, param): #ฟังก์ชันที่จะทำงาน
    if event == cv2.EVENT_LBUTTONDOWN: #ถ้าเป็นการคลิกซ้าย
        blue = imgresize[y,x,0] #เราจะเอาค่าสีที่อ่านได้มาเก็บไว้ในตัวแปร blue
        green = imgresize[y,x,1] #เราจะเอาค่าสีที่อ่านได้มาเก็บไว้ในตัวแปร green
        red = imgresize[y,x,2] #เราจะเอาค่าสีที่อ่านได้มาเก็บไว้ในตัวแปร red
        
        #แก้ไขโค้ดจาก basic16.py โดยการลบโค้ด2 บรรทัดต่อไปนี้***   
        # text = str(blue) + " , " + str(green) + " , " + str(red) #เราจะเอาค่าสีที่อ่านได้มาเก็บไว้ในตัวแปร text
        # cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7  , (0,0,0), cv2.LINE_4)
        
        #แล้วแก้เปลี่ยนเป็น ดังนี้ จะแสดงหน้าต่างเพิ่มอีกหน้านึง กลายเป็น 2 หน้าต่าง
        #cv2.imshow("Result", imgcolor) คือคำสั่งที่สร้างหน้าต่างใหม่ โดยเปลี่ยนชื่อจาก "Output" เป็น "Result" โดยหน้าต่าง output แสดงหน้าต่างต้นแบบ 
        # และหน้าต่าง result แสดงภาพสีที่เราเอาเมาส์ไปคลิก  ,โดยอันดับแรกเราจะสร้างภาพสีดำก่อน เช่น
        imgcolor = numpy.zeros([300,300,3], numpy.uint8)#กําหนดขนาดภาพ , กําหนดชนิดข้อมูล ,  สรุปมันการสร้างภาพสีดำ numpy.uint8 คือสีดำของภาพ  
        #note; numpy.zeros([300,300,3]) คือการสร้างภาพสีดำขนาด 300x300 และมี 3 ช่องสี
        #cv2.imshow("Result", imgcoloer) คือการแสดงภาพสีดำ ,unsigned integer 0-255 คือสีดำของภาพที่เราจะสร้างไม่มีสัญลักษณ์ (uint8) ,8 คือ 8 bits
        
        #เปลี่ยนภาพจแสดงภาพหน้าต่าง2จากกภาพสีดำเป็น ภาพตามที่เราคลิกเมาส์ เช่น สี blue ,green ,red
        imgcolor[:] = [blue, green, red]

        cv2.imshow("Result", imgcolor)#แสดงหน้าต่าง result หรือ หน้าต่างสีดำ 
        
#แสดงภาพ
cv2.imshow("Output", imgresize) #แสดงหน้าต่างต้นแบบ
cv2.setMouseCallback("Output", clickPosition)#cilckPosition คือฟังก์ชันที่เราจะใช้ทำงาน
cv2.waitKey(0)#รอให้ผู้ใช้งานกดปุ่มเพื่อปิดหน้าต่าง
cv2.destroyAllWindows()#ปิดหน้าต่าง