## Variables locales
def saludar():
    nombre="Jaime"
    print(f"Hola {nombre} Bienvenido")

saludar()
# print(nombre)

## Variables globales
edad=25

def mostraredad():
    global edad
    print(f"Tu edad es: {edad}")

mostraredad()
print(type(edad))

## Variable no local

def principal():
    subtotal = 0

    def calcularmonto():
        nonlocal subtotal
        subtotal += 100
        print(f"El nuevo valor es: {subtotal}")

    calcularmonto()
    print(f"El nuevo valor en Principal: {subtotal}")

principal()