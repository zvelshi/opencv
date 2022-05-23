import cv2 as cv

img = cv.imread("./Resources/Photos/toronto.jpg")
cv.imshow("Img", img)

# bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Img1", gray)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("Img2", hsv)

# bgr to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Img3", lab)

# bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("Img4", rgb)

cv.waitKey(0)