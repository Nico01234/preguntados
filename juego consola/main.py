from juego import *
from funcion_menu import *
from funciones_generales import *
from config import *
from cantidad import * 
import pygame

pygame.display.set_caption("Juego de preguntas")
mensaje = "Ingresar opcion"
mensaje_error = "Ingrese una opcion valida"
minimo = 1
maximo = 4
puntos_respuesta_correcta = 0
cantidad_vidas = 3
cantidad_tiempo = 5

while True:
    mostrar_menu()
    #opcion = ingresar_numero(mensaje, mensaje_error, minimo, maximo)
    opcion = capturar_opcion(1, 5)
    
    match opcion:
        case 1:
            jugar("preguntas.csv", puntos_respuesta_correcta, cantidad_vidas, cantidad_tiempo)
            
        case 2:
            mostrar_ranking(pantalla, "ranking.csv", 200, 200, pygame.font.Font(None, 36), margen=20 )
        
        case 3:
            pass
        
        case 4:
            while True:
                mostrar_submenu()
                opcion = ingresar_numero(mensaje, mensaje_error, 1, 4)
                match opcion:
                    case 1:
                        puntos_respuesta_correcta = modificar_cantidad_puntos()
                        
                    
                    case 2:
                        cantidad_vidas = modificar_cantidad_vidas()
                        
                    case 3:
                        cantidad_tiempo = modificar_cantidad_tiempo()
                    
                    case 4:
                        print("volviendo al menu principal")
                        break
                        
            
