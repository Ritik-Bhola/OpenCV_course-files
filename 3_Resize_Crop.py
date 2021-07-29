import cv2
import numpy as np

img=cv2.imread("Resources/adaptiveml.png")  #Reading image from Resources folder
print(img.shape)   #prints shape of the image

imgResize=cv2.resize(img,(500,400))
print(imgResize.shape)   #prints shape of the image

imgCroped=img[0:200,300:800]# Croping image
cv2.imshow("Output",img)  # Showing image
cv2.imshow("Resize Image",imgResize)  # Showing Resized image
cv2.imshow("Croped Image",imgCroped)  # Showing croped image
cv2.waitKey(0)  #  Time to show image 
