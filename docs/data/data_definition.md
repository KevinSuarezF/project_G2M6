# Definición de los datos

## Origen de los datos

* Fuente de los datos: Los datos provienen de un dataset disponible en Kaggle, titulado "vehicles-colombia-fasecolda". Esta base de datos fue creada y compartida por el usuario de Kaggle panchicore.

* Forma en que se obtuvieron: Los datos fueron recopilados y estructurados por la organización Fasecolda, que es la Federación de Aseguradores Colombianos. Fasecolda recopila información detallada sobre vehículos en Colombia, incluyendo características técnicas, precios, y otros datos relevantes para el mercado de seguros.

## Especificación de los scripts para la carga de datos

La carga de datos se realiza desde __init__.py (src/nombre_paquete/__init__.py) y configura el entorno para descargar, descomprimir y listar el dataset desde Kaggle de manera automatizada. Inicialmente, se establece la variable de entorno KAGGLE_CONFIG_DIR para apuntar al directorio donde se encuentra el archivo de configuración kaggle.json, ajustando sus permisos a 0o600 para garantizar la seguridad. Luego, se define el directorio de destino download_path y se ejecuta el comando de Kaggle para descargar el dataset vehicles-colombia-fasecolda a dicho directorio. La ruta del archivo ZIP descargado se establece y el archivo se descomprime en el directorio de destino utilizando la librería zipfile. Posteriormente, el archivo ZIP se elimina para ahorrar espacio en el sistema. Finalmente, se listan y muestran los archivos extraídos para verificar el contenido, automatizando así todo el proceso. 

### Rutas de origen de datos

Ubicación de los archivos de origen de los datos: Los archivos de origen están disponibles en Kaggle. Se pueden descargar desde la página del dataset: https://www.kaggle.com/datasets/panchicore/vehicles-colombia-fasecolda/data

Estructura de los archivos de origen de los datos: Los datos están en formato CSV. Las columnas típicas incluyen Marca, Modelo, Precio por año, entre otras.

### Base de datos de destino

Los datos se van a manejar por el momento en el repositorio, donde despues de realizar la recoleccion de datos, se realiza el preprocesamiento y de ser necesario se almacenaria en src/nombre_paquete/database, o en la memoria de la maquina virtual/local, por lo que el proceso de entrenamiento y validación se realizan directamente allí.
