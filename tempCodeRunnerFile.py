#เปลี่ยนสีภาพ
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#แสดงภาพ
cv2.imshow("Output", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()