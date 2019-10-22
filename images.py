# packages
import cv2 as cv

# convrting image to numpy array
new_image = np.asarray(image)

# plotting image in grayscale
plt.imshow(image, cmap='gray')

# applying adaptive thresholding with CV2
new_image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 1)
new_image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 1)

