import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    # Configuración del pipeline
    options = PipelineOptions(
        runner="DataflowRunner",  # Cambiar a DataflowRunner para GCP / DirecRunner para Local
        project="gcp-data-engineer-curso-499611",
        region="us-central1",
        temp_location="gs://gcp-curso-dtfrun/temp"
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Leer archivo" >> beam.io.ReadFromText("gs://dataflow-samples/shakespeare/kinglear.txt")
            | "Separar palabras" >> beam.FlatMap(lambda line: line.split())
            | "Contar palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText("gs://gcp-curso-dtfrun/output/wordcount")
        )
    print("Pipeline ejecutado exitosamente!")
    
if __name__ == "__main__":
    run()