# PersonaCipher

> **Your face recognizer in images and videos.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green?logo=linux)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-3.0-orange)

---

## 🧠 Overview

**Face Recognition Application** is a Python-based face recognition project using the `face_recognition` and `OpenCV` libraries. The application allows users to recognize faces in images and videos using a preloaded dataset of known faces.

## Features
- Load known faces from a dataset.
- Recognize faces in a given image.
- Recognize faces in a given video.
- User-friendly command-line interface.

## Requirements
```bash
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install face_recognition opencv-python numpy dlib requests bs4 pyfiglet colorama;python3 -m pip install --upgrade pip setuptools wheel
```

## Usage
### Clone the repository:

For Windows using powershell (download the zip file ):
    
    curl -o PersonaCipher.zip  https://github.com/cyb2rS2c/PersonaCipher/archive/refs/heads/main.zip
    Expand-Archive -Force  .\PersonaCipher.zip
    cd PersonaCipher/PersonaCipher-main

Note: you need to install the same tools on windows in order to work.

For Linux:
    
    git clone https://github.com/cyb2rS2c/PersonaCipher.git
    cd PersonaCipher
    
### 1. Prepare the Dataset
Place images of known people inside a dataset directory (default: `dataset2`). Each person's images should be inside a folder named after them. Example structure:

```
dataset2/
  ├── John_Doe/
  │   ├── img1.jpg
  │   ├── img2.jpg
  ├── Jane_Smith/
  │   ├── img1.jpg
  │   ├── img2.jpg
```

### Note: you can skip creating **/dataset2** manually and just edit the **usernames.txt** and then create it automatically using:
```bash
python3 create_dataset.py
```

### 2. Run the Application
Execute the script using:

```bash
python3 persona_cipher.py
```

### 3. Select an Option from the Menu
- **Recognize faces in an image**: Provide the image path when prompted.
- **Recognize faces in a video**: Provide the video file path when prompted.
- **Exit**: Close the application.

## Functionality Overview

### `load_known_faces(dataset_dir='dataset2')`
Loads face encodings from the dataset directory and stores them for recognition.

### `recognize_faces_in_image(image_path)`
- Detects and recognizes faces in a provided image.
- Draws a rectangle around recognized faces and labels them.

### `recognize_faces_in_video(mp4_path)`
- Processes frames from a video file.
- Detects and recognizes known faces in real-time.
- Draws bounding boxes and labels recognized faces.

### `main_menu()`
A user-friendly menu to select image or video recognition.

### Support for fetching 10 images related to each username in **usernames.txt**:
```bash
python3 create_dataset.py
```

## Screenshots
<img width="576" height="560" alt="face" src="https://github.com/user-attachments/assets/171ea466-b5e4-48ec-ba38-fe0e37133e4b" />
<img width="1038" height="355" alt="Screenshot_2025-11-13_15-00-02" src="https://github.com/user-attachments/assets/51961531-abe0-4265-b3a3-7648fbc99704" />



## Notes
- The face recognition model uses the HOG-based feature extraction method.
- Ensure to edit the usernames inside the **usernames.txt** and then run the create_dataset.py as shown above.
- You can adjust the face matching threshold (`0.6` in the script) to fine-tune accuracy.
- The program has been tested on a linux machine, make sure to follow other guids on how to install the dependencies mentioned above for windows.
- It’s simple to run on both Linux and Windows after installing the required dependencies.
- Press `q` to exit video processing.


## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

