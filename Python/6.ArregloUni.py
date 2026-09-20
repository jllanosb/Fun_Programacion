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

## Operaciones Insercion, Busqueda, Modificacion y Eliminacion

#--- Insercion ----
# Final de un arreglo append()
productos=['Teclado', 'Mouse','Monitor', 'Laptop']
productos.append("Celular Tactil")
print(productos)

# Insertar posicion especifica insert
productos.insert(1, "Iphone")
print(productos)

# Insertar varios elementos extend()
productos.extend(['HP', 'TV','Asus', 'Refrigeradora','TV'])
print(productos)

#--- Busqueda ----
if 'TV' in productos:
    posicion = productos.index('TV')
    print(f'Encontrado en la posicion: {posicion}')
else:
    print(f'El elemento TV no se encontrado')

print(productos.index('TV'))
print(productos.count('TV'))

#--- Modificar elemento ----
productos[7]='Licuadora'
print(productos)

for k in range(len(productos)):
    if productos[k] == 'Refrigeradora':
        productos[k]= 'Auriculares'
print(productos)

# Reemplaza por cero a notas menor 11
print(Notas)
for i in range(len(Notas)):
    if Notas[i]<11:
        Notas[i]=0
print(Notas)

# Suma + 1 a cada nota ...modificacion masiva
for i in range(len(Notas)):
    Notas[i]=Notas[i]+1
print(Notas)

# Modificacion por segmentos colocar en mayusculas con upper
productos[1:3]=[producto.upper() for producto in productos[1:3]]
print(productos)

# modificacion por listas
precios=[35,80,74,99]
precios=[precio*0.9 if precio > 70 else precio for precio in precios]
print(precios)

# ----- Eliminacion -----
# Eliminar valor
productos.remove('Licuadora')
print(productos)

# Eliminar por indice metodo pop()
eliminado = productos.pop(2)
print(eliminado)
print(productos)

# eliminar por segmento (Rango definido)
del productos[1:3]
print(productos)

# Eliminacion masiva
Notas = [x for x in Notas if x > 12]
print(Notas)

# Vaciar lista
Notas.clear()
print(Notas)