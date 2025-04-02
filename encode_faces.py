import os
import face_recognition
import pickle

KNOWN_FACES_DIR = 'data/known_faces'
ENCODINGS_FILE = 'data/known_faces_encodings.pkl'

def encode_known_faces():
    known_encodings = []
    known_names = []

    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            name = os.path.splitext(filename)[0]
            filepath = os.path.join(KNOWN_FACES_DIR, filename)
            image = face_recognition.load_image_file(filepath)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(name)
                print(f"[+] Encoded {name}")
            else:
                print(f"[!] No face found in {filename}")

    # Save encodings to file
    with open(ENCODINGS_FILE, 'wb') as f:
        pickle.dump((known_encodings, known_names), f)

    print(f"\n✅ Saved {len(known_encodings)} face encodings to {ENCODINGS_FILE}")

if __name__ == "__main__":
    encode_known_faces()
