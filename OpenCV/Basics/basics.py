import cv2
import imutils

# Normal Image
image = cv2.imread("jp.jpg")
(h, w, d) = image.shape
print(f"width={w}, height={h}, depth={d}")
cv2.imshow("Image", image)
cv2.waitKey(0)

# Cropped image
(B, G, R) = image[100, 50]
print(f"Red{R}, Blue{B}, Green{G}")
roi = image[30:190, 300:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Resized Image
resized = cv2.resize(image, (200, 200))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

# Undistorted Resized Image
r = 300.0 / w
dim = (300, int(r * h))
resized = cv2.resize(image, dim)
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

# Resize Using Imutils
resized = imutils.resize(image, width=800)
cv2.imshow("Resized", resized)
cv2.waitKey(0)

# Rotated Image
centre = (w//2, h//2)
M = cv2.getRotationMatrix2D(centre, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("RotatedImage", rotated)
cv2.waitKey(0)

# Rotating Using Imutils
rotated = imutils.rotate(image, -45)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)

# Non-Clipped Rotated Image
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)

# Smoothed Image
smoothed = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Smoothed Image", smoothed)
cv2.waitKey(0)

# Drawing Rectangle On Image
output = image.copy()
cv2.rectangle(output, (320, 60), (410, 180), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# Drawing Circle On Image
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -2)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# Drawing Line On Image
output = image.copy()
cv2.line(output, (120, 100), (400, 210), (0, 0, 255), 5)
cv2.imshow("line", output)
cv2.waitKey(0)

# Drawing Text On Image
output = image.copy()
cv2.putText(output, "Jurassic Park!", (55, 70),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
