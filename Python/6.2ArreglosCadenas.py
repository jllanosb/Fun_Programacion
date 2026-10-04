print("Arreglo de Cadenas")
mensaje = "Fundamentos de Programacion"
print(mensaje)
print(mensaje[3])
print(mensaje[10])
print(mensaje[11])

# Inmutabilidad
notas=[14,20,8,15]
notas[2] = 12
print(notas)

palabra = "UPN."
# palabra[3] = "♠"
print(palabra)

texto = palabra[0] + palabra[1] + palabra[2] + "♠"
print(texto)

print("Concatenacion")
nombre = "Jaime"
apellido = "Llanos"
completo = nombre + " " + apellido
print(completo)

# Longitud de la cadena
cantidad = len(mensaje)
print(f'El texto {mensaje} tiene una longitud de {cantidad} letras')
# Ultimo caracter
print(f'El ultimo caracter del texto {mensaje} es {mensaje[len(mensaje) - 1]}')

print("Recorriendo una Cadena")
for i in range(len(mensaje)):
    print(f'{i} -> {mensaje[i]}')

# EJERCICIO
"""
Leer un codigo de estudiante y su carrera
Formar una etiqueta
Mostrar la longitud codigo, carrera, etiqueta
Mostrar primer y ultimo caracter del codigo
Recorrer cada letra de la carrera
Crear una etiqueta nueva agregando el semestre sin alterar la original
"""
codigo=input("Ingrese su codigo: ")
carrera=input("ingrese su carrera: ")

etiqueta = codigo + "|" + carrera
etiqueta_periodo = etiqueta + "|2026-2"

print(etiqueta)
print(f'Longitud del Codigo: {len(codigo)}')
print(f'Longitud de la Carrera: {len(carrera)}')
print(f'Longitud de la Etiqueta: {len(etiqueta)}')

if len(codigo) > 0:
    print(f'Primer Caracter {codigo[0]}')
    print(f'Ultimo caracter {codigo[len(codigo) - 1]}')

print("Recorriendo la carrera")
for i in range(len(carrera)):
    print(f'{i} -> {carrera[i]}')

print(etiqueta_periodo)
