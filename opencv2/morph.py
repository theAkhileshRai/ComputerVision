import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/manishrai/PycharmProjects/OpenCV/220px-Lenna_(test_image).png',0)

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations= 1)
dilate = cv2.dilate(img,kernel,iterations=1)
plt.subplot(131)
plt.imshow(img),plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(132)
plt.imshow(erosion)
plt.subplot(133)
plt.imshow(dilate)
plt.title('Erode')
plt.show()
