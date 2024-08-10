class CuentaBancaria:
    def __init__(self, numero_cuenta, propietario, balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    # Punto 8
    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print("Depósito exitoso. El nuevo balance es: ", self.balance)
        else:
            print("El monto a depositar debe ser positivo.")

    # Punto 9
    def retirar(self, monto):
        if monto > 0:
            if monto <= self.balance:
                self.balance -= monto
                print("Retiro exitoso. El nuevo balance es:", self.balance)
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser positivo.")
    
    # Punto 10
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print("Se ha aplicado una cuota de manejo del 2%. El nuevo balance es:", self.balance)

    # Punto 11
    def mostrar_detalles(self):
        print("Número de Cuenta: ", self.numero_cuenta)
        print("Propietario: ", self.propietario)
        print("Balance: ", self.balance)


cuenta1 = CuentaBancaria("24445556667", "Juanito Alimaña", 1000)
cuenta1.depositar(500)
cuenta1.retirar(2000) #Caso para probar Fondos Insuficientes
cuenta1.retirar(300)
cuenta1.aplicar_cuota_manejo()
cuenta1.mostrar_detalles()
