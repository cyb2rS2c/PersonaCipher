import face_recognition
import cv2
import numpy as np
import os
import pyfiglet
from colorama import Fore, init

init(autoreset=True)


# Global lists for known face encodings and names
known_face_encodings = []
known_face_names = []


def create_ascii_art_with_author(project_name, author_name):
    project_ascii = pyfiglet.figlet_format(project_name, font="slant")  # Customize the font as needed
    print(project_ascii)
    print(Fore.RED + f"Author: {author_name}")

# Load known faces from the dataset
def load_known_faces(dataset_dir='dataset2'):
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
    # Open the video file
    video_capture = cv2.VideoCapture(mp4_path)

    # Check if video was opened successfully
    if not video_capture.isOpened():
        print(f"Error opening video file {mp4_path}")
        return

    found_match = False  # Flag to check if any known faces were found

    while True:
        ret, frame = video_capture.read()
        if not ret or frame is None:
            print("No frame detected or end of video.")
            break  # Exit the loop if no frame is captured or video ends

        # Convert the image from BGR (OpenCV format) to RGB (face_recognition format)
        rgb_frame = frame[:, :, ::-1]

        # Detect face locations
        face_locations = face_recognition.face_locations(rgb_frame)
        print(f"Detected {len(face_locations)} faces in the current frame.")

        if face_locations:
            try:
                # Encode the detected faces
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                # Ensure that we have encodings for all detected faces
                if len(face_encodings) == len(face_locations):
                    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                        # Check if the face matches a known encoding
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = "Unknown"

                        # Find the best match index
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)

                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                            found_match = True  # Set flag if a known face is found

                        # Draw a box around the face
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                        # Label the face with the name
                        cv2.putText(frame, name, (left + 6, bottom + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                else:
                    print("Mismatch between face locations and encodings detected.")
            except Exception as e:
                print(f"Error in face encoding: {e}")

        else:
            print("No faces detected in this frame.")

        # Display the video frame
        cv2.imshow('Video', frame)

        # Break from the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After processing the video, check if any known faces were found
    if found_match:
        print("Known faces were detected in the video.")
    else:
        print("No known faces were detected in the video.")

    # Release the video capture object and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

# Main menu to run the application
def main_menu():
    project_name = "Face Recognition Application"
    author_name = "cyb2rS2c"
    create_ascii_art_with_author(project_name, author_name)
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
            break
        else:
            print("Invalid choice. Please select again.")

# Run the application
if __name__ == "__main__":
    main_menu()
