# Python ile istediğiniz fotoğrafın karakalem şeklinde yazdırılmasını sağlayan program



from cv2 import cv2



img = cv2.imread("E:/DOWNLOADS/elizabeth.jpg") #buraya istediğiniz resmin ismini uzantısıyla yazın
 

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_img = cv2.bitwise_not(gray_img)

img_smoothing = cv2.GaussianBlur(inverted_img, (21, 21), sigmaX=0, sigmaY=0)

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

final_img = dodgeV2(gray_img, img_smoothing)

cv2.imshow("two maximoffs", final_img)
cv2.waitKey()
 


