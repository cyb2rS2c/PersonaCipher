# PersonaCipher

> **Your face recognizer in images and videos.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green?logo=linux)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-5.0-orange)

---
## 🧠 Overview

**PersonaCipher** is a Python-based face recognition project using the `face_recognition` and `OpenCV` libraries. The application allows users to recognize faces in images and videos using a preloaded dataset of known faces.

## ✨ Features

✔️ **Recognize faces in images**

✔️ **Recognize faces in videos (MP4)**

✔️ **Auto-scale frames for fast performance**

✔️ **Auto-create datasets from usernames**

✔️ **Automatic image fetching (10 per user)**

✔️ **MP4 downloader for online videos**

✔️ **CLI interface with ASCII art banner**

✔️ **Windows & Linux compatible**

Note:  If you are using linux then go read the [TODO](TODO.md) to set everything automatically.
## Project tree:
```
├── assets
│   ├── images
│   │   └── image.png
│   ├── known_faces
│   │   ├── Elon_Musk
│   │   │   ├── img10.jpg
│   │   │   ├── img1.jpg
│   │   │   ├── img2.jpg
│   │   │   ├── img3.jpg
│   │   │   ├── img4.jpg
│   │   │   ├── img5.jpg
│   │   │   ├── img6.jpg
│   │   │   ├── img7.jpg
│   │   │   ├── img8.jpg
│   │   │   └── img9.jpg
│   │   ├── John_Doe
│   │   │   ├── img10.jpg
│   │   │   ├── img1.jpg
│   │   │   ├── img2.jpg
│   │   │   ├── img3.jpg
│   │   │   ├── img4.jpg
│   │   │   ├── img5.jpg
│   │   │   ├── img6.jpg
│   │   │   ├── img7.jpg
│   │   │   ├── img8.jpg
│   │   │   └── img9.jpg
│   │   ├── Messi
│   │   │   ├── img10.jpg
│   │   │   ├── img1.jpg
│   │   │   ├── img2.jpg
│   │   │   ├── img3.jpg
│   │   │   ├── img4.jpg
│   │   │   ├── img5.jpg
│   │   │   ├── img6.jpg
│   │   │   ├── img7.jpg
│   │   │   ├── img8.jpg
│   │   │   └── img9.jpg
│   │   └── Ronaldo
│   │       ├── img10.jpg
│   │       ├── img1.jpg
│   │       ├── img2.jpg
│   │       ├── img3.jpg
│   │       ├── img4.jpg
│   │       ├── img5.jpg
│   │       ├── img6.jpg
│   │       ├── img7.jpg
│   │       ├── img8.jpg
│   │       └── img9.jpg
│   └── videos
│       └── video.mp4
├── datasets
│   └── usernames.txt
├── face_recognition
│   ├── api.py
│   ├── face_detection_cli.py
│   ├── face_recognition_cli.py
│   └── __init__.py
├── LICENSE
├── README.md
├── requirements.txt
├── setup.sh
└── src
    ├── create_dataset.py
    ├── mp4_downloader.py
    └── persona_cipher.py

```
## Requirements
```bash
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt
```
Note: if you counter any issue with `pip`, execute this command manually:
```bash
python3 -m pip install --upgrade pip setuptools wheel
```
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
Place images of known people inside a dataset directory (default: `known_faces`). Each person's images should be inside a folder named after them. Example structure:

```
 assets├── 
    known_faces/
      ├── John_Doe/
      │   ├── img1.jpg
      │   ├── img2.jpg
      ├── Jane_Smith/
      │   ├── img1.jpg
      │   ├── img2.jpg
```

But you do not need to create it manually.
### Auto-Generate Dataset
1. Edit the names in `usernames.txt`
2. Run:
```bash
python3 create_dataset.py
```
The script will:

1. Create folders
2. Download 10 images per user
3. Build a complete dataset automatically

## Usage
### Run PersonaCipher
```bash
python3 persona_cipher.py
```
### Menu Options 
- **Recognize faces in an image**: Provide the image path when prompted.
- **Recognize faces in a video**: Provide the video file path when prompted.
- **Exit**: Close the application.

## Functionality Overview

### MP4 Downloader
Download any video URL:
```bash
python3 mp4_downloader.py
```
### `load_known_faces()`
Loads face encodings from the dataset directory and stores them for recognition.

### `recognize_faces_in_image()`
- Detects and recognizes faces in a provided image.
- Draws a rectangle around recognized faces and labels them.

### `recognize_faces_in_video()`
- Processes frames from a video file.
- Detects and recognizes known faces in real-time.
- Draws bounding boxes and labels recognized faces.

## Screenshots
<img width="576" height="560" alt="face" src="https://github.com/user-attachments/assets/171ea466-b5e4-48ec-ba38-fe0e37133e4b" />
<img width="1038" height="355" alt="Screenshot_2025-11-13_15-00-02" src="https://github.com/user-attachments/assets/51961531-abe0-4265-b3a3-7648fbc99704" />

## Notes
- Uses HOG-based face detection
- Threshold for matching: 0.6
- Works on both Linux and Windows
- Avoid noisy datasets for best recognition
- Press q to exit video mode

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

