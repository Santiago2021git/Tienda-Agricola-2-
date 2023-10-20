from MODELO import Plagas
from UI import InterfazGrafica


registros_pesticidas = []


def print_options():
    print("REGISTROS DE PRODUCTOS DE CONTROL DE PLAGAS ")
    print('*' * 50)
    print("[C]rear peticida")
    print("[L]istar pesticidas")
    print("[E]liminar psticida")
    print("[S]alir")
    run()


def run():
    command = input()
    command = command.upper()

    if command == 'C':
        crear_pesticida()
    elif command == 'L':
        imprimir()
    elif command == 'E':
        eliminar_pesticida()
    elif command == 'S':
        InterfazGrafica.escoger_opciones()
    else:
        print("comando invalido")
        run()


def crear_pesticida():
    (registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto,
     periodo_de_carencia) = ingreso_de_datos_fertilizante()
    mi_fertilizante = Plagas.Plaga(registro_ica, nombre_del_producto, frecuencia_de_aplicacion,
                                   valor_del_producto, periodo_de_carencia)
    registros_pesticidas.append(mi_fertilizante)
    print_options()


def ingreso_de_datos_fertilizante():
    registro_ica = (str(input("Ingrese el registro ICA del producto: ")))
    nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
    frecuencia_de_aplicacion = (str(input("Ingrese la frecuencia de aplicacion del producto: ")))
    valor_del_producto = (int(input("Ingrese ingrese el precio: ")))
    periodo_de_carencia = (str(input("Ingrese la fecha de ultima aplicacion del producto: ")))
    return registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, periodo_de_carencia


def imprimir():
    tamaño = len(registros_pesticidas)
    contador = 0
    while contador <= tamaño - 1:
        print('*' * 50)
        print(f"Registro ICA: {registros_pesticidas[contador]._registro_ica}")
        print(f"Nombre del fertilizante: {registros_pesticidas[contador]._nombre_del_producto}")
        print(f"Frecuencia de aplicacion: {registros_pesticidas[contador]._frecuencia_de_aplicacion}")
        print(f"Precio: {registros_pesticidas[contador]._valor_del_producto}")
        print(f"Periodo de carencia: {registros_pesticidas[contador]._periodo_de_carencia}")
        print('*' * 50)

        contador += 1
    print_options()


def eliminar_pesticida():
    producto = (str(input("ingrese el nombre del producto que desea eliminar: ")))
    producto = producto.upper()
    tamaño = len(registros_pesticidas)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_pesticidas[eliminador]._nombre_del_producto.upper()
        if producto == eliminar:
            del registros_pesticidas[eliminador]
            break

        eliminador += 1
    print_options()


def buscar_producto():
    producto = str(input("ingrese el nombre del producto que desea buscar: "))
    producto = producto.upper()
    tamaño = len(registros_pesticidas)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_pesticidas[buscador]._nombre_del_producto.upper()
        if producto == buscar:
            print('*' * 50)
            print(f"Registro ICA: {registros_pesticidas[buscador]._registro_ica}")
            print(f"Nombre del fertilizante: {registros_pesticidas[buscador]._nombre_del_producto}")
            print(f"Frecuencia de aplicacion: {registros_pesticidas[buscador]._frecuencia_de_aplicacion}")
            print(f"Precio: {registros_pesticidas[buscador]._valor_del_producto}")
            print(f"Periodo de carencia: {registros_pesticidas[buscador]._periodo_de_carencia}")
            print('*' * 50)
            break

        buscador += 1

    if buscador == tamaño:
        print("el producto que esta buscando no existe en el inventario")

    return registros_pesticidas[buscador]

