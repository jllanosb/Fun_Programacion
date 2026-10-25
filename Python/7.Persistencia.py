print("Persistencia de Datos")
# Capacidad de convervar informacion despues de terminar una ejecucion
# Crear archivo .txt, escribir un mensaje
with open("Python\datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola estudiantes\n")

print("Archivo creado correctamente.")

# Abrir el archivo leer el contenido
with open("Python\datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read();

print(f'Contenido: {contenido}')

print("Puntero de un Archivo")
# Crear archivo -- Apunta a un indice
with open("Python\estudiantes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Susana\nDiana\nMaria\n")

with open("python\estudiantes.txt", "r", encoding="utf-8") as archivo:
    posicion_inicial = archivo.tell()
    primera_linea= archivo.readline()
    posicion_final = archivo.tell()

print(f'Posicion Inicial: {posicion_inicial}')
print(f'Primera Linea: {primera_linea}')
print(f'Posicion Final: {posicion_final}')

print("Operaciones con Punteros")