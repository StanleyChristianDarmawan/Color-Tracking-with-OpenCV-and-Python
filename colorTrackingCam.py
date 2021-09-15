import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # convert BGR frame to HSV for better detection
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    #Pick lower and upper color in HSV value to track
    lower_color = np.array([90, 50, 50])
    upper_color = np.array([130, 255, 255])

    # mask will keep the ordered area and blackout the unbooked area
    mask = cv.inRange(hsv, lower_color, upper_color)

    # Comparing the bit from mask to the bit of frame and if this return one then it will keep that pixel
    output = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Color Tracking', output)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()