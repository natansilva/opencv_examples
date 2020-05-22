import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 300)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 300)

fgbg = cv.createBackgroundSubtractorMOG2()
fgknn = cv.createBackgroundSubtractorKNN()


while cap.isOpened():
    ret, frame = cap.read()

    bg_mask = fgbg.apply(frame)
    bg_frame = cv.bitwise_or(frame, frame, mask=bg_mask)

    knn_mask = fgknn.apply(frame)
    knn_frame = cv.bitwise_or(frame, frame, mask=knn_mask)

    cv.imshow('Image', np.concatenate([frame, bg_frame, knn_frame], axis=1))

    if cv.waitKey(30) == 27:
        break

cap.release()
cv.destroyAllWindows()