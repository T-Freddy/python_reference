# import packages
import cv2 as cv
import pytesseract
from scipy import ndimage

# convrting image to numpy array
new_image = np.asarray(image)

# plotting image in grayscale
plt.imshow(image, cmap='gray')
# applying adaptive thresholding with CV2
new_image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 1)
new_image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 1)

# denoising
new_image = ndimage.median_filter(image, 3)

# image to text
text = pytesseract.image_to_string(image, lang='eng')
