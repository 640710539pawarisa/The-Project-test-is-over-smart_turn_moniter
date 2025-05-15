# เส้น Contours หาเส้นเค้าโครงบนภาพ basic46
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("image/ant.jpg")
img = cv2.resize(img,(400,300))
#ทำเป็น GrayScale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ทำเป็น threshold คือการแปลงภาพเทาเป็นภาพbinary
thresh , result = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#ใช้ในการหาเส้น Contours
contours, hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#contours เอาไว้เก็บค่าของเส้น Contours
#hierarchy เอาไว้เก็บค่าของ hierarchyหรือจำนวนชั้น หรือลำดับชั้น
#cv2.RETR_TREE คือการใช้ในการหาเส้น Contours ,cv2.findContours(arrayรูปภาพ ,รูปแบบการพิจารณาลำดับชั้นของเส้นโครง,รูปแบบการหาเส้นเค้าโครง)
#ลองเปลี่ยนค่ารูปแบบการหาเส้น Contours ให้เป็น cv2.RETR_EXTERNAL และ cv2.CHAIN_APPROX_NONE ได้
print(len(contours))#นับว่ามีกี่จุดเส้น Contour

#darawContours ใช้ในการวาดเส้น Contours
cv2.drawContours(img,contours,-1,(0,0,255),thickness=2)#เส้นสีแดง เปลี่ยนสีได้
#ใช้ในการวาดเส้น Contours, cv2.drawContours(arrayรูปภาพ,เส้น Contours,ลำดับชั้น,สีของเส้น Contours,ความหนาของเส้น Contours)


cv2.imshow("Original",img)
cv2.imshow("Contours",result)
cv2.waitKey(0)
cv2.destroyAllWindows()