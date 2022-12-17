import cv2
import imutils


# Loading Haar Cascade Detector
print("[INFO] loading face detector...")
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Loading Images
image = cv2.imread("image2.jpg")
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecting Faces Using HaarCascade
print("[INFO] Performing face detection!...")
rect = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=1, minSize=(30, 30),
                                 flags=cv2.CASCADE_SCALE_IMAGE)
print(f"[INFO] {len(rect)} faces detected!...")

# Looping over Bounding Boxes
for (x, y, w, h) in rect:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show Image
cv2.imshow("Detected Face", image)
cv2.waitKey(0)
