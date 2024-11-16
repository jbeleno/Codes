import os
import cv2  # Importa OpenCV
from PIL import Image
import numpy as np

# Define la carpeta donde están las imágenes
input_folder = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\aumentamiento de datos\test\Monilia-fase-3'
output_folder = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\aumentamiento de datos\clases perspectiva\Monilia-fase-3'

# Crea la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

def apply_perspective(image, version):
    width, height = image.size
    src_points = np.array([[0, 0], [width, 0], [0, height], [width, height]], dtype='float32')
    
    if version == 1:
        # Primera versión de la transformación de perspectiva (menos pronunciada)
        dst_points = np.array([[width * 0.1, height * 0.1], [width * 0.9, height * 0.2], [width * 0.1, height * 0.9], [width * 0.9, height * 0.9]], dtype='float32')
    elif version == 2:
        # Segunda versión de la transformación de perspectiva (más pronunciada)
        dst_points = np.array([[width * 0.2, height * 0.2], [width * 0.8, height * 0.1], [width * 0.2, height * 0.8], [width * 0.8, height * 0.9]], dtype='float32')

    # Calcular la matriz de transformación
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Aplicar la transformación de perspectiva
    transformed_image = cv2.warpPerspective(np.array(image), matrix, (width, height))

    return Image.fromarray(transformed_image)

# Itera sobre los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filtra solo imágenes
        # Carga la imagen
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Aplica la primera versión de la transformación de perspectiva
        transformed_image_v1 = apply_perspective(img, version=1)
        transformed_image_v1.save(os.path.join(output_folder, f'perspective_v1_{filename}'))

        # Aplica la segunda versión de la transformación de perspectiva
        transformed_image_v2 = apply_perspective(img, version=2)
        transformed_image_v2.save(os.path.join(output_folder, f'perspective_v2_{filename}'))

print("Transformaciones de perspectiva completadas.")
