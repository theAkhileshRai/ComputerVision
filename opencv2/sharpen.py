import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/manishrai/PycharmProjects/OpenCV/220px-Lenna_(test_image).png',0)

kernel = np.ones((5,5),np.float32)/25

dst = cv2.Canny(img,100,100)

plt.subplot(121)
plt.imshow(img),plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(dst)
plt.title('Sharpen')
plt.show()
