import cv2
import numpy as np


img = cv2.imread("Resources/adaptiveml.png")  # Importing image

kernel=np.ones((5,5),np.uint8)

imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Converting color image to grey
imgBlur=cv2.GaussianBlur(imgGrey,(7,7),0)  # Adding blur effect to grey image
imgCanny =  cv2.Canny(img,100,100)  # Edge detector in image -- By increasing the numbers we can get less edge image
imageDialation=cv2.dilate(imgCanny,kernel,iterations=1)  # used to increase thickness of edges
imageEroded=cv2.erode(imageDialation,kernel,iterations=1)   # used to increase thickness of edges

cv2.imshow("Grey Image",imgGrey)  # showing grey image
cv2.imshow("Blur Image",imgBlur)  # showing brur image 
cv2.imshow("Canny Image",imgCanny)  # showing Canny image 
cv2.imshow("Dialation Image",imageDialation)  # showing delated image 
cv2.imshow("Eroded Image",imageEroded)  # showing eroded image 

cv2.waitKey(0) # adding wait time