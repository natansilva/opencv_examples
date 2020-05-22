import cv2 as cv

## Using first camera on device
cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    ## If frame is not read correctly close camera
    if ret != True:
        break
    
    ## Close camera if "q" is press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    cv.imshow('frame', frame)

## Release the camera and close windows
cap.release()
cv.destroyAllWindows()