# Name: Image Perspective Transformation
# Description: This script applies two types of perspective transformations to images in a given folder, generating new images with different perspectives.
# Nombre: Transformación de perspectiva de imágenes
# Explicación: Este script aplica dos tipos de transformaciones de perspectiva a imágenes en una carpeta dada, generando nuevas imágenes con diferentes perspectivas.

import os
import cv2  # Import OpenCV / Importa OpenCV
from PIL import Image
import numpy as np

# Input folder where the images are located
# Carpeta de entrada donde están las imágenes
input_folder = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\aumentamiento de datos\test\Monilia-fase-3'
# Output folder where the transformed images will be saved
# Carpeta de salida donde se guardarán las imágenes transformadas
output_folder = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\aumentamiento de datos\clases perspectiva\Monilia-fase-3'

# Create the output folder if it does not exist
# Crea la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

def apply_perspective(image, version):
    width, height = image.size
    src_points = np.array([[0, 0], [width, 0], [0, height], [width, height]], dtype='float32')
    
    if version == 1:
        # First version of the perspective transformation (less pronounced) / Primera versión de la transformación de perspectiva (menos pronunciada)
        dst_points = np.array([[width * 0.1, height * 0.1], [width * 0.9, height * 0.2], [width * 0.1, height * 0.9], [width * 0.9, height * 0.9]], dtype='float32')
    elif version == 2:
        # Second version of the perspective transformation (more pronounced) / Segunda versión de la transformación de perspectiva (más pronunciada)
        dst_points = np.array([[width * 0.2, height * 0.2], [width * 0.8, height * 0.1], [width * 0.2, height * 0.8], [width * 0.8, height * 0.9]], dtype='float32')

    # Calculate the transformation matrix / Calcular la matriz de transformación
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply the perspective transformation / Aplicar la transformación de perspectiva
    transformed_image = cv2.warpPerspective(np.array(image), matrix, (width, height))

    return Image.fromarray(transformed_image)

# Iterate over the files in the input folder
# Itera sobre los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filter only images / Filtra solo imágenes
        # Load the image / Carga la imagen
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Apply the first version of the perspective transformation / Aplica la primera versión de la transformación de perspectiva
        transformed_image_v1 = apply_perspective(img, version=1)
        # Save the first transformed image in the output folder / Guarda la primera imagen transformada en la carpeta de salida
        transformed_image_v1.save(os.path.join(output_folder, f'perspective_v1_{filename}'))

        # Apply the second version of the perspective transformation / Aplica la segunda versión de la transformación de perspectiva
        transformed_image_v2 = apply_perspective(img, version=2)
        # Save the second transformed image in the output folder / Guarda la segunda imagen transformada en la carpeta de salida
        transformed_image_v2.save(os.path.join(output_folder, f'perspective_v2_{filename}'))

print("Perspective transformations completed.")  # Transformaciones de perspectiva completadas.
