import cv2

print("Package imported")
# Uncomment it to import image
"""

img=cv2.imread("Resources/adaptiveml.png")  #Reading image from Resources folder

cv2.imshow("Output",img)  # Showing image
cv2.waitKey(0)  #  Time to show image 

"""


vid = cv2.VideoCapture("Resources/test_vedio.mp4") # Reading video rom Resources folder

while True:
    success,image = vid.read() # Converting video to image
    cv2.imshow("Video",image)  # showing video as a combination of images
    if cv2.waitKey(10) & 0xFF ==ord('q'):    #Time to show video and  quiting video if " q " is pressed
        break
   

"""
web=cv2.VideoCapture(0)  # If you have single webcam type 0, if 2 type 1 ....and so on
web.set(3,640) # here id 3 is width
web.set(4,480) # here id 4 is height

while True:
    success,image1 = web.read() # Converting video to image
    cv2.imshow("Video",image1)  # showing video as a combination of images
    if cv2.waitKey(10) & 0xFF ==ord('q'):    #Time to show video and  quiting video if " q " is pressed
        break

"""