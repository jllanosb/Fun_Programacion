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
