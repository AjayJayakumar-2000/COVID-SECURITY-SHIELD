import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime
AT = "/Users/ajayjayakumar/PycharmProjects/pythonProject6/face"
face = []
BCA =[]
lIst = os.listdir(AT)
print(lIst)
for cls in lIst:
    currentImg = cv2.imread(f'{AT}/{cls}')
    face.append(currentImg)
    BCA.append(os.path.splitext(cls)[0])
print(BCA)


def findEncodings(face):
    face_encodings_list = []
    for fa in face:
        fa = cv2.cvtColor(fa, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(fa)[0]
        face_encodings_list.append(encode)
    return face_encodings_list

def Attendance(name):
    with open('/Users/ajayjayakumar/PycharmProjects/pythonProject6/ajay.csv', 'r+') as f:
        myDataList = f.readlines()
    nameList = []
    for line in myDataList:
        entry = line.split(',')
    nameList.append(entry[0])
    if name not in nameList:
        now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    f.writelines(f'n{name},{dtString}')

encodeListKnown = findEncodings(face)
print('Encoding Complete')

video_capture = cv2.VideoCapture(0)


'''file1image = face_recognition.load_image_file("/Users/ajayjayakumar/PycharmProjects/pythonProject6/face/ajay.jpg")
face_landmarks_list = face_recognition.face_landmarks(file1image)
face1_encoding = face_recognition.face_encodings(file1image)[0]

known_face_encodings = [
    face1_encoding
]
known_face_names = [
    "ajay"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True   '''''

while True:

    done, frame = video_capture.read()


    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)


    rgb_small_frame = small_frame, cv2.COLOR_BGR2RGB

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(face_encodings_list, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(face_encodings_list, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:

                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,(left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()