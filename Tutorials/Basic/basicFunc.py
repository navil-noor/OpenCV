import cv2 as cv

img = cv.imread('../Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)  # ksize is always odd number
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)  # use blur to decrease edges
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding (gets back from dilated to canny)
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
# interpolation inter_area is default for shrinking the image
# use inter_linear or inter_cubic (slowest but best quality) for enlarging image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
