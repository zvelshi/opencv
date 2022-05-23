import cv2 as cv

img = cv.imread('./Resources/Photos/cat1.jpg')

def rescaleFrame(frame,scale=0.25):
    # will work for images, videos, live sources
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # will work for live video
    capture.set(3,width)
    capture.set(4,height)

cv.imshow('Cat', rescaleFrame(img))
cv.waitKey(0)

