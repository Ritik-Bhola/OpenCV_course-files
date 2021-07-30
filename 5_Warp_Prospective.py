import cv2
import numpy as np

img=cv2.imread("Resources/card2.jpeg")
# imgResize=cv2.resize(img,(500,400))

width,height =175,300
# pt1=np.float32([[182,220],[388,168],[272,366],[426,210]])
# pt2=np.float32([[0,height],[0,0],[width,height],[width,0]])

pt1=np.float32([[102,26],[179,26],[102,144],[179,144]])
pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

# cv2.imshow("Output",imgResize)
cv2.imshow("Img",img)
cv2.imshow("Warp Prospective Image",imgOutput)
cv2.waitKey(0) 