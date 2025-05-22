# Name: Image Rotation
# Description: This script rotates images in a given folder in three directions: 90° clockwise, 90° counter-clockwise, and 180° upside down, generating new rotated images.
# Nombre: Rotación de imágenes
# Explicación: Este script rota imágenes en una carpeta dada en tres direcciones: 90° en sentido horario, 90° en sentido antihorario y 180° al revés, generando nuevas imágenes rotadas.

import os
from PIL import Image

# Input folder where the images are located
# Carpeta de entrada donde están las imágenes
input_folder = 'PATH/TO/YOUR/INPUT/FOLDER'  # <-- Change this to your input images folder path
# Output folder where the rotated images will be saved
# Carpeta de salida donde se guardarán las imágenes rotadas
output_folder = 'PATH/TO/YOUR/OUTPUT/FOLDER'  # <-- Change this to your output folder path

# Create the output folder if it does not exist
# Crea la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Iterate over the files in the input folder
# Itera sobre los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filter only images / Filtra solo imágenes
        # Load the image / Carga la imagen
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Rotate the images in the specified directions / Rota las imágenes en las direcciones especificadas
        rotated_clockwise = img.rotate(-90, expand=True)  # Clockwise / Sentido horario
        rotated_counterclockwise = img.rotate(90, expand=True)  # Counter-Clockwise / Sentido antihorario
        rotated_upsidedown = img.rotate(180, expand=True)  # Upside Down / Al revés

        # Save the rotated images in the output folder / Guarda las imágenes rotadas en la carpeta de salida
        rotated_clockwise.save(os.path.join(output_folder, f'rotated_clockwise_{filename}'))
        rotated_counterclockwise.save(os.path.join(output_folder, f'rotated_counterclockwise_{filename}'))
        rotated_upsidedown.save(os.path.join(output_folder, f'rotated_upsidedown_{filename}'))

print("Rotation completed.")  # Rotaciones completadas.
