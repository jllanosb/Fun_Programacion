# Declarando Arreglo

Valores = [0,0,0,0]
print(Valores)

# Insertando valor en una posicion
Valores[1]=25

# Mostrando el Arreglo
print(Valores)

# Tipo dato arreglo
print(type(Valores))

# longitud de un arreglo
print(f'Longitud es: {len(Valores)}')

# EL ultimo elemento
print(f'{Valores[len(Valores) - 1 ]}')

## Arreglo Nombres
Nombres = ['Juan','Maria','Jose','Pedro','Luis']
print(Nombres)
print(f'Cantidad de Nombres guardados: {len(Nombres)}')
print(f'Ultimo nombre guardado: {Nombres[len(Nombres) - 1]}')

Edades = [23,14,18,25,17]
print(f'Elemento en la posicion 1: {Edades[1]}')
print(f'Elemento en la indice 4: {Edades[4]}')

## RECORRER UN ARRAY - ARREGLO- LISTA - VECTOR
Notas=[14,16,18,10,12,11]

for i in range(len(Notas)):
    # print("Posicion",i,"Valor: ", Notas[i])
    print(f'Posicion {i} Valor: {Notas[i]}')

print(Nombres)
for k in range(len(Nombres)):
    print(f'Elemento {k+1} Valor: {Nombres[k]}')