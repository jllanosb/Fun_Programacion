print("Operaciones Abrir, Leer, Escribir y Cerrar Archivos")
# Utilizar import os

import os

nombre_archivo= "Python\\escribir.txt"
# obtener la ruta
ruta_completa = os.path.abspath(nombre_archivo)
print(f'Nombre Archivo: {nombre_archivo}')
print(f'Ruta Completa: {ruta_completa}')

# Escribir
archivo =  open(nombre_archivo, "w", encoding="utf-8")
archivo.write("Archivo abierto en modo escritura. \n")
archivo.close() # Cierre manual

print("Archivo creado y escrito correctamente.")

#Escribir varias lineas
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("Maria \n")
    archivo.write("Esperanza \n")
    archivo.write("Sofia \n")

print("Datos escritos correctamente")

#Escribir sin elliminar
with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("Maria Fernanda \n")
    archivo.write("Perla \n")

# Leer contenido
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)

#Leer linea por linea
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    linea1= archivo.readline()
    linea2= archivo.readline()
    linea3= archivo.readline()
    linea4= archivo.readline()
    linea5= archivo.readline()

print(f'Linea 1: {linea1}')
print(f'Linea 2: {linea2}')
print(f'Linea 3: {linea3}')
print(f'Linea 4: {linea4}')
print(f'Linea 5: {linea5}')

# Leer como coleccion
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.readlines()

for i in range(len(contenido)):
    print(f'Linea {i+1}: {contenido[i].strip()}')