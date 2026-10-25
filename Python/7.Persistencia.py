print("Persistencia de Datos")
# Capacidad de convervar informacion despues de terminar una ejecucion
# Crear archivo .txt, escribir un mensaje
with open("Python\\datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola estudiantes\n")

print("Archivo creado correctamente.")

# Abrir el archivo leer el contenido
with open("Python\\datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read();

print(f'Contenido: {contenido}')

print("Puntero de un Archivo")
# Crear archivo -- Apunta a un indice
with open("Python\\estudiantes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Susana\nDiana\nMaria\n")

with open("python\\estudiantes.txt", "r", encoding="utf-8") as archivo:
    posicion_inicial = archivo.tell()
    primera_linea= archivo.readline()
    posicion_final = archivo.tell()

print(f'Posicion Inicial: {posicion_inicial}')
print(f'Primera Linea: {primera_linea}')
print(f'Posicion Final: {posicion_final}')

print("Operaciones con Punteros")

with open("Python\\codigo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("UPN2026")

with open("Python\\codigo.txt", "r", encoding="utf-8") as archivo:
    # puntero se mueve a la posicion 2
    archivo.seek(2)
    posicion_actual = archivo.tell()
    contenido = archivo.read()

print(f'Posicion actual: {posicion_actual}')
print(f'Contenido leido: {contenido}')

print("Archivo de Texto con datos legibles")

with open("Python\\estudiante.txt", "w", encoding="utf-8") as archivo1:
    archivo1.write("Estudiante: Susana\n")
    archivo1.write("Nota: 17\n")
    archivo1.write("Estado: Aprobado\n")

with open("Python\\estudiante.txt", "r", encoding="utf-8") as archivo1:
    contenido1 = archivo1.read()

print(contenido1)

print("Archivos Binarios")
# Almacenar Bytes
with open("Python\\numero.bin", "wb") as archivo:
    archivo.write(bytes([64,65,66,67,68,69,70]))

with open("Python\\numero.bin", "rb") as archivo:
    datos = archivo.read()

print(f'Datos Binarios: {datos}')