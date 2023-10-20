from MODELO import Fertilizantes
from UI import InterfazGrafica


registros_fertilizantes = []


def print_options():
    print("REGISTROS DE FERTILIZANTES ")
    print('*' * 50)
    print("[C]rear fertilizante")
    print("[L]istar fertilizante")
    print("[E]liminar fertilizante")
    print("[S]alir")
    run()

def run():
    command = input()
    command = command.upper()

    if command == 'C':
        crear_fertilizante()
    elif command == 'L':
        imprimir()
    elif command == 'E':
        eliminar_fertilizante()
    elif command == 'B':
        buscar_producto()
    elif command == 'S':
        InterfazGrafica.escoger_opciones()
    else:
        print("comando invalido")
        run()


def crear_fertilizante():
    (registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto,
     fecha_de_ultima_aplicacion) = ingreso_de_datos_fertilizante()
    mi_fertilizante = Fertilizantes.Fertilizante(registro_ica, nombre_del_producto, frecuencia_de_aplicacion,
                                   valor_del_producto, fecha_de_ultima_aplicacion)
    registros_fertilizantes.append(mi_fertilizante)
    print_options()


def ingreso_de_datos_fertilizante():
    registro_ica = (str(input("Ingrese el registro ICA del producto: ")))
    nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
    frecuencia_de_aplicacion = (str(input("Ingrese la frecuencia de aplicacion del producto: ")))
    valor_del_producto = (int(input("Ingrese ingrese el precio: ")))
    fecha_de_ultima_aplicacion = (str(input("Ingrese la fecha de ultima aplicacion del producto: ")))
    return registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, fecha_de_ultima_aplicacion


def imprimir():
    tamaño = len(registros_fertilizantes)
    contador = 0
    while contador <= tamaño - 1:
        print('*' * 50)
        print(f"Registro ICA: {registros_fertilizantes[contador]._registro_ica}")
        print(f"Nombre del fertilizante: {registros_fertilizantes[contador]._nombre_del_producto}")
        print(f"Frecuencia de aplicacion: {registros_fertilizantes[contador]._frecuencia_de_aplicacion}")
        print(f"Precio: {registros_fertilizantes[contador]._valor_del_producto}")
        print(f"Fecha de ultima aplicacion: {registros_fertilizantes[contador]._fecha_de_ultima_aplicacion}")
        print('*' * 50)

        contador += 1
    print_options()


def eliminar_fertilizante():
    producto = (str(input("ingrese el nombre del producto que desea eliminar: ")))
    producto = producto.upper()
    tamaño = len(registros_fertilizantes)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_fertilizantes[eliminador]._nombre_del_producto.upper()
        if producto == eliminar:
            del registros_fertilizantes[eliminador]
            break

        eliminador += 1
    print_options()


def buscar_producto():
    producto = str(input("ingrese el nombre del producto que desea buscar: "))
    producto = producto.upper()
    tamaño = len(registros_fertilizantes)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_fertilizantes[buscador]._nombre_del_producto.upper()
        if producto == buscar:
            print('*' * 50)
            print(f"Registro ICA: {registros_fertilizantes[buscador]._registro_ica}")
            print(f"Nombre del fertilizante: {registros_fertilizantes[buscador]._nombre_del_producto}")
            print(f"Frecuencia de aplicacion: {registros_fertilizantes[buscador]._frecuencia_de_aplicacion}")
            print(f"Precio: {registros_fertilizantes[buscador]._valor_del_producto}")
            print(f"Fecha de ultima aplicacion: {registros_fertilizantes[buscador]._fecha_de_ultima_aplicacion}")
            print('*' * 50)
            break

        buscador += 1

    if buscador == tamaño:
        print("el producto que esta buscando no existe en el inventario")

    return registros_fertilizantes[buscador]

