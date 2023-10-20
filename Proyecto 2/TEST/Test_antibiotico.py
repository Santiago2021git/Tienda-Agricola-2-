from MODELO.Antibiotico import Antibiotico

def prueba_antibiotico():
    """
    >>> antibiotico = Antibiotico("Antibiotico1", "10mg", 20.0)
    >>> antibiotico._nombre_del_producto
    'Antibiotico1'
    >>> antibiotico._dosis
    '10mg'
    >>> antibiotico._precio
    20.0

    >>> antibiotico._nombre_del_producto = "Antibiotico2"
    >>> antibiotico._nombre_del_producto
    'Antibiotico2'

    >>> antibiotico._dosis = "5mg"
    >>> antibiotico._dosis
    '5mg'

    >>> antibiotico._precio = 15.0
    >>> antibiotico._precio
    15.0
    """

if __name__ == "__main__":
    import doctest
    prueba_antibiotico()
    doctest.testmod(verbose=True)
