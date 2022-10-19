import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    width = int(cap.get(3))   # 3 corresponds to the property "width"
    height = int(cap.get(4))  # 4 corresponds to the property "height"

    image = np.zeros(frame.shape, np.uint8)  # a black screen with the shape of frame

    img = cv2.line(frame,(0,0),(width,height), (255,0,0), 10)    #Line
    img = cv2.line(img,(0,height),(width,0), (0,255,0), 5)
    img = cv2.rectangle(img,(100,100),(200,200),(128,230,150), 7) #Rectangle
    img = cv2.circle(img,(300,300),50,(0,0,255),-1)    #Circle
# Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Bharath is Awesome', (10,height - 10), font,2,(230,200,230), 5, cv2.LINE_AA)

    cv2.imshow('frame',img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()