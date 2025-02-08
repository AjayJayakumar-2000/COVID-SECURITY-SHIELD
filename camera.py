import face_recognition
import cv2
import numpy as np
from datetime import datetime

try:
    video_capture = cv2.VideoCapture(0)
    current_time = datetime.now().strftime("%H:%M:%S")
    attend = []
    file1image = face_recognition.load_image_file(
        "/Users/ajayjayakumar/PycharmProjects/pythonProject6/face/AMSCU3CSC19002.jpg")
    face_landmarks_list1 = face_recognition.face_landmarks(file1image)
    face1_encoding = face_recognition.face_encodings(file1image)[0]

    file2image = face_recognition.load_image_file(
        "/Users/ajayjayakumar/PycharmProjects/pythonProject6/face/AMSCU3CSC19008.jpg")
    face_landmarks_list2 = face_recognition.face_landmarks(file2image)
    face2_encoding = face_recognition.face_encodings(file2image)[0]

    file3image = face_recognition.load_image_file(
        "/Users/ajayjayakumar/PycharmProjects/pythonProject6/face/AMSCU3CSC19024.jpg")
    face_landmarks_list3 = face_recognition.face_landmarks(file3image)
    face3_encoding = face_recognition.face_encodings(file3image)[0]



    file5image = face_recognition.load_image_file(
        "/Users/ajayjayakumar/PycharmProjects/pythonProject6/face/AMSCU3CSC19053.jpg")
    face_landmarks_list5 = face_recognition.face_landmarks(file5image)
    face5_encoding = face_recognition.face_encodings(file5image)[0]

    known_face_encodings = [
        face1_encoding,
        face2_encoding,
        face3_encoding,
        face5_encoding
    ]

    known_face_names = [
        "Abhijih Jayan",
        "Ajay J Kumar",
        "Chanthukrishnan J",
        "R Padmanabhan"
    ]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True


    def Attendance(name):
        with open('/Users/ajayjayakumar/PycharmProjects/pythonProject6/facerec/amark.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name1 not in nameList :
                now = datetime.now()
                attend.append(name1)

                #print(jk)
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name1},{dtString}')
            print(attend)

    def npresent():
        print("not present")
        notpresent = []
        for i in known_face_names:
                if i not in attend:
                    notpresent.append(i)
    while True:

        done, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:

                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name1 = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name1 = known_face_names[best_match_index]

                face_names.append(name1)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name1, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            Attendance(name1)
            npresent()
        cv2.imshow('Video', frame)
        cv2.waitKey(1)

except KeyboardInterrupt:
    print('KeyboardInterrupt exception is caught')
else:
    print('No exceptions are caught')







