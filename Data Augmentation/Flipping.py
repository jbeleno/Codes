# Name: Image Flipping
# Description: This script performs vertical and horizontal flipping of images in a given folder, generating new flipped images.
# Nombre: Flipping de imágenes
# Explicación: Este script realiza el volteo (flipping) vertical y horizontal de imágenes en una carpeta dada, generando nuevas imágenes volteadas.

import os
from PIL import Image

# Input folder where the images are located
# Carpeta de entrada donde están las imágenes
input_folder = 'PATH/TO/YOUR/INPUT/FOLDER'  # <-- Change this to your input images folder path
# Output folder where the flipped images will be saved
# Carpeta de salida donde se guardarán las imágenes volteadas
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

        # Apply vertical and horizontal flipping / Aplica flipping vertical y horizontal
        flipped_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
        flipped_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Save the vertically flipped image in the output folder / Guarda la imagen volteada verticalmente en la carpeta de salida
        flipped_vertical.save(os.path.join(output_folder, f'vertical_{filename}'))
        # Save the horizontally flipped image in the output folder / Guarda la imagen volteada horizontalmente en la carpeta de salida
        flipped_horizontal.save(os.path.join(output_folder, f'horizontal_{filename}'))

print("Flipping completed.")  # Flipping completado.
