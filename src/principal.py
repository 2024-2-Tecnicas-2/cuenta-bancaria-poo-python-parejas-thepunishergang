from cuenta_bancaria import CuentaBancaria

if __name__ == '__main__':
    # TODO: Adiciona aquí el código que deseas para la Cuenta Bancaria.
    titular = ""
    numeroCuenta = ""
    saldo = 0
    valor_ingreso = 0
    valor_retiro = 0
    opcion = 0
    print("Ingrese el nombre del titular:")
    titular = input()
    print("Ingrese el numero de cuenta a asignar: ")
    numeroCuenta = input()
    print("Ingrese el saldo actual")
    saldo = float(input())

    mi_cuenta = CuentaBancaria(titular, numeroCuenta, saldo)

    while(opcion!= 5):
        print("Ingrese el numero de la opcion que desea acceder: ")
        print("1.Ingresar dinero\n2.Retirar dinero\n3.Consultar saldo con intereses\n4.Cambiar Interes\n5.salir")
        opcion = int(input())
        if(opcion == 1):
            print("digite el valor a ingresar")
            valor_ingreso = float(input())

            print(f"El nuevo saldo es: ${mi_cuenta.ingresar(valor_ingreso)}")

        elif(opcion == 2):
            print("digite el valor a retirar")
            valor_retiro = float(input())
            print(f"El nuevo saldo es: ${mi_cuenta.retirar(valor_retiro)}")

        elif(opcion ==3):
            print(f"Su saldo con intereses es: ${mi_cuenta.calcular_interes()}")

        elif(opcion == 4):
            print("ingrese el nuevo valor del interes")
            interes = float(input())
            mi_cuenta.set_tipo_interes(interes)

        elif(opcion == 5):
            exit()
        else:
            print("Opcion no valida...")

                

        
