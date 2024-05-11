import os
import zipfile

os.environ['KAGGLE_CONFIG_DIR'] = 'src/nombre_paquete/database'
os.chmod('src/nombre_paquete/database/kaggle.json', 0o600)

# Descargar el conjunto de datos de Kaggle
download_path = 'src/nombre_paquete/database'
os.system(f'kaggle datasets download -d panchicore/vehicles-colombia-fasecolda -p "{download_path}"')

# Ruta del archivo ZIP
zip_file_path = os.path.join(download_path, 'vehicles-colombia-fasecolda.zip')

# Directorio de destino para la extracción
extract_dir = 'src/nombre_paquete/database'

# Descomprimir el archivo ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Eliminar el archivo ZIP después de la extracción
os.remove(zip_file_path)

# Listar los archivos extraídos
extracted_files = os.listdir(extract_dir)
print("Archivos extraídos:", extracted_files)

# Renombrar el archivo extraído
for file_name in extracted_files:
    if file_name.endswith('.csv'):
        old_path = os.path.join(extract_dir, file_name)
        new_path = os.path.join(extract_dir, 'vehicles_colombia.csv')
        os.rename(old_path, new_path)
        print(f"Archivo renombrado de '{file_name}' a 'vehicles_colombia.csv'")
        break