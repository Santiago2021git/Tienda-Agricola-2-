from CRUD import CRUD_cliente
from CRUD import CRUD_fertilizante
from CRUD import CRUD_antibiotico
from CRUD import CRUD_factura
from CRUD import CRUD_control_de_plagas


def opciones():
    print("seleccione la opcion que corresponda al area al que desea ingresar:")
    print("1.REGISTRO DE CLIENTES")
    print("2.REGISTRO DE ANTIBIOTICOS")
    print("3.REGISTRO DE PESTICIDAS")
    print("4.REGISTRO DE FERTILIZANTES")
    print("5.FACTURACION")
    print("6.SALIR")
    opcion = int(input("su eleccion es la opcion: "))
    return opcion


def escoger_opciones():
    opcion = opciones()
    if opcion == 1:
        CRUD_cliente.print_options()

    if opcion == 2:
        CRUD_antibiotico.print_options()

    if opcion == 3:
        CRUD_control_de_plagas.print_options()

    if opcion == 4:
        CRUD_fertilizante.print_options()

    if opcion == 5:
        CRUD_factura.print_options()

    if opcion == 6:
        pass
