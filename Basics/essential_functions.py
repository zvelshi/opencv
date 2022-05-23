from configparser import Interpolation
import cv2 as cv

img = cv.imread("./Resources/Photos/toronto.jpg")
#cv.imshow("Cat", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray", gray)

# blur and image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #adjust (x,x) for level of blur, x must be odd
#cv.imshow("Blur", blur)

# edge cascade (edge detection)
canny = cv.Canny(blur, 125, 175) #use blurred source image for better edge detection
cv.imshow("Canny", canny)

# dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("Dialated", dilated)

# eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

# resizing the image
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Redsize", resize)

# cropping the image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey()