"""
Script to load a trained image classification model, preprocess a test image, make a prediction, and display the results.

Dependencies: TensorFlow, NumPy, OpenCV, Matplotlib, os
"""

import tensorflow as tf
import numpy as np
import cv2  # For loading and preprocessing images / Para cargar y preprocesar imágenes
import matplotlib.pyplot as plt
import os

# Path to the saved model
model_path = 'PATH/TO/YOUR/MODEL.h5'  # <-- Change this to your saved model path

# Load the model / Cargar el modelo
model = tf.keras.models.load_model(model_path)

# Get the class names
class_names = sorted(os.listdir('PATH/TO/YOUR/TRAIN/FOLDER'))  # <-- Change this to your train folder path
print(f"Classes: {class_names}")  # Clases: {class_names}

# Function to load and preprocess an image / Función para cargar y preprocesar una imagen
def preprocess_image(image_path, img_size=(512, 512)):
    """
    Loads and preprocesses an image for ResNet50 model prediction.
    Args:
        image_path (str): Path to the image file.
        img_size (tuple): Target size for resizing (width, height).
    Returns:
        np.ndarray: Preprocessed image ready for model prediction.
    """
    # Load the image / Cargar la imagen
    img = cv2.imread(image_path)
    # Resize the image to the expected size / Redimensionar la imagen al tamaño esperado
    img = cv2.resize(img, img_size)
    # Convert the image to array and expand dimensions for the model / Convertir la imagen a array y expandir la dimensión para el modelo
    img = np.expand_dims(img, axis=0)
    # Normalize the image using ResNet50's preprocess_input / Normalizar la imagen usando preprocess_input de ResNet50
    img = tf.keras.applications.resnet50.preprocess_input(img)
    return img

# Path to the test image
test_image_path = 'PATH/TO/YOUR/TEST/IMAGE.jpg'  # <-- Change this to your test image path

# Preprocess the test image / Preprocesar la imagen de prueba
image = preprocess_image(test_image_path)

# Make a prediction / Hacer una predicción
predictions = model.predict(image)

# Get the predicted class (the one with the highest probability) / Obtener la clase predicha (la de mayor probabilidad)
predicted_class = np.argmax(predictions, axis=1)[0]

# Show the main prediction / Mostrar la predicción principal
print(f"Main prediction: {class_names[predicted_class]} ({100 * np.max(predictions):.2f}% probability)")  # Predicción principal

# Show the probabilities for all classes / Mostrar las probabilidades para todas las clases
print("\nProbabilities for each class:")  # Probabilidades para cada clase
for i, prob in enumerate(predictions[0]):
    print(f"{class_names[i]}: {prob * 100:.2f}%")

# Show the test image / Mostrar la imagen de prueba
plt.imshow(cv2.cvtColor(cv2.imread(test_image_path), cv2.COLOR_BGR2RGB))
plt.title(f"Prediction: {class_names[predicted_class]} ({100 * np.max(predictions):.2f}%)")
plt.axis('off')
plt.show()