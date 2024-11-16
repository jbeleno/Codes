import os
from PIL import Image

# Define la carpeta donde están las imágenes
input_folder = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\aumentamiento de datos\clases nuevas imagenes\Monilia-fase-2'
output_folder = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\aumentamiento de datos\clases nuevas imagenes\Monilia-fase-2'

# Crea la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Itera sobre los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filtra solo imágenes
        # Carga la imagen
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Aplica flipping vertical y horizontal
        flipped_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
        flipped_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Guarda las imágenes en la carpeta de salida
        flipped_vertical.save(os.path.join(output_folder, f'vertical_{filename}'))
        flipped_horizontal.save(os.path.join(output_folder, f'horizontal_{filename}'))

print("Flipping completado.")
