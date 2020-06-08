import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('peccy.png')
hist, bins = np.histogram(img.flatten(),255,[0,256])

plt.plot(hist)
plt.show()

# Cumulative Histogram

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(),256,[0,256],color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'),loc='upper left')
plt.show()
