import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Function to fetch image URLs from Google Images
def fetch_image_urls(query, num_images=10):
    query = urllib.parse.quote(query)  # Encode the query for URLs
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"

    # Send a GET request to Google Images
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all image elements
    img_tags = soup.find_all("img")
    img_urls = []

    for img in img_tags:
        img_url = img.get("src")
        if img_url and img_url.startswith("http"):
            img_urls.append(img_url)

        if len(img_urls) >= num_images:
            break

    return img_urls

# Function to download images from URLs
def download_image(url, folder, image_name):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        os.makedirs(folder, exist_ok=True)
        with open(f"{folder}/{image_name}", "wb") as file:
            file.write(response.content)
        print(f"Downloaded {image_name}")
    except Exception as e:
        print(f"Failed to download {image_name}: {e}")

# Function to fetch and save images for a given person
def download_images_for_person(person_name):
    print(f"Searching images for {person_name}...")
    img_urls = fetch_image_urls(person_name)

    folder_name = f"dataset2/{person_name.replace(' ', '_')}"
    image_count = 0

    # Download the first 10 images
    for url in img_urls:
        if image_count >= 10:
            break
        download_image(url, folder_name, f"img{image_count + 1}.jpg")
        image_count += 1

# Function to create the dataset for multiple people
def create_dataset():
    try:
        with open('usernames.txt', 'r') as file:
            username_list = [line.strip() for line in file.readlines() if line.strip()]  # Read and clean the usernames
    except FileNotFoundError:
        print("Error: 'usernames.txt' not found!")
        return

    # Fetch and save images for each username
    for name in username_list:
        download_images_for_person(name)

    print("Dataset creation complete.")

if __name__ == "__main__":
    create_dataset()
