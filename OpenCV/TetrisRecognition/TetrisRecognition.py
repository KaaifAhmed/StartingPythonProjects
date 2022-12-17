import cv2
import imutils as im


# Read The Image
image = cv2.imread("tetris_blocks.png")
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# Convert Color To Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# cv2.waitKey(0)

# Finding The Edges
edged = cv2.Canny(gray, 30, 200)
# cv2.imshow("Edges", edged)
# cv2.waitKey(0)

# Thresholding The Image
thresh = cv2.threshold(gray, 225, 225, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)

# Thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = im.grab_contours(cnts)
output = image.copy()


# Drawing Contours
for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours Image", output)
    cv2.waitKey(0)

# Putting The Text On The Image
text = f'I found {len(cnts)} objects!'
cv2.putText(output, text,  (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (240, 0, 159), 2)
cv2.imshow("Text On Image", output)
cv2.waitKey(0)

# Erosion To Reduce Noise
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

# Dilations To Increase The size
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Image", mask)
cv2.waitKey(0)

# Masking The Image
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)
