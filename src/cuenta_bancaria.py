class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.tipo_interes = 0.015  

    def set_tipo_interes(self, tipo_interes):
        if 0 <= tipo_interes <= 10:
            self.tipo_interes = tipo_interes / 100
        else:
            raise ValueError("El interés debe estar entre 0 y 10")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        return self.saldo

    def calcular_interes(self):
        return self.saldo + (self.tipo_interes * self.saldo)





