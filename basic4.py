#เปลี่ยนสีภาพ basic4

import cv2
img = cv2.imread("image/Klage.jpeg")

#เปลี่ยนสีภาพ
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#แสดงภาพ
cv2.imshow("Output", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#หรือมาปรับเปลี่ยนที่ pathของรูปภาพ ด้วยตัวเลข 0 คือ ภาพขาวดำ 1 คือ ภาพสี

# img = cv2.imread("image/Klage.jpeg",0)

# #ภาพขาวดำ
# cv2.imshow("Output", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # ภาพสี
# img = cv2.imread("image/Klage.jpeg",1)

# cv2.imshow("Output", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()