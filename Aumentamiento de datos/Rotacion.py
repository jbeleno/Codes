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

        # Rota las imágenes en las direcciones especificadas
        rotated_clockwise = img.rotate(-90, expand=True)  # Clockwise
        rotated_counterclockwise = img.rotate(90, expand=True)  # Counter-Clockwise
        rotated_upsidedown = img.rotate(180, expand=True)  # Upside Down

        # Guarda las imágenes en la carpeta de salida
        rotated_clockwise.save(os.path.join(output_folder, f'rotated_clockwise_{filename}'))
        rotated_counterclockwise.save(os.path.join(output_folder, f'rotated_counterclockwise_{filename}'))
        rotated_upsidedown.save(os.path.join(output_folder, f'rotated_upsidedown_{filename}'))

print("Rotaciones completadas.")
