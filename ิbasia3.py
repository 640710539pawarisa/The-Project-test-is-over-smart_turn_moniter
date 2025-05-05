#ปรับเปลี่ยนขนาดภาพ basic3

import cv2
img = cv2.imread("image/Klage.jpeg")

#ปรับเปลี่ยนขนาดภาพ
img_resize = cv2.resize(img, (400,400)) #ความกว้าง,ความสูง

#แสดงภาพ
cv2.imshow("Output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()