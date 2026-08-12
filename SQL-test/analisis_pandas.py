import psycopg2
import pandas as pd

host = "192.168.18.174"
puerto = "5432"
base_datos = "analytics_db"
usuario = "daft"
password = "cochecho"

try:
    print("Conectando al homelab")
    conexion = psycopg2.connect(
        host=host,
        port=puerto,
        database=base_datos,
        user=usuario,
        password=password
    )

    cursor = conexion.cursor()

    consulta = "SELECT artista, album, titulo_pista, genero, formato, duracion_segundos FROM catalogo_musical;"

    columnas = ['Artista', 'Album', 'Titulo', 'Genero', 'Formato', 'Duracion Seg']
    df_musica = pd.read_sql_query(consulta, conexion)

    print("\n--- Análisis Estadístico ---")

    promedioG = df_musica.groupby('genero')['duracion_segundos'].mean().round(2)
    print("Duracion promedio por genero (en segundos):")
    print(promedioG)

except Exception as error:
    print(f"Erro ene la consulta: {error}")
finally:
    if 'conexion' in locals() and conexion is not None:
        conexion.close()
        print("\n Conexion cerrada.")