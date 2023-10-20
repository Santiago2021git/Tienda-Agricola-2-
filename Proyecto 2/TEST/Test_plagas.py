from MODELO import ProductoControl
from MODELO.Plagas import Plaga

def prueba_plaga():
    """

    Crear un objeto Plaga y acceder a sus atributos.

    >>> plaga = Plaga("456XYZ", "Plaga X", "Semanal", 50.0, 7)
    >>> plaga._registro_ica
    '456XYZ'
    >>> plaga._nombre_del_producto
    'Plaga X'
    >>> plaga._frecuencia_de_aplicacion
    'Semanal'
    >>> plaga._valor_del_producto
    50.0
    >>> plaga._periodo_de_carencia
    7

    >>> plaga._periodo_de_carencia = 14
    >>> plaga._periodo_de_carencia
    14
    """

if __name__ == "__main__":
    import doctest
    prueba_plaga()
    doctest.testmod(verbose=True)
