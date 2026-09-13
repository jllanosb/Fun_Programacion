# REstringir Acceso a campos o valores
class CtaAhorro:
    def __init__(self, Titular, SaldoInicial):
        self.Titular = Titular # Publico
        self.__saldo= SaldoInicial  # Restringido

    def depositar(self, monto):
        if (monto > 0 ):
            self.__saldo += monto # Nuevo saldo restringido

    def mostrar_saldo(self):
        print(f'Titulo: {self.Titular}')
        print(f'Saldo: {self.__saldo:.2f}') # ReEstringido

cuenta = CtaAhorro("Jaime",1500) #Declarar funcion class ctahorro
cuenta.depositar(500)
cuenta.mostrar_saldo()