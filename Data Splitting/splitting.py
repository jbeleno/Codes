# Name: Data Splitting Script
# Description: This script splits image datasets into training and validation folders using scikit-learn's train_test_split.
# Nombre: Script de Separación de Datos
# Explicación: Este script separa conjuntos de imágenes en carpetas de entrenamiento y validación usando train_test_split de scikit-learn.

import os
import shutil
from sklearn.model_selection import train_test_split

# Base directory where the class folders are located
# Directorio base donde están las carpetas de clases
base_dir = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\data sets finales\sin separar\clases perspectiva'

# Output directories for train and validation sets
# Directorios de salida para los conjuntos de entrenamiento y validación
train_dir = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\data sets finales\separados final\final perspectiva\train'
val_dir = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\data sets finales\separados final\final perspectiva\valid'

# Create the train and val folders if they do not exist
# Crear las carpetas de train y val si no existen
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Iterate over the class folders
# Iterar sobre las carpetas de las clases
for class_folder in os.listdir(base_dir):
    class_path = os.path.join(base_dir, class_folder)
    
    # Make sure only folders are processed / Asegurarse de que solo se procesan carpetas
    if os.path.isdir(class_path):
        # Create subfolders in train and val for each class / Crear subcarpetas en train y val para cada clase
        os.makedirs(os.path.join(train_dir, class_folder), exist_ok=True)
        os.makedirs(os.path.join(val_dir, class_folder), exist_ok=True)
        
        # Get all files in the class folder / Obtener todos los archivos de la clase
        files = os.listdir(class_path)
        files = [f for f in files if os.path.isfile(os.path.join(class_path, f))]
        
        # Split the files / Hacer el split
        train_files, val_files = train_test_split(files, test_size=0.2, random_state=42)
        
        # Copy training files / Copiar archivos de entrenamiento
        for file in train_files:
            src = os.path.join(class_path, file)
            dst = os.path.join(train_dir, class_folder, file)
            shutil.copy2(src, dst)
        
        # Copy validation files / Copiar archivos de validación
        for file in val_files:
            src = os.path.join(class_path, file)
            dst = os.path.join(val_dir, class_folder, file)
            shutil.copy2(src, dst)

print("Data splitting completed.")  # Separación de datos completada.