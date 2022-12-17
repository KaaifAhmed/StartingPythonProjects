import cv2
import imutils

# Reading The Images
image = cv2.imread('finding_shapes.png')

# Finding All The Black Shapes
lower, upper = (0, 0, 0), (15, 15, 15)
shape_mask = cv2.inRange(image, lower, upper)
cv2.imshow('Masked Images', shape_mask)
cv2.waitKey(0)

# Finding The Contours In The Mask
cnts = cv2.findContours(shape_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Looping Over The Contours And Drawing Them
for c in cnts:
    cv2.drawContours(image, c, -1, (0, 255, 255), 5)
    cv2.imshow('Shapes', image)
    cv2.waitKey(0)
