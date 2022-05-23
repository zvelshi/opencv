import cv2 as cv

img = cv.imread('./Resources/Photos/toronto.jpg')
cv.imshow('toronto', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("SIMP thresh", thresh)

# inverted simple thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("inv thresh", thresh_inv)

# adaptive thresholding - mean
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresh", adaptive_thresh)

# adaptive thresholding - gaussian
adaptive_thresh_gaus = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresh gaus", adaptive_thresh_gaus)

cv.waitKey(0)