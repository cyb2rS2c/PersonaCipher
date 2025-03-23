# Face Recognition Application

This is a Python-based face recognition project using the `face_recognition` and `OpenCV` libraries. The application allows users to recognize faces in images and videos using a preloaded dataset of known faces.

## Features
- Load known faces from a dataset.
- Recognize faces in a given image.
- Recognize faces in a given video.
- User-friendly command-line interface.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip3 install face_recognition opencv-python numpy
```

## Usage
clone the repository:

For Windows (download the zip file):
    
    cd Face-Recognition-Application
For Linux:
    
    git clone https://github.com/cyb2rS2c/Face-Recognition-Application.git
    cd Face-Recognition-Application
    
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

### 2. Run the Application
Execute the script using:

```bash
python3 face_recognition_app.py
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

## Notes
- The face recognition model uses the HOG-based feature extraction method.
- You can adjust the face matching threshold (`0.6` in the script) to fine-tune accuracy.
- Press `q` to exit video processing.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## Disclaimer

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

