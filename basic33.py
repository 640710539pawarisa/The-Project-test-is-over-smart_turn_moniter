#การเปรียบเทียบค่า Block Size basic33
import cv2 

#import เพิ่ม 
import matplotlib.pyplot as plt

img = cv2.imread("image/map2.jpg",0)#อ่านภาพ

#แก้ไขส่วนนี้******
#เราจะทำแค่ของแบบ Adaptive Meanเป็นตัวอย่าง***   
#ค่า block size อยู่ตรงหลัง ,cv2.THRESH_BINARY ,ค่า block size คือ .... ,ค่า constant คือ ...
# result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)

#โดยเราจะสร้างตัวแปรมา เป็นอาเรย์หรือlist ดังนี้
#กำหนดขนาดของ block
size = [3,5,9,17,33]
#ภาพจะคมชัดมากยิ่งขึ้นตามค่าของ block size ที่เรากําหนด

#แสดงภาพนต้นฉบับ
plt.subplot(231,xticks=[],yticks=[])#แบ่งหน้าต่างเป็น 2 แถว 3 คอลัมน์ ตำแหน่งที่ 1 จองภาพให้เป็น Original ใช้งานในการแสดงภาพ
plt.imshow(img,cmap="gray")#แสดงภาพ , cmap="gray" คือการแสดงภาพในรูปแบบ grayscale

#****loop เลือกทำแบบใดแบบหนึ่ง เพราะเปลี่ยนแค่ cv2.ADAPTIVE_THRESH_MEAN_C เป็น cv2.ADAPTIVE_THRESH_GAUSSIAN_C***********

# #เราจะวนloopเพื่อแสดงผล อันนี้ทำแบบ adaptive mean (cv2.ADAPTIVE_THRESH_MEAN_C)
# for i in range(len(size)):#range คือการวนลูป , len คือการหาความยาวของ size
#     result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,size[i],1)
#     #result คือภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ binary, 
#     #cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,size[i],1) คือการทำ adaptive thresholding
#     plt.subplot(232+i)#plt.subplot คือการแสดงภาพในหน้าต่าง ,แสดงตำแหน่งที่ 2เป็นต้นไป 
#     plt.title("%d"%size[i])#แสดงชื่อภาพ, "%d" คือการใช้ในรุปแบบ decimal ตามด้วยชื่่อตัวแปร คือsize[i]
#     plt.imshow(result,cmap="gray")#แสดงภาพ , cmap="gray" คือการแสดงภาพในรูปแบบ grayscale
#     plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
#เราจะวนloopเพื่อแสดงผล อันนี้ทำแบบ adaptive gaussian(cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
for i in range(len(size)):#range คือการวนลูป , len คือการหาความยาวของ size
    result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,size[i],1)
#result คือภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ binary, 
    #cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,size[i],1) คือการทำ adaptive thresholding
    plt.subplot(232+i)#plt.subplot คือการแสดงภาพในหน้าต่าง ,แสดงตำแหน่งที่ 2เป็นต้นไป 
    plt.title("%d"%size[i])#แสดงชื่อภาพ, "%d" คือการใช้ในรุปแบบ decimal ตามด้วยชื่่อตัวแปร คือsize[i]
    plt.imshow(result,cmap="gray")#แสดงภาพ , cmap="gray" คือการแสดงภาพในรูปแบบ grayscale
    plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
    
plt.show()


