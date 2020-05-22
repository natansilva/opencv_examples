import cv2 as cv
import numpy as np


## Read image
img = cv.imread('LinuxLogo.jpg')

## Kernel is a structure which decides the nature of operation and the quantity
## of neighborhoods to use in operation.
kernel = np.ones((3, 3), np.uint8)

## Dilation operation increases the white area in the image. If atleast one pixel
## under the kernel is `1` so the central pixel is set to `1`.
dilation = cv.dilate(img, kernel, iterations=1)

## Erosion is the oposite of the dilation, the central pixel is set to `1`
## if all the pixels under the kernel are `1`.
erosion = cv.erode(img, kernel, iterations=1)

## Opening is the process of erosion followed by dilation. 
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

## Close is the process of dilation followed by erosion.
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

## Gradient is the difference between dilation and erosion of an image.
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

## Top Hat is the difference between input image and Opening of the image.
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

## Black Hat is the difference between the closing of the input image and input image
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

## Creating unique frame
top = np.concatenate((img, dilation, erosion, opening), axis=1)
botton = np.concatenate((closing, gradient, tophat, blackhat), axis=1)
final_frame = np.concatenate((top, botton), axis=0)

cv.imshow('Window', final_frame)
cv.waitKey(0)
cv.destroyAllWindows()