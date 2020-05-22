import numpy as np
import cv2 as cv

## Funtion to pass to createTrackBar to do nothing
def nothing(x):
    pass


## Initial image
img = np.zeros((200, 600, 3), np.uint8)

## Creating Trackbar
cv.namedWindow('ColorMaker')
cv.createTrackbar('Red', 'ColorMaker', 0, 255, nothing)
cv.createTrackbar('Green', 'ColorMaker', 0, 255, nothing)
cv.createTrackbar('Blue', 'ColorMaker', 0, 255, nothing)

## Starting color maker loop
while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    cv.imshow('ColorMaker', img)

    ## Getting choose colors
    red = cv.getTrackbarPos('Red', 'ColorMaker')
    green = cv.getTrackbarPos('Green', 'ColorMaker')
    blue = cv.getTrackbarPos('Blue', 'ColorMaker')
    
    ## Setting color image with track bar 
    img[:] = [red, green, blue]

cv.destroyAllWindows()