import tensorflow as tf
import numpy as np
import cv2  # Para cargar y preprocesar imágenes
import matplotlib.pyplot as plt
import os

# Ruta del modelo guardado
model_path = r'/content/drive/MyDrive/final perspectiva/modelos /efficientdet_final_model_512x512_30_64.h5'

# Cargar el modelo
model = tf.keras.models.load_model(model_path)

# Obtener los nombres de las clases
class_names = sorted(os.listdir(r'/content/drive/MyDrive/final perspectiva/train'))
print(f"Clases: {class_names}")

# Función para cargar y preprocesar una imagen
def preprocess_image(image_path, img_size=(512, 512)):
    # Cargar la imagen
    img = cv2.imread(image_path)
    # Redimensionar la imagen al tamaño esperado
    img = cv2.resize(img, img_size)
    # Convertir la imagen a array y expandir la dimensión para que tenga el formato adecuado para el modelo
    img = np.expand_dims(img, axis=0)
    # Normalizar la imagen usando el preprocess_input de ResNet50
    img = tf.keras.applications.resnet50.preprocess_input(img)
    return img

# Ruta de la imagen de prueba
test_image_path = r'/content/drive/MyDrive/final perspectiva/Moniliafase2(2).jpg'

# Preprocesar la imagen de prueba
image = preprocess_image(test_image_path)

# Hacer una predicción
predictions = model.predict(image)

# Obtener la clase predicha (la de mayor probabilidad)
predicted_class = np.argmax(predictions, axis=1)[0]

# Mostrar la predicción principal
print(f"Predicción principal: {class_names[predicted_class]} ({100 * np.max(predictions):.2f}% probabilidad)")

# Mostrar las probabilidades para todas las clases
print("\nProbabilidades para cada clase:")
for i, prob in enumerate(predictions[0]):
    print(f"{class_names[i]}: {prob * 100:.2f}%")

# Mostrar la imagen de prueba
plt.imshow(cv2.cvtColor(cv2.imread(test_image_path), cv2.COLOR_BGR2RGB))
plt.title(f"Predicción: {class_names[predicted_class]} ({100 * np.max(predictions):.2f}%)")
plt.axis('off')
plt.show()