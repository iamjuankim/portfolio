import os
import shutil
import random

# Define the dataset path
dataset_path = 'C:\\QualityDataset\\data'

# Create train and test folders inside data
train_path = os.path.join(dataset_path, 'train')
test_path = os.path.join(dataset_path, 'test')

# Ensure the train and test directories exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# List of quality folders (assuming these are subfolders in data)
quality_folders = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p']

# Function to split and move images to train and test directories
def split_and_move_images():
    for folder in quality_folders:
        # Path to the current quality folder
        folder_path = os.path.join(dataset_path, folder)
        
        # Create subfolders for train and test within the current quality folder
        train_subfolder = os.path.join(train_path, folder)
        test_subfolder = os.path.join(test_path, folder)
        
        # Create subfolders if they don't exist
        os.makedirs(train_subfolder, exist_ok=True)
        os.makedirs(test_subfolder, exist_ok=True)
        
        # Get the list of image files in the current folder
        image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
        
        # Shuffle the image files to ensure random distribution
        random.shuffle(image_files)
        
        # Split images into 80% for training and 20% for testing
        split_index = int(0.8 * len(image_files))
        train_images = image_files[:split_index]
        test_images = image_files[split_index:]
        
        # Move the images to the corresponding train and test subfolders
        for image in train_images:
            shutil.move(os.path.join(folder_path, image), os.path.join(train_subfolder, image))
        
        for image in test_images:
            shutil.move(os.path.join(folder_path, image), os.path.join(test_subfolder, image))
        
        print(f"Images from {folder} have been split into train and test sets.")

# Call the function to split and move images
split_and_move_images()

print("Image splitting complete.")