import cv2 
import numpy as np

img = cv2.imread("Resources/card2.jpeg")

#  In order to perform horizontal and vertical stack we need both images to have same number of kernel i.e they must be both rgb or both must be grey.
imghor=np.hstack((img,img))  # horizontal Stack
imgVer=np.vstack((img,img))  # vertical Stack
 
cv2.imshow("Horizontal",imghor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)