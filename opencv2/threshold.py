import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/manishrai/PycharmProjects/OpenCV/220px-Lenna_(test_image).png',0)

ret,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)

ret4,th4 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['Global Thresholding', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding','OTSU']

images = [th1,th2,th3,th4]

for i in range(len(images)):
    plt.subplot(2,2,1+i),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


