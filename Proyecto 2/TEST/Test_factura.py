class Factura:
    """
    Clase que representa una factura.

    Args:
        fecha (str): La fecha de la factura.

    Example:
        >>> factura = Factura("2023-10-20")
        >>> factura.fecha
        '2023-10-20'

    Attributes:
        fecha (str): La fecha de la factura.

    Properties:
        antibiotico (list): Lista de antibióticos.
        plaga (list): Lista de plagas.
        fertilizante (list): Lista de fertilizantes.

    Example:
        >>> factura.antibiotico = "Amoxicilina"
        >>> factura.antibiotico
        ['Amoxicilina']
        >>> factura.plaga = "Mosquitos"
        >>> factura.plaga
        ['Mosquitos']
        >>> factura.fertilizante = "Nitrógeno"
        >>> factura.fertilizante
        ['Nitrógeno']
    """

    def __init__(self, fecha):
        self._fecha = fecha
        self._valor_de_la_compra = 0
        self._antibiotico = []
        self._plaga = []
        self._fertilizante = []

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def antibiotico(self):
        return self._antibiotico

    @antibiotico.setter
    def antibiotico(self, antibiotico):
        self._antibiotico.append(antibiotico)

    @property
    def plaga(self):
        return self._plaga

    @plaga.setter
    def plaga(self, plaga):
        self._plaga.append(plaga)

    @property
    def fertilizante(self):
        return self._fertilizante

    @fertilizante.setter
    def fertilizante(self, fertilizante):
        self._fertilizante.append(fertilizante)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
