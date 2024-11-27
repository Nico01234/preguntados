
def modificar_cantidad_puntos() -> int:
    cantidad_modificada = input("Ingrese la cantidad de puntos por respuestas correctas: ")
    while not cantidad_modificada.isdecimal():
        cantidad_modificada = input("Ingrese la cantidad de puntos por respuestas correctas: ")
    cantidad = int(cantidad_modificada)
    return cantidad


def modificar_cantidad_vidas() -> int:
    cantidad_modificada = input("Ingrese la cantidad de vidas: ")
    while not cantidad_modificada.isdecimal():
        cantidad_modificada = input("Ingrese la cantidad de vidas: ")
    cantidad = int(cantidad_modificada)
    return cantidad


def modificar_cantidad_tiempo() -> int:
    cantidad_modificada = input("Ingrese la cantidad de tiempo: ")
    while not cantidad_modificada.isdecimal():
        cantidad_modificada = input("Ingrese la cantidad de tiempo: ")
    cantidad = int(cantidad_modificada)
    return cantidad
