#!/bin/bash

python3 -m venv myvenv

source myvenv/bin/activate

pip3 install -r requirements.txt

cd src
known_faces_dir="../assets/known_faces"
if [ ! -d "$known_faces_dir" ]; then
  echo "Creating directory for known faces at assets/known_faces..."
  mkdir -p "$known_faces_dir"
else
  echo "Directory for known faces already exists at assets/known_faces."
fi

mp4_found=false
for mp4_file in ../assets/videos/*.mp4; do
  if [ -f "$mp4_file" ]; then
    mp4_found=true
    break
  fi
done

if [ "$mp4_found" = false ]; then
  echo "No MP4 file found in assets folder. Running mp4_downloader.py to download one..."
  python3 mp4_downloader.py
else
  echo "MP4 file(s) found in assets folder. Skipping download."
fi

image_found=false
for image_file in ../assets/images/*.{png,jpg,jpeg}; do
  if [ -f "$image_file" ]; then
    image_found=true
    break
  fi
done

if [ "$image_found" = false ]; then
  echo "No valid image (PNG, JPG, JPEG) found in assets folder. Please add an image."
  exit 1
else
  echo "Valid image found in assets folder. Proceeding."
fi

echo "Running create_dataset.py to ensure dataset is created..."
python3 create_dataset.py
clear
echo "Running persona_cipher.py..."
python3 persona_cipher.py
