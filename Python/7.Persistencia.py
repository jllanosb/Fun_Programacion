print("Persistencia de Datos")

# Crear archivo .txt, escribir un mensaje
with open("Python\datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola estudiantes\n")

print("Archivo creado correctamente.")

# Abrir el archivo leer el contenido
with open("Python\datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read();

print(f'Contenido: {contenido}')