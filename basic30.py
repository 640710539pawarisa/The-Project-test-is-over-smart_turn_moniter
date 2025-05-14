#เปรียบเทียบค่า Threshold Value basic30
#คือการลองเปลี่ยนค่า threshold value ให้เป็นค่าอื่นดู ค่า เดิมคือ 128
import cv2#เรียกใช้ cv2
import matplotlib.pyplot as plt #เรียกใช้ matplotlib

#อ่านภาพ
img = cv2.imread("image/ant.jpg")#อ่านภาพ
img =cv2.resize(img,(400,300))#ปรับขนาดภาพ

#แปลงภาพสีเป็น grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#ใช้ในการเปลี่ยนค่า threshold value ว่าจะเป็นแบบใบ โดยทำเป็น list ขึ้นมาชุดนึง
threshold_values = [50 , 100 , 150 , 200 , 250]

plt.subplot(231,xticks=[],yticks=[]) #แบ่งหน้าต่างเป็น 2 แถว 3 คอลัมน์ ตำแหน่งที่ 1 จองภาพให้เป็น Original ใช้งานในการแสดงภาพ
plt.title("Original")
plt.imshow(img_gray, cmap="gray") #แสดงภาพ , cmap="gray" คือการแสดงภาพในรูปแบบ grayscale

#วนลูปตาม รูปที่เราสร้าง
for i in range(len(threshold_values)):#range คือการวนลูป , len คือการหาความยาวของ threshold_values
    thresh, result = cv2.threshold(img_gray, threshold_values[i], 255, cv2.THRESH_BINARY)#thresh คือค่ากลาง threshold 
    #, result คือภาพที่เราแปลงจากภาพgrayscale เป็น ภาพ binary
    plt.subplot(232+i)#การplot ตามรูปที่เราสร้างโดยให้เริ่มต้นที่ต่อท้ายoriginalคือ231 (มันคือตำแหน่งที่ 1)แต่เราจะเริ่มต้นที่ 232
    plt.title("%d"%threshold_values[i])#แสดงชื่อภาพ , "%d" คือการใช้ในรุปแบบ decimal ตามด้วยชื่่อตัวแปร คือthreshold_values[i]
    plt.imshow(result, cmap="gray")#cmap="gray" คือการแสดงภาพในรูปแบบ grayscale
    #ตรงแสดงภาพ เราจะได้ภาพเดิมแต่เปลี่ยนค่า threshold valueใหม่ เช่น threshold_values = [50 , 100 , 150 , 200 , 250]
    plt.xticks([]),plt.yticks([])#ไม่แสดงตัวแปร x และ y
    
plt.show()