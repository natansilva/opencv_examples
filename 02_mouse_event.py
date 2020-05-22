import cv2 as cv
import numpy as np


## Function to draw a rectangule on mouse event
def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        rectangule['x1'] = x
        rectangule['y1'] = y
    
    if event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (rectangule['x1'], rectangule['y1']), (x, y), (255, 255, 255))
        cv.imshow('img', img)

## Initial image and retangule position
img = np.zeros((600, 600, 3), np.uint8)
rectangule = { 'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0 }

## Open window and wait to draw retangule
cv.imshow('img', img)
cv.setMouseCallback('img', click_event)

## Waiting any button press to exit
cv.waitKey(0)
cv.destroyAllWindows()