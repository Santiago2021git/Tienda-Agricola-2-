from MODELO import ProductoControl
from MODELO.Fertilizantes import Fertilizante

def prueba_fertilizantes():
    
    """
    Pruebas para la clase Fertilizante.

    >>> fertilizante = Fertilizante("12345", "Fertilizante X", "Mensual", 50.0, "2023-10-19")


    >>> fertilizante._registro_ica
    '12345'
    >>> fertilizante._nombre_del_producto
    'Fertilizante X'
    >>> fertilizante._frecuencia_de_aplicacion
    'Mensual'
    >>> fertilizante._valor_del_producto
    50.0
    >>> fertilizante._fecha_de_ultima_aplicacion
    '2023-10-19'

    >>> fertilizante._fecha_de_ultima_aplicacion = "2023-11-15"
    >>> fertilizante._fecha_de_ultima_aplicacion
    '2023-11-15'
    """

if __name__ == "__main__":
    import doctest
    prueba_fertilizantes()
    doctest.testmod(verbose=True)
