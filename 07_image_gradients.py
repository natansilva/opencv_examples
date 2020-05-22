import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


## Read image
img = cv.imread('images/sudoku.jpg')

## Apply laplacian filter to detect edges
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0)
sobel_x = np.uint8(np.absolute(sobel_x))

sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1)
sobel_y = np.uint8(np.absolute(sobel_y))

sobel_combined = cv.bitwise_or(sobel_x, sobel_y)

## Show images and filters
images = [img, lap, sobel_x, sobel_y, sobel_combined]
titles = ['Original', 'Laplacian', 'SobelX', 'SobelY', 'Combined sobel']
for image, title, i in zip(images, titles, range(1, len(images)+1)):
    plt.subplot(230+i)
    plt.imshow(image)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])

plt.show()