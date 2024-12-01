import os
from PIL import Image

# Define the path to your dataset (updated for your laptop)
dataset_path = 'C:\\QualityDataset'

# Define the path for saving cropped and scaled images
output_path = os.path.join(dataset_path, 'data')

# List of quality folders
quality_folders = ['1440p', '1080p', '720p', '480p', '360p', '240p', '144p']

# Coordinates for cropping (you can change these coordinates as needed)
crop_coords = [
    (320, 320, 352, 352), (414, 358, 446, 390), (508, 396, 540, 428), (602, 434, 634, 466),
    (696, 472, 728, 504), (790, 510, 822, 542), (884, 548, 916, 580), (978, 586, 1010, 618),
    (1072, 624, 1104, 656), (1166, 662, 1198, 694), (1260, 700, 1292, 732), (1354, 738, 1386, 770),
    (1448, 776, 1480, 808), (1542, 814, 1574, 846), (1636, 852, 1668, 884), (1730, 890, 1762, 922),
    (1824, 928, 1856, 960), (1918, 966, 1950, 998), (2012, 1004, 2044, 1036), (2106, 1042, 2138, 1074)
]

# Function to scale up the image
def scale_up(image, factor=10):
    width, height = image.size
    new_size = (width * factor, height * factor)
    return image.resize(new_size, Image.Resampling.NEAREST)

# Function to process each image in the dataset
def process_images():
    for folder in quality_folders:
        folder_path = os.path.join(dataset_path, folder)
        output_folder = os.path.join(output_path, folder)  # Save in corresponding subfolder in "data"
        
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Iterate over each image in the folder (assuming all are .png)
        for i in range(50):
            image_name = f"{i+1}.png"
            image_path = os.path.join(folder_path, image_name)
            img = Image.open(image_path)

            # Generate 10 cropped images with scaling
            for idx, (left, top, right, bottom) in enumerate(crop_coords):
                cropped_img = img.crop((left, top, right, bottom))
                scaled_img = scale_up(cropped_img, factor=10)  # Scale up 10x

                # Save the scaled image as PNG
                save_name = f"{folder}_{i+1}_{idx+1}.png"  # Image name format
                save_path = os.path.join(output_folder, save_name)
                scaled_img.save(save_path)
                print(f"Saved {save_name} in {output_folder}")

# Call the function to process images
process_images()
