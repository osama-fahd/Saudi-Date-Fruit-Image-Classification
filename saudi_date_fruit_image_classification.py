import pathlib

import zipfile

local_zip = '/content/Date_Fruit_Image_Dataset_Splitted_Train.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall()

zip_ref.close()

base_dir = 'train'
base_dir = pathlib.Path(base_dir)

import zipfile

local_zip = '/content/Date_Fruit_Image_Dataset_Splitted_Test.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall()

zip_ref.close()

test_dir = 'test'
test_dir = pathlib.Path(test_dir)

image_count = len(list(test_dir.glob('*/*.jpg')))
print(image_count)

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = train_datagen.flow_from_directory(
    base_dir,
    target_size=(160, 160),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

validation_data = train_datagen.flow_from_directory(
    base_dir,
    target_size=(160, 160),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

test_datagen = ImageDataGenerator(rescale=1./255)

test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=(160, 160),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(160, 160, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.2),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(9, activation='softmax')  # 9 classes
])

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

epochs = 15
history = model.fit(
    train_data,
    epochs=epochs,
    validation_data=validation_data,
    verbose=1
)

test_loss, test_accuracy = model.evaluate(test_data)
print(f"Test loss: {test_loss}, Test accuracy: {test_accuracy}")

y_true = test_data.classes
y_pred = np.argmax(model.predict(test_data), axis=-1)

print("Classification Report:\n", classification_report(y_true, y_pred, target_names=test_data.class_indices.keys()))

confusion_mtx = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_mtx, annot=True, fmt='d', xticklabels=test_data.class_indices.keys(), yticklabels=test_data.class_indices.keys(), cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

import os
from PIL import Image
import matplotlib.pyplot as plt

train_dir = 'train'
test_dir = 'test'

class_dirs = os.listdir(train_dir)

fig, axes = plt.subplots(3, 3, figsize=(12, 12))
axes = axes.flatten()

for i, class_dir in enumerate(class_dirs):
    class_path = os.path.join(train_dir, class_dir)

    image_files = os.listdir(class_path)

    image_path = os.path.join(class_path, image_files[5])

    image = Image.open(image_path)
    axes[i].imshow(image)
    axes[i].set_title(class_dir)
    axes[i].axis('off')

plt.tight_layout()
plt.show()