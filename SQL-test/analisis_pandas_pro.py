import pandas as pd
from sqlalchemy import create_engine

cadena_conexion = "postgresql://daft:cochecho@192.168.18.174:5432/analytics_db"

try:
    print("Generando conexion a homelab")

    motor = create_engine(cadena_conexion)

    consulta = "SELECT artista, album, titulo_pista, genero, formato, duracion_segundos FROM catalogo_musical;"

    with motor.connect() as conexion_activa:
        df_musica = pd.read_sql_query(consulta, conexion_activa)

    print("\n--- Análisis Estadístico ---")
    promedio_por_genero = df_musica.groupby('genero')['duracion_segundos'].mean().round(2)
    print("duracion de la musica por genero(en segundos)")
    print(promedio_por_genero)
except Exception as error:
    print(f"Error en la consulta {error}")