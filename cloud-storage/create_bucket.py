# Importamos la librería para manejar argumentos por línea de comandos (la terminal)
import argparse
# Importamos el módulo de almacenamiento de la SDK oficial de Google Cloud
from google.cloud import storage

def main():
    # 1. CONFIGURACIÓN DE ARGUMENTOS EN LA TERMINAL
    # Creamos el analizador de argumentos con una descripción de lo que hace el script
    parser = argparse.ArgumentParser(description="Create a GCP bucket.")
    
    # Definimos que el script requiere obligatoriamente un parámetro de texto llamado 'bucket_name'
    parser.add_argument("bucket_name", type=str, help="Name of the bucket to create")
    
    # Procesamos los argumentos que el usuario escribió al ejecutar el script
    args = parser.parse_args()

    # Guardamos en una variable el nombre del bucket que ingresó el usuario
    bucket_name = args.bucket_name
    print(f"Bucket name received: {bucket_name}")
    
    # 2. CONEXIÓN Y LÓGICA DE GOOGLE CLOUD
    # Inicializamos el cliente de almacenamiento (usa las credenciales de tu entorno)
    storage_client = storage.Client()
    
    # Creamos un objeto de tipo bucket local con el nombre deseado
    bucket = storage_client.bucket(bucket_name)
    
    # Definimos la clase de almacenamiento (ej: STANDARD, NEARLINE, COLDLINE, ARCHIVE)
    bucket.storage_class = "STANDARD"
    
    # Enviamos la petición a Google Cloud para crear el bucket físicamente,
    # indicando la región geográfica donde se alojarán los datos (ej: US-CENTRAL1)
    new_bucket = storage_client.create_bucket(bucket, location="us-central1")
    
    # Confirmamos en la terminal que el bucket se creó con éxito mostrando sus propiedades reales
    print(f"Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}")

# Esto asegura que el código solo se ejecute si corres este archivo directamente,
# y no si lo importas como un módulo en otro script.
if __name__ == "__main__":
    main()
    
#Para crear bucket desde el script
#1) estar conectado a la cuenta desde la terminal al google cloud
#2) correr el scrip desde la carpeta raiz del proyecto 
# comando create_buckey.py [name_del_bucket]
# create_bucket.py gcp-bucket-regional-script1