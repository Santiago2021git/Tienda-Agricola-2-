from MODELO import ProductoControl


class Plaga(ProductoControl.Producto_Control):
    def __init__(self, registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto,
                 periodo_de_carencia):
        self._periodo_de_carencia = periodo_de_carencia
        super().__init__(registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto)


@property
def periodo_de_carencia(self):
    return self._periodo_de_carencia


@periodo_de_carencia.setter
def periodo_de_carencia(self, periodo_de_carencia):
    self._periodo_de_carencia = periodo_de_carencia

