import cv2
import numpy
pic = cv2.imread('image.jpg')

threshholdval1=50
threshholdval2=100

canny = cv2.Canny(pic, threshholdval1,threshholdval2)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
