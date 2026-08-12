import psycopg2

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

    consulta = "SELECT artista, titulo_pista, formato FROM catalogo_musical WHERE formato = 'FLAC';"
    cursor.execute(consulta)


    resultados = cursor.fetchall()
    print("\n--- Canciones en Alta FIdelidad (FLAC) ---   ")
    for fila in resultados:
        print(f"Artista: {fila[0]}, Título: {fila[1]}, Formato: {fila[2]}")

except Exception as error:
    print("Error al conectar a la base de datos:", error)

finally:
    if 'conexion' in locals() and conexion is not None:
        cursor.close()
        conexion.close()
        print("Conexión cerrada.")