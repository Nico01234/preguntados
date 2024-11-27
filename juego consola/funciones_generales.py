def ingresar_numero(mensaje, mensaje_error, minimo, maximo) -> int:
    """
    ¿Que hace? : Pide al usuario un numero que este dentro un rango especifico
    ¿Que recibe? : 
    - mensaje :(str) Mensaje que se muestra al usuario
    - mensaje_error :(str) Mensaje de error que se muestra al usuario cuando el valor no es valido
    - minimo : (int) Valor minimo del rango
    - maximo : (int) Valor maximo del rango
    ¿Que devuelve? : (int) Numero ingresado por el usuario dentro del
    """
    
    while True:
        numero = input(f"{mensaje}: ")
        if numero.isdecimal():
            numero_int = int(numero)
        
            if numero_int >= minimo and numero_int <= maximo:
                return numero_int
        else:
            print(f"{mensaje_error}: ")
            
def validar_numero(mensaje, mensaje_error) -> int:
    numero = input(f"{mensaje}: ")
    while not numero.isdecimal():
        numero = input(f"{mensaje_error}: ")
    numero = int(numero)
        
    return numero


def preguntar_con_tiempo(pregunta, limite_tiempo):
    import threading
    respuesta = None
    tiempo = threading.Timer(limite_tiempo, print, ("\n tiempo agotado!"))
    tiempo.start()
    respuesta = input(f"{pregunta} tienes {limite_tiempo} segundos para responder\n")
    tiempo.cancel()
    return respuesta