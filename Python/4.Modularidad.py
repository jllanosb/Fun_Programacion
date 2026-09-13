# modulos --> funcion especifica

## Calcular Productos

def leer_producto():
    return input("Ingrese un producto: ")

def leer_precio():
    return float(input("Ingrese un Precio: "))

def calcular_igv(precio):
    return precio*0.18

def resultados(nombre, precio, igv):
    total=precio + igv
    print(f'Producto: {nombre}')
    print(f'Precio: {precio}')
    print(f'IGV: {igv}')
    print(f'Total a pagar: {total}')

nombre = leer_producto()
precio = leer_precio()
igv = calcular_igv(precio)
resultados(nombre,precio,igv)