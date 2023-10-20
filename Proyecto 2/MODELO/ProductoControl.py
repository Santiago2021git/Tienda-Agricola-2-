class Producto_Control:
    def __init__(self, registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto):
        self._registro_ica = registro_ica
        self._nombre_del_producto = nombre_del_producto
        self._frecuencia_de_aplicacion = frecuencia_de_aplicacion
        self._valor_del_producto = valor_del_producto


@property
def registro_ica(self):
    return self._registro_ica


@registro_ica.setter
def registro_ica(self, registro_ica):
    self._registro_ica = registro_ica


@property
def nombre_del_producto(self):
    return self._nombre_del_producto


@nombre_del_producto.setter
def nombre_del_producto(self, nombre_del_producto):
    self._nombre_del_producto = nombre_del_producto


@property
def frecuencia_de_aplicacion(self):
    return self._frecuencia_de_aplicacion


@frecuencia_de_aplicacion.setter
def frecuencia_de_aplicacion(self, frecuencia_de_aplicacion):
    self._frecuencia_de_aplicacion = frecuencia_de_aplicacion


@property
def valor_del_producto(self):
    return self._valor_del_producto


@valor_del_producto.setter
def valor_del_producto(self, valor_del_producto):
    self._valor_del_producto = valor_del_producto

