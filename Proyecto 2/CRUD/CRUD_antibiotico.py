from MODELO import Antibiotico
from UI import InterfazGrafica

registros_antibiotico = []


def print_options():
    print("REGISTROS DE ANTIBIOTICO ")
    print('*' * 50)
    print("[C]rear antibiotico")
    print("[L]istar antibiotico")
    print("[E]liminar antibiotico")
    print("[S]alir")
    run()

def run():
    command = input()
    command = command.upper()

    if command == 'C':
        crear_antibiotico()
    elif command == 'L':
        imprimir()
    elif command == 'E':
        eliminar_antibioico()
    elif command == 'S':
        InterfazGrafica.escoger_opciones()
    else:
        print("comando invalido")
        run()


def crear_antibiotico():
    nombre_del_producto, dosis, precio = ingreso_de_datos_antibiotico()
    mi_antibiotico = Antibiotico.Antibiotico(nombre_del_producto, dosis, precio)
    registros_antibiotico.append(mi_antibiotico)
    print_options()


def ingreso_de_datos_antibiotico():
    nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
    dosis = (str(input("Ingrese la dosis del producto: ")))
    precio = (int(input("Ingrese ingrese el precio: ")))
    return nombre_del_producto, dosis, precio


def imprimir():
    tamaño = len(registros_antibiotico)
    contador = 0
    while contador <= tamaño - 1:
        print('*' * 50)
        print(f"Nombre del antibiotico: {registros_antibiotico[contador]._nombre_del_producto}")
        print(f"Dosis Recomendada: {registros_antibiotico[contador]._dosis}")
        print(f"Tipo de animal: {registros_antibiotico[contador]._tipo_de_animal}")
        print(f"Precio: {registros_antibiotico[contador]._precio}")
        print('*' * 50)

        contador += 1
    print_options()


def eliminar_antibioico():
    producto = (str(input("ingrese el nombre del producto que desea eliminar: ")))
    producto = producto.upper()
    tamaño = len(registros_antibiotico)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_antibiotico[eliminador]._nombre_del_producto.upper()
        if producto == eliminar:
            del registros_antibiotico[eliminador]
            break

        eliminador += 1
    print_options()


def buscar_producto():
    producto = str(input("ingrese el nombre del producto que desea buscar: "))
    producto = producto.upper()
    tamaño = len(registros_antibiotico)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_antibiotico[buscador]._nombre_del_producto.upper()
        if producto == buscar:
            print(f"Nombre del antibiotico: {registros_antibiotico[buscador]._nombre_del_producto}")
            print(f"Dosis Recomendada: {registros_antibiotico[buscador]._dosis}")
            print(f"Tipo de animal: {registros_antibiotico[buscador]._tipo_de_animal}")
            print(f"Precio: {registros_antibiotico[buscador]._precio}")
            break

        buscador += 1

    if buscador == tamaño:
        print("el producto que esta buscando no existe en el inventario")

    return registros_antibiotico[buscador]

