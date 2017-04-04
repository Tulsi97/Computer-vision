import numpy
import cv2

img= cv2.imread('image.jpg',0)
img=cv2.imwrite('blackNwhite.png',img)
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
