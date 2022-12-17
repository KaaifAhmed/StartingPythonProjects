import cv2
import face_recognition
import numpy as np
import imutils
import os
from datetime import datetime


path = 'AttendanceList'
attendance_img = cv2.imread('DwayneJohnson.jpg')
Images = []
ClassNames = []
AttendanceList = os.listdir(path)


for cl in AttendanceList:
    img = cv2.imread(f'{path}/{cl}')
    Images.append(img)
    ClassNames.append(str(cl.split(".")[0]))
print('[INFO] Images Read!...')


def find_encodings(imgs):
    encoding_list = []
    for i in imgs:
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        i = face_recognition.face_encodings(i)[0]
        encoding_list.append(i)
    return encoding_list


def mark_attendance(nm):
    with open('AttendanceFile.csv', 'r+') as f:
        my_data_list = f.readlines()
        time_list = []
        now = datetime.now()
        a_time = now.strftime('%H:%M')
        c_time = a_time + '\n'

        for line in my_data_list:
            entry = line.split(",")
            time = entry[1]
            time_list.append(time)

        if c_time not in time_list:
            f.writelines(f"{nm},{c_time}")


encodeList = find_encodings(Images)
print('[INFO] Encoding Complete!...')


attendance_img = cv2.cvtColor(attendance_img, cv2.COLOR_BGR2RGB)
print('[INFO] Comparison Image Loaded Successfully!...')

comp_img_enc = face_recognition.face_encodings(attendance_img)[0]
print('[INFO] Comparison Image Encoded Successfully!...')

print('[INFO] Comparing The Images...')

result = face_recognition.compare_faces(encodeList, comp_img_enc)
face_dis = face_recognition.face_distance(encodeList, comp_img_enc)
matchIndex = np.argmin(face_dis)

if result[matchIndex]:
    name = ClassNames[matchIndex]

    print(f'[INFO] The Image Matched Successfully with {name}')

    attendance_img = cv2.cvtColor(attendance_img, cv2.COLOR_RGB2BGR)
    attendance_img = imutils.resize(attendance_img, width=400)
    face_loc = face_recognition.face_locations(attendance_img)[0]

    cv2.rectangle(attendance_img, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 255, 0), 2)
    cv2.rectangle(attendance_img, (face_loc[3] - 1, face_loc[2]), (face_loc[1] + 1, face_loc[2] + 25),
                  (0, 255, 0), cv2.FILLED)
    cv2.putText(attendance_img, name, (face_loc[3] + 6, face_loc[2] + 18),
                cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

    mark_attendance(name)

    cv2.imshow('Matches Found', attendance_img)
    cv2.waitKey(0)
else:
    print('[INFO] No Matches Found!')

    attendance_img = cv2.cvtColor(attendance_img, cv2.COLOR_RGB2BGR)
    attendance_img = imutils.resize(attendance_img, width=500)
    face_loc = face_recognition.face_locations(attendance_img)[0]

    cv2.rectangle(attendance_img, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 0, 355), 2)
    cv2.rectangle(attendance_img, (face_loc[3] - 1, face_loc[2]), (face_loc[1] + 1, face_loc[2] + 25),
                  (0, 0, 255), cv2.FILLED)
    cv2.putText(attendance_img, 'No Matches Found!', (face_loc[3] + 6, face_loc[2] + 18),
                cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('No Matches Found! ', attendance_img)
    cv2.waitKey(0)
