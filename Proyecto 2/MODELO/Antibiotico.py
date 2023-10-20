class Antibiotico:
    def __init__(self, nombre_del_producto, dosis, precio):
        self._nombre_del_producto = nombre_del_producto
        self._dosis = dosis
        self._tipo_de_animal = ["Bobinos", "Caprinos", "Porcinos"]
        self._precio = precio


@property
def nombre_del_producto(self):
    return self._nombre_del_producto

@nombre_del_producto.setter
def nombre_del_producto(self,nombre_del_producto):
    self._nombre_del_producto = nombre_del_producto

@property
def dosis(self):
    return self._dosis

@dosis.setter
def dosis(self,dosis):
    self._dosis = dosis

@property
def precio(self):
    return self._precio

@precio.setter
def precio(self,precio):
    self._precio = precio