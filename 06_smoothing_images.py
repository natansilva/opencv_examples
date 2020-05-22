import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('images/lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
convolutional_2d =  cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
g_blur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateral_filter = cv.bilateralFilter(img, 9, 75, 75)

images = [img, convolutional_2d, blur, g_blur, median, bilateral_filter]
titles = ['Original', '2D Convolutional', 'Blur', 'Gaussian blur', 'Median', 'Bilateral']

plt.figure(figsize=[50, 30])
for image, title, i in zip(images, titles, range(1, len(images)+1)):
    plt.subplot(230+i)
    plt.imshow(image)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])

plt.show()