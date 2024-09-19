# Definimos unos cuantos clientes
clientes= [
    {'Nombre': 'Hector',
    'Apellidos':'Costa Guzman',
    'dni':'11111111A'},
    {'Nombre': 'Juan',
    'Apellidos':'González Márquez',
    'dni':'22222222B'}
]
# Creamos una función que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            return '{} {}'.format(c['Nombre'],c['Apellidos'])
            
    return 'Cliente no encontrado'

def borrar_cliente(clientes, dni):
   
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            return str(c),"> BORRADO"
            
    return 'Cliente no encontrado'

def crear_cliente():
    Nombre = input('Ingrese el nombre del cliente: ')
    Apellidos = input('Ingrese los apellidos del cliente: ')
    dni= input('Ingrese el dni: ')

    clientes.append(dict(Nombre = Nombre, Apellidos=Apellidos, dni = dni))
    return f'Cliente Agregado'

def peticion():
    print('-------SISTEMA DE CLIENTES--------------')
    print('ELIGE UNA OPCION:')
    print("""
        1.CONSULTAR LISTA DE CLIENTES
        2.AGREGAR CLIENTES
        3.BORRAR CLIENTE
        4.CONSULTAR POR DNI
        5.SALIR
          """)
    opcion = '0'
    while opcion != '5':
        opcion = input('Ingrese su opcion (1-5): ')
        match opcion:
            case '1':
                print(clientes)
            case '2':
                print('---DATOS DEL CLIENTE----')
                crear_cliente()
                print('CLIENTE AGREGADO!!!')
            case '3':
                dni = input('ingrese el dn1 a eliminar: ')
                borrar_cliente(clientes,dni)
               
            case '4':
                dni = input('ingrese el dn1 a buscar: ')
                print(f'EL CLIENTE CON EL DNI {dni} es:')
                print(mostrar_cliente(clientes,dni))
            case '5':
                return 'SALISTE DEL SISTEMA!!'
                
    return

print(peticion())
