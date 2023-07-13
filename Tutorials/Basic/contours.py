import cv2 as cv
import numpy as np

img = cv.imread('../Photos/bird1.jpg')
cv.imshow('Bird', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# mode = cv.RETR_LIST for all contours, RETR_EXTERNAL only external, RETR_TREE for all hierarchical contour approx
# method = CHAIN_APPROX_NONE returns nothing (all points within a line), APPROX_SIMPLE to compress and finds end points
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
