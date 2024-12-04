
def calcular_centro_pantalla(dimensiones_pantalla : tuple, dimensiones_texto: tuple) -> int:
    
    """
    ¿Que hace? : Calcula el centro de pantalla en horizontal
    
    ¿Que recibe? : 
    - dimensiones_pantalla : (tuple) 
    - dimensiones_texto : (tuple)
    
    ¿Que devuelve? : (int) entero como coordenada x 
    """
    
    centro = dimensiones_pantalla[0] // 2
    centro_texto = dimensiones_texto[0] // 2
    
    return centro - centro_texto
