import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    width = int(cap.get(3))   # 3 corresponds to the property "width"
    height = int(cap.get(4))  # 4 corresponds to the property "height"

    #Convert colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Extract particular color and show it
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(frame,lower_blue,upper_blue)
    result = cv2.bitwise_and(frame,frame, mask = mask)

    cv2.imshow('frame', result)

    #cv2.imshow('frame', hsv)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()