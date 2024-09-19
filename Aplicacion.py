
def depositar(saldo):
    valor = int(input("Cuanto desea depositar?: "))
    saldo += valor
    print(f'Su saldo actualizado es de: {saldo}')

def retirar(saldo):
    valor = int(input("Cuanta plata desea retirar?: "))
    
    if valor > saldo:
        print("Saldo Insuficiente")
        print("Ingrese un saldo disponible en su cuenta")

    else:
        saldo -=valor
        print(f"Uste retiro: {valor}")
        print(f"El nuevo saldo es: {saldo}")

def aplicacion():
    nombre = "Peter Parker"
    cuenta = "ahorros"
    saldo = 1500
    print('-----------Datos del Cliente-----------')
    print(f'Nombre: {nombre}')
    print(f'Tipo de cuenta: {cuenta}')
    print(f'Saldo actual: {saldo}\n')
    print("-----------BIENVENIDOS AL SISTEMA---------")

    print("Ingrese una opcion")
    print("1.Consultar Saldo")
    print("2.Retirar")
    print("3.Depositar")
    print('9.Salir')

    opcion = int(input('Ingrese la opcion: '))
    while (opcion != 9):
        match (opcion):
            case 1:
                print(f'Su saldo actual es: {saldo}')
                break
            case 2:
                retirar(saldo)
                break
            case 3:
                depositar(saldo)
                break
            case 9:
                print('Saliendo del sistema. Gracias por visitar nuestros servicios')
                break
            
    
aplicacion()