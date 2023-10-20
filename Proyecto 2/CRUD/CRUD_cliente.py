from CRUD import CRUD_factura
from MODELO import Cliente
from UI import InterfazGrafica


registros_clientes = []


def print_options():
    print("REGISTROS DE CLIENTES ")
    print('*' * 50)
    print("[C]rear cliente")
    print("[L]istar clientes")
    print("[E]liminar cliente")
    print("[S]alir")
    run()

def run():
    command = input()
    command = command.upper()

    if command == 'C':
        crear_cliente()
    elif command == 'L':
        imprimir_clientes()
    elif command == 'E':
        eliminar_cliente()
    elif command == 'S':
        InterfazGrafica.escoger_opciones()
    else:
        print("comando invalido")
        run()


def crear_cliente():
    nombre, cedula = ingreso_de_datos_cliente()
    mi_cliente = Cliente.Cliente(nombre, cedula)
    registros_clientes.append(mi_cliente)
    print_options()


def ingreso_de_datos_cliente():
    nombre = (str(input("Ingrese el nombre del cliente: ")))
    cedula = (int(input("Ingrese la cedula del cliente: ")))
    return nombre, cedula


def imprimir_clientes():
    contador = 0
    tamaño = len(registros_clientes)
    while contador <= tamaño - 1:
        print('*' * 50)
        print("nombre del cliente: ", registros_clientes[contador]._nombre)
        print("cedula: ", registros_clientes[contador]._cedula)

        contador += 1
    print_options()


def imprimir():
    contador = 0
    tamaño = len(registros_clientes)
    while contador <= tamaño - 1:
        print('*' * 50)
        print("nombre del cliente: ", registros_clientes[contador]._nombre)
        print("cedula: ", registros_clientes[contador]._cedula)

        contador_facturas = 0
        tamaño_facturas = len(registros_clientes[contador]._factura_cliente)
        while contador_facturas <= tamaño_facturas - 1:
            print('*' * 50)
            print("Datos de la Factura")
            print("fecha de la factura: ", registros_clientes[contador]._factura_cliente[contador_facturas]._fecha)
            print("valor de la compra: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                  ._valor_de_la_compra)

            contador_antibioticos = 0
            contador_fertilizantes = 0
            contador_pesticidas = 0
            tamaño_antibioticos = len(registros_clientes[contador]._factura_cliente[contador_facturas]._antibiotico)
            tamaño_fertilizanes = len(registros_clientes[contador]._factura_cliente[contador_facturas]._fertilizante)
            tamaño_pesticidas = len(registros_clientes[contador]._factura_cliente[contador_facturas]._plaga)

            while contador_antibioticos <= tamaño_antibioticos - 1:
                print('*' * 50)
                print("antibioticos")
                print("nombre del producto: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._nombre_del_producto)
                print("dosis(entre 400kg y 600kg): ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._dosis)
                print("tipo de animal: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._tipo_de_animal)
                print("precio: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._antibiotico[contador_antibioticos]._precio)

                contador_antibioticos += 1

            while contador_pesticidas <= tamaño_pesticidas - 1:
                print('*' * 50)
                print("productos de control : plagas")
                print("registro ica: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._registro_ica)
                print("nombre del producto: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._nombre_del_producto)
                print("frecuencia de aplicacion: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._frecuencia_de_aplicacion)
                print("valor del producto: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._valor_del_producto)
                print("periodo de carencia: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._plaga[contador_pesticidas]._periodo_de_carencia)

                contador_pesticidas += 1

            while contador_fertilizantes <= tamaño_fertilizanes - 1:
                print("           ")
                print("productos de control : fertilizantes")
                print("registro ica", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._registro_ica)
                print("nombre del producto", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._nombre_del_producto)
                print("frecuencia de aplicacion", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._frecuencia_de_aplicacion)
                print("valor del producto", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._valor_del_producto)
                print("fecha de ultima aplicacion: ", registros_clientes[contador]._factura_cliente[contador_facturas]
                      ._fertilizante[contador_fertilizantes]._fecha_de_ultima_aplicacion)

                contador_fertilizantes += 1

            contador_facturas += 1

        contador += 1
    CRUD_factura.print_options()


def eliminar_cliente():
    cedula = int(input("ingrese la cedula del cliente que desea eliminar: "))
    tamaño = len(registros_clientes)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_clientes[eliminador]._cedula
        if cedula == eliminar:
            del registros_clientes[eliminador]
            break

        eliminador += 1
    print_options()


def buscar_cliente():
    cedula = int(input("ingrese la cedula del cliente que desea buscar: "))
    tamaño = len(registros_clientes)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_clientes[buscador]._cedula
        if cedula == buscar:
            print(f"Nombre del cliente: {registros_clientes[buscador]._nombre}")
            print(f"Cedula del cliente: {registros_clientes[buscador]._cedula}")
            numero_de_facturas = len(registros_clientes[buscador]._factura_cliente)
            print(f"Numero de facturas: {numero_de_facturas}")
            break

        buscador += 1

    if buscador == tamaño:
        print("el cliente que esta buscando no esta registrado")

    return buscador

