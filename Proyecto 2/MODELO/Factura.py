class Factura:
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
def fecha(self,fecha):
    self._fecha = fecha

@property
def antibiotico(self):
    return self._antibiotico

@antibiotico.setter
def antibiotico(self,antibiotico):
    self._antibiotico.append(antibiotico)


@property
def plaga(self):
    return self._plaga

@plaga.setter
def plaga(self,plaga):
    self._plaga.append(plaga)

@property
def fertilizante(self):
    return self._fertilizante

@fertilizante.setter
def fertilizante(self,fertilizante):
    self._fertilizante.append(fertilizante)
