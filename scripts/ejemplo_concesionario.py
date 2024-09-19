class Empleado:
    def __init__(self,nombre,cedula,telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono

    def set_nombre(self,nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    
    def set_cedula(self,cedula):
        self._cedula = cedula
    def get_cedula(self):
        return self._cedula
    
    def set_nombre(self,telefono):
        self._telefono = telefono
    def get_telefono(self):
        return self._telefono
    
class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono,nPlaza,salario,contrato):
        super().__init__(nombre, cedula, telefono)
        self._nPlaza = nPlaza
        self._salario = salario
        self._contrato=contrato
    
    def set_nPlaza(self,nPlaza):
        self._nPlaza = nPlaza
    def get_nPlaza(self):
        return self._nPlaza
   
    def set_salario(self,salario):
        self._salario = salario
    def get_salario(self):
        return self._salario
   
    def set_contrato(self,contrato):
        self._contrato = contrato
    def get_contrato(self):
        return self._contrato
    
    def calcularSalario(self):
        return self._salario + (self._salario * 0.02)
        
class EmpleadoIndefinido(Empleado):
    def __init__(self, nombre, cedula, telefono,nPlaza,salario,categoria):
        super().__init__(nombre, cedula, telefono)
        self._nPlaza = nPlaza
        self._salario = salario
        self._categoria = categoria

    def set_nPlaza(self, nPlaza):
        self._nPlaza = nPlaza
    def get_nPlaza(self):
        return self._nPlaza
    
    def set_salario(self, salario):
        self._salario = salario
    def get_salario(self):
        return self._salario
    
    def set_categoria(self, categoria):
        self._categoria = categoria
    def get_categoria(self):
        return self._categoria
    
    def calcularSalario(self):
       
        if (self._categoria == 1):
            return self._salario + (self._salario * 0.03)
        elif (self._categoria == 2):
            return self._salario + (self._salario * 0.05)
        elif (self._categoria == 3):
            return self._salario + (self._salario * 0.08)
        else:
            return self._salario

class Subcontrato(Empleado):
    def __init__(self, nombre, cedula, telefono,empresa):
        super().__init__(nombre, cedula, telefono)  
        self._responsable = empresa

    def set_responsable(self,empresa):
        self._responsable = empresa
    def get_responsable(self):
        return self._responsable
    
subcontrato1 = Subcontrato('Eli','10652313','321654854','Cocacola')
subcontrato2 = Subcontrato('Maria','11522313','347852154','Alpina')

print('Empleados subcontratados')
print('*************Empleado 1**********')
print(f'Nombre: {subcontrato1.get_nombre()}\nCédula: {subcontrato1.get_cedula()}\nTelefono: {subcontrato1.get_telefono()}\nEmpresa responsable: {subcontrato1.get_responsable()}')
print('*************Empleado 2**********')
print(f'Nombre: {subcontrato2.get_nombre()}\nCédula: {subcontrato2.get_cedula()}\nTelefono: {subcontrato2.get_telefono()}\nEmpresa responsable: {subcontrato2.get_responsable()}')

contrato = Empleado('Carlos','10854621',31652455)
print('--------Contratados----')
print(f'Nombre: {contrato.get_nombre()}\nCedula: {contrato.get_cedula()}\nTelefono: {contrato.get_telefono()}')


