import csv
#API formato JSON --Pares--> Clave:Valor --> "Nombre":"Jaime"
import json
import sqlite3

# Persistencia de Datos con Archivos
print('Datos Organizados con estructura definida')
estudiantes = [
    ["E001","Jaime","17"],
    ["E002","Diana","16"],
    ["E003","Susana","14"]
]
archivo_csv = open("Python\\estudiantes_csv.txt", "w", encoding="utf-8")
for estudiante in estudiantes:
    linea = ",".join(estudiante)
    archivo_csv.write(linea + "\n")
archivo_csv.close()

archivo_tsv = open("Python\\estudiantes_tsv.txt", "w", encoding="utf-8")
for estudiante in estudiantes:
    linea = "\t".join(estudiante)
    archivo_tsv.write(linea + "\n")
archivo_tsv.close()

archivo_pipe = open("Python\\estudiantes_pipe.txt", "w", encoding="utf-8")
for estudiante in estudiantes:
    linea = "|".join(estudiante)
    archivo_pipe.write(linea + "\n")
archivo_pipe.close()

print("Archivos CSV, TSV y  PIPE creados correctamente")

# Archivos CSV en Python
with open("python\\estudiantes.csv","w",newline ="", encoding="utf-8") as archivo:
    escritor=csv.writer(archivo)
    escritor.writerow(["Codigo","Nombre","Nota"])
    escritor.writerow(["E001","Jaime","17"])
    escritor.writerow(["E002","Diana","16"])
    escritor.writerow(["E003","Susana","14"])

print("Archivo estudiantes.csv creado correctamente!!")

#Leer el archivo csv
with open("python\\estudiantes.csv","r",newline="",encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    print(f'Encabezado: {encabezado}')
    for fila in lector:
        codigo = fila[0]
        nombre = fila[1]
        nota = fila[2]
        print(f'Codigo: {codigo} - Nombre: {nombre} - Nota: {nota}')

#Crear lista productos en formato JSON
productos =[
    {
        "Codigo":"P001",
        "Nombre":"Laptop",
        "Categoria":"Tecnologia",
        "Precio": 2500.00,
        "Stock": 20
    },
    {
        "Codigo":"P002",
        "Nombre":"Mouse",
        "Categoria":"Accesorios",
        "Precio": 75.0,
        "Stock": 40
    },
    {
        "Codigo":"P003",
        "Nombre":"Router",
        "Categoria":"Comunicaciones",
        "Precio": 200.00,
        "Stock": 10
    }
]

with open("python\\productos.json","w", encoding="utf-8") as archivo:
    #guardar los productos en el archivo
    json.dump(productos, archivo, indent=4,ensure_ascii=False)
    print("Archivo productos.json creado correctamente")

#Leer contenido archivo json
with open("python\\productos.json", "r", encoding="utf-8") as archivo:
    productos = json.load(archivo)
    print("Lista de Productos")
    print("**********************")
    for producto in productos:
        print(f'Codigo: {producto["Codigo"]}')
        print(f'Nombre: {producto["Nombre"]}')
        print(f'Categoria: {producto["Categoria"]}')
        print(f'Precio: {producto["Precio"]}')
        print(f'Stock: {producto["Stock"]}')
        valor_inventario = producto["Precio"] *producto["Stock"]
        print(f'Valor del Inventario: s/. {valor_inventario}')
        print("--------------------------")

# Limitacions csv, TSV, pipe, etc. Capacidad almacenamiento
# --> Migrar en Base de Datos
# Usar SQLite --> sqlite3
conexion = sqlite3.connect("python\\estudiante.db")
cursor=conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS estudiante")

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiante(
    id integer primary key autoincrement,
    nombre text not null,
    edad integer not null
)
""")

cursor.execute("DELETE FROM estudiante")
cursor.execute("INSERT INTO estudiante (nombre, edad) values (?,?)", ("Susana",23,))
cursor.execute("INSERT INTO estudiante (nombre, edad) values (?,?)", ("Maria",35,))
cursor.execute("INSERT INTO estudiante (nombre, edad) values (?,?)", ("Jaime",40,))
cursor.execute("INSERT INTO estudiante (nombre, edad) values (?,?)", ("Diana",37,))

conexion.commit()

#consultar
cursor.execute("SELECT id, nombre, edad FROM estudiante")
registros = cursor.fetchall()

for fila in registros:
    print(f'ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]} años')

conexion.close()


