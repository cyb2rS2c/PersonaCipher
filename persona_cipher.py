import face_recognition
import cv2
import numpy as np
import os
import pyfiglet
from colorama import Fore, init
import platform

init(autoreset=True)

# Global lists for known face encodings and names
known_face_encodings = []
known_face_names = []


def clear_screen():
    current_os = platform.system()
    if current_os in ["Linux", "Darwin"]:
        os.system("clear")
    elif current_os == "Windows":
        os.system("cls")

def create_ascii_art_with_author(project_name, author_name,author_description):
    project_ascii = pyfiglet.figlet_format(project_name, font="poison")
    print(Fore.RED+project_ascii)
    print(Fore.MAGENTA + f"{author_description}")
    print(Fore.RED + f"Author: {author_name}")

# Load known faces from the dataset
def load_known_faces(dataset_dir='known_faces'):
    for person_name in os.listdir(dataset_dir):
        person_dir = os.path.join(dataset_dir, person_name)
        if not os.path.isdir(person_dir):
            continue
        for img_file in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_file)
            if os.path.isfile(img_path):  # Only proceed if it's a file
                image = face_recognition.load_image_file(img_path)
                face_encodings = face_recognition.face_encodings(image)
                if len(face_encodings) > 0:
                    known_face_encodings.append(face_encodings[0])
                    known_face_names.append(person_name)

    print("Encoded faces for recognition.")

# Recognize faces in a given image
def recognize_faces_in_image(image_path):
    image_to_recognize = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image_to_recognize)

    if not face_locations:
        print("No faces found in the image.")
        return

    face_encodings = face_recognition.face_encodings(image_to_recognize, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index] and face_distances[best_match_index] < 0.6:  # Adjust threshold as necessary
            name = known_face_names[best_match_index]

        # Draw a box around the face
        cv2.rectangle(image_to_recognize, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image_to_recognize, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Convert to BGR for OpenCV display
    bgr_image = cv2.cvtColor(image_to_recognize, cv2.COLOR_RGB2BGR)
    cv2.imshow('Recognized Faces', bgr_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()

# Recognize faces in a given video
def recognize_faces_in_video(mp4_path):
    video_capture = cv2.VideoCapture(mp4_path)

    if not video_capture.isOpened():
        print(f"Error opening video file {mp4_path}")
        return

    found_match = False

    while True:
        ret, frame = video_capture.read()
        if not ret or frame is None:
            print("End of video or no frame.")
            break
        rgb_frame = frame[:, :, ::-1]
        small_frame = cv2.resize(rgb_frame, (0, 0), fx=0.5, fy=0.5)
        face_locations_small = face_recognition.face_locations(small_frame, model="hog")
        face_encodings = face_recognition.face_encodings(small_frame, face_locations_small)
        scaled_locations = []
        for (top, right, bottom, left) in face_locations_small:
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            scaled_locations.append((top, right, bottom, left))
        for (top, right, bottom, left), face_encoding in zip(scaled_locations, face_encodings):

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

            name = "Unknown"

            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    found_match = True
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if found_match:
        print("Known faces detected.")
    else:
        print("No known faces detected.")

    video_capture.release()
    cv2.destroyAllWindows()
def main_menu():
    project_name = "PersonaCipher"
    author_name = "cyb2rS2c"
    author_description = "Your face recognizer in images & videos."
    create_ascii_art_with_author(project_name, author_name,author_description)
    load_known_faces()
    while True:
        print("\nFace Recognition Menu")
        print("1. Recognize faces in an image")
        print("2. Recognize faces in a video")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            image_path = input("Enter the path of the image: ")
            recognize_faces_in_image(image_path)
        elif choice == '2':
            video_path = input("Enter the path of the video: ")
            recognize_faces_in_video(video_path)
        elif choice == '3':
            print("Exiting the program.")
            clear_screen()
            break
        else:
            print("Invalid choice. Please select again.")

# Run the application
if __name__ == "__main__":
    main_menu()
