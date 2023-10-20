from CRUD import CRUD_cliente
from CRUD import CRUD_fertilizante
from CRUD import CRUD_antibiotico
from CRUD import CRUD_control_de_plagas
from MODELO import Factura
from UI import InterfazGrafica


def print_options():
    print("REGISTROS DE FACTURAS ")
    print('*' * 50)
    print("[C]rear factura")
    print("[L]istar facturas")
    print("[S]alir")
    run()

def run():
    command = input()
    command = command.upper()

    if command == 'C':
        agregar_factura_a_cliente(CRUD_cliente.registros_clientes)
    elif command == 'L':
        CRUD_cliente.imprimir()
    elif command == 'S':
        InterfazGrafica.escoger_opciones()
    else:
        print("comando invalido")
        run()


def agregar_factura_a_cliente(clientes):
    factura_mi_cliente = crear_factura()
    cliente = CRUD_cliente.buscar_cliente()
    clientes[cliente]._factura_cliente.append(factura_mi_cliente)
    print_options()


def crear_factura():
    fecha = ingreso_de_datos_factura()
    precio_factura = 0
    factura_mi_cliente = Factura.Factura(fecha)
    eleccion2 = 0
    while eleccion2 != 4:
        print("    ")
        print("1.agregar antibiotico")
        print("2.agregar pesticida")
        print("3.agregarproducto de control fertilizante")
        print("4.Salir")
        eleccion2 = (int(input("Ingrese la opcion: ")))

        if eleccion2 == 1:
            mi_antibiotico = CRUD_antibiotico.buscar_producto()
            precio_factura = precio_factura + mi_antibiotico._precio
            factura_mi_cliente._antibiotico.append(mi_antibiotico)

        if eleccion2 == 2:
            mi_pesticida = CRUD_control_de_plagas.buscar_producto()
            precio_factura = precio_factura + mi_pesticida._valor_del_producto
            factura_mi_cliente._plaga.append(mi_pesticida)

        if eleccion2 == 3:
            mi_fertilizante = CRUD_fertilizante.buscar_producto()
            precio_factura = precio_factura + mi_fertilizante._valor_del_producto
            factura_mi_cliente._fertilizante.append(mi_fertilizante)

    factura_mi_cliente._valor_de_la_compra = precio_factura
    return factura_mi_cliente


def ingreso_de_datos_factura():
    fecha = (str(input("Ingrese la fecha de la factura: ")))
    return fecha

