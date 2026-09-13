# Declarar una funcion
## -------------------------------
# def saludar(a,b,c): --> a,b,c son parametros
def saludar():
    print("Bienvenido al curso de Fundamentos de Programación")

# Invocar o Llamar a una funcion
saludar()
# saludar(1,2,3) --> 1,2,3 son argumentos

## Declarar funcion sin retorno
## -------------------------------
def menu():
    print("1. Registrar")
    print("2. Buscar")
    print("3. Salir")

menu()

## Declarar funcion con retorno
## -------------------------------
def producto(a,b):
    return a * b

# Llamar a funcion con retorno pasando argumentos
resultado = producto(8,7)
print(f'{resultado}, Resultado*2 = {resultado*2}')

## Funcion con varios argumentos
## -------------------------------
def promedio(T1, T2, T3, EP, EF):
    return T1*0.10 + T2*0.10 + T3*0.10 + EP*0.20 + EF*0.50

resultado1 = promedio(20,20,20,14,12)
print(f'Tu Promedio Final es {resultado1}')

## Declarar Funcion con parametros determinados
## -------------------------------

def saludar_estudiante(nombre, curso='Fundamentos de Programación'):
    print(f'Hola {nombre}, Bienvenido a {curso}')

saludar_estudiante('Jaime')
saludar_estudiante('Jaime','Base de Datos')

## Funciones Anidadas
## -------------------------------

def proceso_compra(monto):
    def aplicar_igv(valor):
        return valor*0.18

    igv= aplicar_igv(monto)
    total = monto + igv
    return total

resultado2 = proceso_compra(550)
print(f'Total a pagar con IGV es: s/{resultado2}')