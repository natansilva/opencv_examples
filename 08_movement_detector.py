import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 300)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    frame_a = frame1.copy()
    frame_b = frame1.copy()
    frame_c = frame1.copy()

    ## Difference between frames and image preprocessing
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilate = cv.dilate(thresh, None, iterations=3)

    ## Getting contours of objects
    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    ## Draw objects with movement
    cv.drawContours(frame_a, contours, -1, (0, 255, 0), 2)

    ## Draw rectangules from object
    for contour in contours:
        ## Ignore tiny objects
        if cv.contourArea(contour) < 1000:
            continue

        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(frame_b, (x, y), (x+w, y+h), (0, 255,0), 2)
    
    ## Draw objects (better for shapes)
    for contour in contours:
        approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
        cv.drawContours(frame_c, [approx], -1, (0, 255, 0), 2)

    cv.imshow('Video', np.concatenate([frame1, frame_a, frame_b, frame_c], axis=1))

    ## Next frame
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break

cap.release()
cv.destroyAllWindows()