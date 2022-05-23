import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # 500,500 = width,height, 3 = num colour channels
cv.imshow("Blank", blank)

#img = cv.imread("Photos/cat1.jpg")
#cv.imshow("Cat", img)

# 1. paint the image a certain colour
#blank[:] = 0,0,255 <-- paint whole image
#blank[200:300, 300:400] = 0,0,255 <-- paint a range in an image
#cv.imshow("Green", blank)

# 2. draw a rectangle
#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) #<-- to fill the rectangle, thickness=cv.FILLED or -1
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) #<-- defining boundaries by shape of img
#cv.imshow("Rectangle", blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
#cv.imshow("Circle", blank)

# 4. draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
#cv.imshow("Line", blank)

# 5. writing text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)

