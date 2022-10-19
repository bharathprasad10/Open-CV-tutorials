import cv2
import random
img = cv2.imread('green.JPG',-1)

'''
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randrange(255),random.randrange(255),random.randrange(255)]
'''

tag = img[300:400,400:500]
img[100:200,300:400] = tag

print(img.shape)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()