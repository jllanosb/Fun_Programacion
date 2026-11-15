# Funcion Saludar
# def indica funcion
# saludar nombre funcion
# nombre es el parametro de la funcion
# return lo que devuelve la funcion

def saludar(nombre):
    print(f'Hola, Buen dia {nombre}')

# Llamar a la funcion
# nombre(argumentos)
saludar('Jaime')

def sumar(a,b):
    return a+b

resultado = sumar(7,8)
print(resultado)

print("FUNCION RECURSIVA")
"""
def funcion_recursiva(parametro):
    if condicion_de_parada:
        return valor_conocido
    else:
        return operacion(parametro,
                        funcion_recursvia(parametro_Reducido))
"""

def cuenta_regresiva(n):
    # caso base
    if n==0:
       print("¡Fin!")
       return
    
    print(n)
    #Caso recursivo (llamando asi mismo)
    cuenta_regresiva(n-1)

cuenta_regresiva(7)

# Errores comunes en Recursividad
# sin caso base
"""
def f(n):
    return f(n-1)  ## Recursividad infinita

f()
3
2
1
-1
-2
...
-infinito

# Caso base inalcanzable
def f1 (n):
    if n==0:
    n=5
    f1(n-2)
5
3
1
-1
-3
-5

def f2(n):
    return n + f(n) # 1
    1+ 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1++1 --infinito

Desbordamiento
    f(100000)
"""

print("Funciones Recursivas Simples")
# Factorial
"""
Factorial 5! = 5 x 4 x 3 x 2 x 1 = 120
n! = 1 --> n=0 ------> Caso base
n! = n* (n-1)! --> n > 0 ---> Caso recursivo
"""
def factorial(n):
    if n<0:
        raise ValueError("Numero no válido")
    #caso base
    if n==0:
        return 1
    else:
        # Caso recursivo
        return n*factorial(n-1)

print(f'El factorial de 5 es: {factorial(5)}')
print(f'El factorial de 0 es: {factorial(0)}')

# Potencia
"""
base^exp=1  --> exp=0
base^exp= base x base^(exp-1)   --> exp > 0
"""
def potencia(base, exp):
    if exp <0:
        raise ValueError("Exponente no Válido")
    #caso base
    if exp==0:
        return 1
    else:
        #caso recursivo
        return base * potencia(base, exp-1)

print(f'La Potencia de 2^10 es: {potencia(2,10)}')
print(f'La Potencia de 2^10 es: {potencia(5,0)}')

# Sumatoria
"""
suma(n)=0 --> n=0
suma(n) = n+suma(n-1) --> n>0
"""
def suma_hasta(n): #  suma 1 a n
    if n <0:
        raise ValueError("Numero no Válido")
    if n==0:
        return 0
    else:
        return n + suma_hasta(n-1)

print(f'La sumatoria de los 10 primeros numeros es: {suma_hasta(10)}')

# suma de elementos de una lista
"""
suma_lista([a, ...restoelementos]) = a+ suma_lista(resto)
suma_lista([])  = 0
"""
def suma_lista(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(f'La suma de los elementos de la lista es: {suma_lista([10,20,30,40,50])}')

# suma digitos de un numero
"""
suma_digito(0) = 0
suma_digito(n) = (n % 10) + suma_digito(n // 10)
"""

def suma_digitos(n):
    if n==0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

print(f'La suma de los digitos del numero 123456789 ees:{suma_digitos(12345678)}')
    
# Conteo
# conteo hacia arriba
def contar_arriba(n, actual=1):
    # caseo base
    if actual>n:
        return
    print(actual)
    # Caso recursivo
    contar_arriba(n, actual +1)

print("\n Conteo")
contar_arriba(7)

# conteo de digitos de un numero
"""
contar_digitos(0) = 0
contar_digitos(n) = 1+contar_digitos (n // 10)
"""

def contar_digitos(n):
    #caso base
    if n==0:
        return 0
    else:
        # caso recursivo
        return 1 + contar_digitos(n // 10)

print(f'La cantidad de digitos del numero 987654321 es: {contar_digitos(987654321)}')

# cuantas veces aparece un elemento en una lista
def contar_ocurrencias(lista, objetivo):
    #caso base
    if len(lista)==0:
        return 0
    if lista[0] == objetivo: # coincide
        return 1+ contar_ocurrencias(lista[1:], objetivo)
    else:
        return contar_ocurrencias(lista[1:], objetivo)

print(f'Numero de veces que se repite el numero 1: {contar_ocurrencias([1,2,1,1,1,2,3,4,5,6,7,8,9], 1)}')