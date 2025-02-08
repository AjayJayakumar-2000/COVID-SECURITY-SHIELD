from tkinter import *
import datetime
import time
from threading import *
import face_recognition
import cv2
import numpy as np
import smtplib
import mysql.connector

root = Tk()

root.geometry("400x200")
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="barcodedb"
    )
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('projectg287@gmail.com','ajay221200')
notpresent = []
def Threading():
    t1 = Thread(target=attendancetime)
    t1.start()
attend = []
jk = []
known_face_names = [
                    "Abhijih Jayan",
                    "Ajay J Kumar",
                    "Chanthukrishnan J",
                    "Karthik P",
                    "R Padmanabhan"
                ]

def attendancetime():
    while True:

        set_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)


        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == set_time:
            print("attendance_closed")
            exit()
        else:
            try:
                video_capture = cv2.VideoCapture(0)
                jk = []
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

                file4image = face_recognition.load_image_file(
                    "/Users/ajayjayakumar/PycharmProjects/pythonProject6/face/AMSCU3CSC19038.jpg")
                face_landmarks_list4 = face_recognition.face_landmarks(file4image)
                face4_encoding = face_recognition.face_encodings(file4image)[0]

                file5image = face_recognition.load_image_file(
                    "/Users/ajayjayakumar/PycharmProjects/pythonProject6/face/AMSCU3CSC19053.jpg")
                face_landmarks_list5 = face_recognition.face_landmarks(file5image)
                face5_encoding = face_recognition.face_encodings(file5image)[0]

                known_face_encodings = [
                    face1_encoding,
                    face2_encoding,
                    face3_encoding,
                    face4_encoding,
                    face5_encoding
                ]

                known_face_names = [
                    "Abhijih Jayan",
                    "Ajay J Kumar",
                    "Chanthukrishnan J",
                    "Karthik P",
                    "R Padmanabhan"
                ]

                face_locations = []
                face_encodings = []
                face_names = []
                process_this_frame = True

                def Attendance(name):

                    with open('/Users/ajayjayakumar/PycharmProjects/pythonProject6/facerec/amark.csv', 'r+') as f:

                        if current_time == "13:16:00":
                            exit()


                        else:
                            myDataList = f.readlines()
                            nameList = []
                            for line in myDataList:
                                entry = line.split(',')
                                nameList.append(entry[0])
                            if name1 not in nameList:
                                now = datetime.now()
                                dtString = now.strftime('%H:%M:%S')
                                f.writelines(f'\n{name1},{dtString}')

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
                            name1 = "unknown"

                            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                name1 = known_face_names[best_match_index]
                                print(name1)
                                jk.append(name1)

                            face_names.append(name1)
                    process_this_frame = not process_this_frame

                    for (top, right, bottom, left), name1 in zip(face_locations, face_names):
                        top *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4

                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(frame, name1, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                        Attendance(name1)




            except KeyboardInterrupt:
                print('KeyboardInterrupt exception is caught')
            else:
                print('No exceptions are caught')

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            video_capture.release()
            cv2.destroyAllWindows()








Label(root, text="attendance_timer", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set_timer", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()


for i in known_face_names:
    if i not in jk:
        notpresent.append(i)
notpresent =list(dict.fromkeys(notpresent))

mailid =[]
for j in notpresent:
    mycursor = mydb.cursor(buffered=True)
    q = 'SELECT ParentsMailId FROM STUDENTS where Name = \'' + j + '\''
    mycursor.execute(q)
    users = mycursor.fetchone()
    mailid.append(users[0])
print(mailid)

for k in mailid:
    server.sendmail('projectg287@gmail.com', k, 'your son absent today')
    print("mail send")






