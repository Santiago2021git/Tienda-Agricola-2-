from MODELO import ProductoControl


class Fertilizante(ProductoControl.Producto_Control):
    def __init__(self, registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto,
                 fecha_de_ultima_aplicacion):
        self._fecha_de_ultima_aplicacion = fecha_de_ultima_aplicacion
        super().__init__(registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto)


@property
def fecha_de_ultima_aplicacion(self):
    return self._fecha_de_ultima_aplicacion


@fecha_de_ultima_aplicacion.setter
def fecha_de_ultima_aplicacion(self, fecha_de_ultima_aplicacion):
    self._fecha_de_ultima_aplicacion = fecha_de_ultima_aplicacion

