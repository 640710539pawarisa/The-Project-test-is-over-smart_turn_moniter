#แสดง Threshold ใน Matplotlib
import cv2
#เพิ่ม Matplotlib เข้ามา
import matplotlib.pyplot as plt

#อ่านภาพ
gray_img = cv2.imread("image/gradient.jpeg")
gray_img =cv2.resize(gray_img,(250,250))#ปรับขนาดภาพ

#ทำภาพเทาเป็นภาพขาวดำด้วย คำสั่ง cv2.threshold******
thresh, result1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh, result2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh, result3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
thresh, result4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
thresh, result5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

#สิ่งที่เราสร้างเพิ่ม คือ list
images = [gray_img, result1,result2,result3,result4,result5]
#images คือตัวแปรที่เก็บภาพที่เราสร้าง ,result1 คือตัวแปรที่เก็บภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ binary ,
#result2 คือตัวแปรที่เก็บภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ binary_inv
#result3 คือตัวแปรที่เก็บภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ trunc
#result4 คือตัวแปรที่เก็บภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ tozero
#result5 คือตัวแปรที่เก็บภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ tozero_inv
titles = ["Original","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]
#titles คือตัวแปรที่เก็บชื่อภาพที่เราสร้าง โดนเขียนจับคู่กับ imagesที่เราสร้าง listไว้ 

#แสดงภาพ
for i in range(len(images)):#range คือการวนลูป , len คือการหาความยาวของ images
    plt.subplot(2,3,i+1)#แบ่งหน้าต่างเป็น 2 แถว 3 คอลัมน์ , i+1 คือการวนลูป ,subplot คือการแสดงภาพในหน้าต่าง
    plt.imshow(images[i])#แสดงภาพ , images[i] คือภาพที่เราสร้าง
    plt.title(titles[i])#แสดงชื่อภาพ, titles[i] คือชื่อภาพที่เราสร้าง
    plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
plt.show()


