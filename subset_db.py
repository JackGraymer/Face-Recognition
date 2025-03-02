import shutil
import os

# copy the first picture from the path subfolders to the folder 'celebrities'. Rename each image as its folder name.jpg

# Define paths
source_path = "Celebrity Faces Dataset"
destination_path = "celebrities"

# Create destination folder if it doesn't exist
os.makedirs(destination_path, exist_ok=True)

# Iterate through each subfolder in the dataset
for folder in os.listdir(source_path):
    folder_path = os.path.join(source_path, folder)

    if os.path.isdir(folder_path):  # Ensure it's a folder
        images = [f for f in os.listdir(
            folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if images:  # Check if there are any images
            first_image = images[0]  # Take the first image
            source_image_path = os.path.join(folder_path, first_image)
            destination_image_path = os.path.join(
                destination_path, f"{folder}.jpg")

            # Copy and rename the image
            shutil.copy(source_image_path, destination_image_path)
            print(f"Copied: {source_image_path} -> {destination_image_path}")

print("Process completed.")
