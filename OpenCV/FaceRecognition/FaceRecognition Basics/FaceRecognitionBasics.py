import face_recognition
import imutils
import cv2


img_elon = cv2.imread('ElonMusk.jpg')
img_test = cv2.imread('ElonTest.jpg')

loc = face_recognition.face_locations(img_elon)[0]
enc = face_recognition.face_encodings(img_elon)[0]
cv2.rectangle(img_elon, (loc[3], loc[0]), (loc[1], loc[2]), (0, 0, 255), 2)

loc_test = face_recognition.face_locations(img_test)[0]
enc_test = face_recognition.face_encodings(img_test)[0]
cv2.rectangle(img_test, (loc_test[3], loc_test[0]), (loc_test[1], loc_test[2]), (0, 0, 255), 2)

img_elon = imutils.resize(img_elon, height=300)
img_test = imutils.resize(img_test, height=300)

result = face_recognition.compare_faces([enc], enc_test)
face_dis = face_recognition.face_distance([enc], enc_test)
print(face_dis)
print(result)
cv2.putText(img_test, f"{result} {round(face_dis[0], 2)}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('ElonMusk', img_elon)
cv2.imshow('ElonTest', img_test)
cv2.waitKey(0)
