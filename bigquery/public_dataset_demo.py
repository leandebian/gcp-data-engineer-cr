# 1. Importamos la librería oficial de Google Cloud para interactuar con BigQuery
from google.cloud import bigquery

def query_public_dataset():

    # 2. Inicializamos el cliente de BigQuery. 
    # Busca automáticamente tus credenciales activas (gcloud login) en tu máquina.
    client = bigquery.Client()

    # 3. Definimos la consulta SQL como una cadena de texto (String) multilínea.
    # Usamos triple comilla (""") para poder escribir en varias líneas cómodamente.
    query="""
SELECT order_items.id, order_id, product_id, products.name
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
JOIN `bigquery-public-data.thelook_ecommerce.products` AS products
ON order_items.product_id = products.id
"""

    # 4. Enviamos la consulta a BigQuery mediante 'client.query(query)'.
    # .to_dataframe + cant de lineas 
    # Google Cloud termine de procesar la consulta y devuelva las filas de datos.
    results = client.query(query).to_dataframe()[:20]

    # 5. Imprimimos el resultados fila por fila.
    print(results)

# 7. Esta condición asegura que el código solo se ejecute si ejecutas este archivo directamente
# (por ejemplo, con 'python public_dataset_demo.py'), evitado que corra si lo importaras desde otro script.
if __name__=="__main__":
    query_public_dataset() 
