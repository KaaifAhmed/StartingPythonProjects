# Importing Necessary Packages
import cv2
import imutils
from imutils.perspective import four_point_transform
from skimage.filters import threshold_local


# Loading Image And Finding The Ratio
image = cv2.imread('Document3.jpg')
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height=500)

# Converting Image To Grayscale, Blurring It And Finding Edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

# Showing The Images
print('STEP:1 EDGES DETECTION ')
cv2.imshow("Image", image)
cv2.imshow("Edged Image", edged)
cv2.waitKey(0)

# Finding The Contours And Keeping The Largest One
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]


# Looping OVer The Contours
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # If The Approximated Contour Has Four Edges Then We Pass It
    if len(approx) == 4:
        screenCnt = approx
        break

# Showing The Outline Of The Image
print('STEP:2 FIND CONTOURS OF THE IMAGE')
try:
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
except NameError:
    print("Invalid Image")

cv2.imshow('Outline', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying Four Point Transform To Take A Top-Down Image
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

# Converting The Image To Grayscale AND Thresholding It To Give It A Black&White Paper Effect
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset=10, method="gaussian")
warped = (warped > T).astype("uint8") * 255

# Show Scanned Images
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height=650))
cv2.imshow("Scanned", imutils.resize(warped, height=650))
cv2.waitKey(0)
