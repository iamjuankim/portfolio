import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint

# Define paths for dataset and processed images
dataset_path = 'C:\\QualityDataset\\data'

# Set up data generators for training and testing with custom augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,                    # Normalize image values to [0, 1]
    horizontal_flip=True,              # Random horizontal flip
    vertical_flip=True,                # Random vertical flip
    brightness_range=[0.3, 1.0]       # Random brightness adjustment between 0.3 and 1.0
)

test_datagen = ImageDataGenerator(rescale=1./255)  # Only rescaling for testing data

# Update your dataset to reflect your folder structure
train_dir = os.path.join(dataset_path, 'train')  # Folder containing training data
test_dir = os.path.join(dataset_path, 'test')    # Folder containing testing data

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),  # Resize images to 128x128 (or any size you prefer)
    batch_size=32,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),  # Resize images to 128x128
    batch_size=32,
    class_mode='categorical'
)

# Build a CNN model
model = models.Sequential([
    # Input Layer
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D((2, 2)),

    # Second Conv Block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third Conv Block
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Fully Connected Layer
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    
    # Output Layer with softmax activation for multi-class classification
    layers.Dense(len(os.listdir(train_dir)), activation='softmax')  # Output layer based on the number of quality folders
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Set up a model checkpoint to save the best model during training
checkpoint = ModelCheckpoint('img_sort.h5', save_best_only=True)

# Train the model
model.fit(
    train_generator,
    epochs=10,
    validation_data=test_generator,
    callbacks=[checkpoint]
)

# Save the model (if not saved during training)
model.save('img_sort.h5')

print("Model training complete and saved as 'img_sort.h5'.")
