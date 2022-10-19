import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    width = int(cap.get(3))   # 3 corresponds to the property "width"
    height = int(cap.get(4))  # 4 corresponds to the property "height"

    image = np.zeros(frame.shape, np.uint8)  # a black screen with the shape of frame

    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) # resizing the frame by 1/4th

    image[:height//2, :width//2] = smaller_frame #placing the frame in the top left corner
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame
    cv2.imshow('frame',image)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()