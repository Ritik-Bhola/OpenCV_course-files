import cv2
import numpy as np

def empty(a):
    pass
cv2.namedWindow("TrackBars")  # Ceating a window TrackBar
cv2.resizeWindow("TrackBars",640,240)  # Resizing TrackBar
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  # Creating Trackbar here 0=min value of track bar, 179 = max value of trackbar and empty is the function used with trackbar.
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Saturation Min","TrackBars",0,255,empty)
cv2.createTrackbar("Saturation Max","TrackBars",255,255,empty)
cv2.createTrackbar("Value Min","TrackBars",0,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread("Resources/card2.jpeg")  # importing image

    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # Converting imd BGR color to HSV

    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")  # Getting TrackBar value
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")  # Getting TrackBar value
    s_min = cv2.getTrackbarPos("Saturation Min","TrackBars")    # Getting TrackBar value
    s_max = cv2.getTrackbarPos("Saturation Max","TrackBars")    # Getting TrackBar value
    v_min = cv2.getTrackbarPos("Value Min","TrackBars")     # Getting TrackBar value
    v_max = cv2.getTrackbarPos("Value Max","TrackBars")     # Getting TrackBar value
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)  # It will filter out and give us image of that color
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original Image",img) # Showing image
    cv2.imshow("HSV Image",imgHSV)  # Showing image
    cv2.imshow("Mask",mask)  # Showing image
    cv2.imshow("Result",imgResult)  # Showing image
    cv2.waitKey(0) 