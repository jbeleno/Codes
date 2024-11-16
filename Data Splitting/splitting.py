import os
import shutil
from sklearn.model_selection import train_test_split

# Directorio base donde están las carpetas de clases
base_dir = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\data sets finales\sin separar\clases perspectiva'

# Directorios de salida
train_dir = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\data sets finales\separados final\final perspectiva\train'
val_dir = r'C:\Users\jesus\OneDrive\Desktop\cosas importantes\data sets finales\separados final\final perspectiva\valid'

# Crear las carpetas de train y val si no existen
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Iterar sobre las carpetas de las clases
for class_folder in os.listdir(base_dir):
    class_path = os.path.join(base_dir, class_folder)
    
    # Asegurarse de que solo se procesan carpetas
    if os.path.isdir(class_path):
        # Crear subcarpetas en train y val para cada clase
        os.makedirs(os.path.join(train_dir, class_folder), exist_ok=True)
        os.makedirs(os.path.join(val_dir, class_folder), exist_ok=True)
        
        # Obtener todos los archivos de la clase
        files = os.listdir(class_path)
        files = [f for f in files if os.path.isfile(os.path.join(class_path, f))]
        
        # Hacer el split
        train_files, val_files = train_test_split(files, test_size=0.2, random_state=42)
        
        # Copiar archivos de entrenamiento
        for file in train_files:
            src = os.path.join(class_path, file)
            dst = os.path.join(train_dir, class_folder, file)
            shutil.copy2(src, dst)
        
        # Copiar archivos de validación
        for file in val_files:
            src = os.path.join(class_path, file)
            dst = os.path.join(val_dir, class_folder, file)
            shutil.copy2(src, dst)

print("Separación de datos completada.")