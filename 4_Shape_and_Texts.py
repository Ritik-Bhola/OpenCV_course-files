import cv2
import numpy as np

img =np.zeros((400,400,3),np.uint8)  # creating a np array which will form an black image

# img[:] = 255,0,0  # coloring img blue

cv2.line(img,(0,0),(300,300),(0,255,0),3) # creating line on image where- 0,0 is starting point, 300,300 is ending point,(0,255,0) is for green color and 3 denotes width of line.
cv2.rectangle(img,(0,0),(250,250),(0,0,255),2) # same values as line
# cv2.rectangle(img,(0,0),(250,250),(0,0,255),cv2.FILLED) # used to fill the rectangle
cv2.circle(img,(200,50),30,(255,255,0),5)  # Creating circle where (200,50) is centre point, 30 is radius, 5 is widht of arc.
cv2.putText(img,"Hello",(250,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2) # Putting text on image where, (250,200) is starting point, 1 is size of test,2 is thickness of text.

cv2.imshow("Image",img)
cv2.waitKey(0)
