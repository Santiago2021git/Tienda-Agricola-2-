from MODELO.Cliente import Cliente

def prueba_cliente():
    """
    >>> cliente = Cliente("Juan", "12345")
    >>> cliente._nombre
    'Juan'
    >>> cliente._cedula
    '12345'

    >>> cliente._nombre = "Maria"
    >>> cliente._nombre
    'Maria'

    >>> cliente._cedula = "54321"
    >>> cliente._cedula
    '54321'
    """

if __name__ == "__main__":
    import doctest
    prueba_cliente()
    doctest.testmod(verbose=True)
