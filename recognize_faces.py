import os
import csv
import cv2
import face_recognition
import pickle
from datetime import datetime
import numpy as np
from playsound import playsound

def log_attendance(name, log_file='attendance.csv'):
    file_exists = os.path.isfile(log_file)
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Name', 'Date', 'Time', 'Status'])  # Header
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        time = now.strftime('%H:%M:%S')
        writer.writerow([name, date, time, 'Present'])


ENCODINGS_FILE = 'data/known_faces_encodings.pkl'

with open(ENCODINGS_FILE, 'rb') as f:
    known_encodings, known_names = pickle.load(f)

video = cv2.VideoCapture(0)
recognized_faces = set()

print("[INFO] Starting webcam. Press 'q' to quit.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Resize frame and convert to RGB correctly
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    try:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]
                if name not in recognized_faces:
                    recognized_faces.add(name)
                    log_attendance(name)
                    print(f"[LOG] {name} recognized at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    playsound(r'C:\Windows\Media\tada.wav')

            top, right, bottom, left = [v * 4 for v in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    except Exception as e:
        print(f"[ERROR] face_recognition failed: {e}")

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
