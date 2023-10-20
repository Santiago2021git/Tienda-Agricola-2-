from MODELO.ProductoControl import Producto_Control

def prueba_producto_control():
    
    """
    Pruebas para la clase Producto_Control.

    Crear un objeto Producto_Control y acceder a sus atributos.

    >>> producto = Producto_Control("123ABC", "Producto A", "Mensual", 100.0)
    >>> producto._registro_ica
    '123ABC'
    >>> producto._nombre_del_producto
    'Producto A'
    >>> producto._frecuencia_de_aplicacion
    'Mensual'
    >>> producto._valor_del_producto
    100.0

    Modificar los valores de los atributos.

    >>> producto._registro_ica = "456XYZ"
    >>> producto._registro_ica
    '456XYZ'
    >>> producto._nombre_del_producto = "Producto B"
    >>> producto._nombre_del_producto
    'Producto B'
    >>> producto._frecuencia_de_aplicacion = "Semanal"
    >>> producto._frecuencia_de_aplicacion
    'Semanal'
    >>> producto._valor_del_producto = 200.0
    >>> producto._valor_del_producto
    200.0
    """

if __name__ == "__main__":
    import doctest
    prueba_producto_control()
    doctest.testmod(verbose=True)
