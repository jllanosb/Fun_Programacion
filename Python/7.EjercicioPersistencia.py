import pyodbc
import pandas as pd

# pip install pyodbc pandas
servidor = 'localhost'
base_datos = 'Hospital_Caj'
usuario = 'estudiante'
clave = 'Prueba27'

conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server});'
    f'SERVER={servidor};'
    f'DATABASE={base_datos};'
    f'UID={usuario};'
    f'PWD={clave};'
    'TrustServerCertificate=yes;'
)
print("Conexion Exitosa")

cursor = conexion.cursor()
cursor = conexion.cursor("DROP TABLE IF EXISTS Python")

sql = """
CREATE TABLE Python(
    id_alumno int identity(1,1) primary key,
    Nombre varchar(100) not null,
    Apellido varchar(100),
    Edad int,
    Ciudad Varchar(100)
)
"""

cursor.execute(sql)
conexion.commit()

#iNSERT
datos = [
    ('Jaime', 'Ll.', 25, 'Cajamarca'),
    ('Susana', 'Mejia', 37, 'Cuzco'),
    ('Diana', 'Reyes', 42,'Trujillo')
]

cursor.executemany("""
INSERT INTO Python (Nombre, Apellido, Edad, Ciudad)
VALUES (?,?,?,?)
""", datos)

conexion.commit()

# LEER DATOS
df=pd.read_sql("SELECT * FROM Python", conexion)

print(f'\nRegistros de la Tabla Python')
print(df)

cursor.close()
conexion.close()