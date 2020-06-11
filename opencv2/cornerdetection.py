import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/manishrai/PycharmProjects/OpenCV/220px-Lenna_(test_image).png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
#kernel = np.ones((5,5),np.float32)/25

dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
img[dst>dst.max()/4] = [0,255,0]
plt.subplot(121)
plt.imshow(img),plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(dst)
plt.title('Corner')
plt.show()
