class Cliente:
    def __init__(self, nombre, cedula):
        self._nombre = nombre
        self._cedula = cedula
        self._factura_cliente = []


@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self,nombre):
    self._nombre = nombre

@property
def cedula(self):
    return self._cedula

@cedula.setter
def cedula(self,cedula):
    self._cedula = cedula


@property
def factura_cliente(self):
    return self._factura_cliente

@factura_cliente.setter
def factura_cliente(self,factura_cliente):
    self._factura_cliente.append(factura_cliente)
