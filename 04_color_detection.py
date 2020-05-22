import numpy as np
import cv2 as cv


## Read image and changing to HSV format
img = cv.imread('WindowsLogo.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

## Cut red color on image
mask_red = cv.inRange(hsv, (0, 50, 50), (15, 255, 255))
result_red = cv.bitwise_and(img, img, mask=mask_red)

## Cut blue color on image
mask_blue = cv.inRange(hsv, (90, 50, 50), (130, 255, 255))
result_blue = cv.bitwise_and(img, img, mask=mask_blue)

## Cut yellow color on image
mask_yellow = cv.inRange(hsv, (16, 50, 50), (40, 255, 255))
result_yellow = cv.bitwise_and(img, img, mask=mask_yellow)

## Creating unique frame
top = np.concatenate((img, result_red), axis=1)
botton = np.concatenate((result_blue, result_yellow), axis=1)
final_frame = np.concatenate((top, botton), axis=0)

cv.imshow('Window', final_frame)
cv.waitKey(0)
cv.destroyAllWindows()