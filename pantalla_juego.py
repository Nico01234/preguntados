import pygame
from colores import *
from config_cantidad import *
from constantes import *
from colores import *
from funciones import *
from settings import *
from pantalla_config import *


# Inicializar pygame
pygame.init()

fondo_juego = pygame.image.load("fondo_juego.jpg") # path de la imagen
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))  # Escala la imagen al tamaño de la ventana

pygame.display.set_caption("Juego de Preguntas")


def jugar(tiempo_por_pregunta, cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil, cantidad_de_vidas) -> str:
    
    """
    ¿Que hace? : Inicia el juego, mostrando las preguntas, cantidad de tiempo, puntos y vidas.
    
    ¿Que recibe? : 
    - tiempo_por_pregunta : (int) tiempo limite por pregunta
    - cantidad_de_puntos_facil : (int) cantidad de puntos para nivel fácil
    - cantidad_de_puntos_intermedio : (int) cantidad de puntos para nivel intermedio
    - cantidad_de_puntos_dificil : (int) cantidad de puntos para nivel dificil
    - cantidad_de_vidas_int : (int) cantidad de vidas
    
    ¿Que devuelve? : 
    - (str) : guarda los datos de la partida
    """
    
    nombre_jugador = pedir_nombre_jugador() 
    preguntas = cargar_preguntas('preguntas.csv')  # Asegúrate de que este archivo exista y esté en el formato correcto
    pregunta_actual = 0
    puntos = 0  # Contador de puntos
    vidas = cantidad_de_vidas
    
    
    #tiempo_por_pregunta = tiempo_por_pregunta  # Tiempo en segundos para responder cada pregunta
    reloj = pygame.time.Clock()  # Reloj para manejar el tiempo
    tiempo_restante = tiempo_por_pregunta * 1000 # Convertir segundos a milisegundos

    tiempo_inicio = pygame.time.get_ticks() 
    
    # Bucle principal del juego
    jugando = True

    while jugando:
        tiempo_transcurrido = reloj.tick(30)  # Limita a 30 cuadros por segundo y devuelve el tiempo transcurrido
        tiempo_restante -= tiempo_transcurrido # Reduce el tiempo restante según el tiempo transcurrido
        print(tiempo_restante)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener posición del mouse
                pos = pygame.mouse.get_pos()

                # Verificar en qué botón se hizo clic
                botones = mostrar_pregunta(
                    preguntas[pregunta_actual]["pregunta"], 
                    preguntas[pregunta_actual]["opciones"], 
                    puntos, 
                    vidas
                )
                
                
                for i, boton in enumerate(botones):
                    if boton.collidepoint(pos):  # Si el clic fue dentro del botón
                        if i + 1 == preguntas[pregunta_actual]["respuesta_correcta"]:
                            if preguntas[pregunta_actual]["dificultad"] == "facil":
                                puntos += cantidad_de_puntos_facil
                            elif preguntas[pregunta_actual]["dificultad"] == "intermedio":
                                puntos += cantidad_de_puntos_intermedio
                            else:
                                puntos += cantidad_de_puntos_dificil
                        else:
                            vidas -= 1
                        actualizar_estadisticas_globales(preguntas[pregunta_actual]["pregunta"], puntos)
                        
                        pregunta_actual += 1  # Ir a la siguiente pregunta
                        tiempo_restante = tiempo_por_pregunta * 1000 # Reiniciar el tiempo para la nueva pregunta
                    print(f"Pregunta: {pregunta_actual}")
                    print(f"Opciones: {pregunta_actual}")
                    print(f"Respuesta correcta (índice): {pregunta_actual}")
                    print(cantidad_de_puntos_facil)
                    print(cantidad_de_puntos_intermedio)
                    print(cantidad_de_puntos_dificil)
                    print(vidas)
                    print(f"Índice seleccionado: {i}")

                # Si el tiempo se acaba, considerar la respuesta incorrecta
        if tiempo_restante <= 0:
            vidas -= 1
            pregunta_actual += 1
            tiempo_restante = tiempo_por_pregunta * 1000 # Reiniciar el tiempo
            
            if vidas == 0:
                tiempo_total = (pygame.time.get_ticks() - tiempo_inicio)  // 1000
                mostrar_mensaje_fin(nombre_jugador, puntos, vidas, tiempo_total)
                return guardar_partida(nombre_jugador, puntos, vidas, tiempo_total)

            actualizar_estadisticas_globales(preguntas[pregunta_actual]["pregunta"], False)
            
            # Verificar si hemos llegado a la última pregunta
        if pregunta_actual >= len(preguntas):
            tiempo_total = (pygame.time.get_ticks() - tiempo_inicio) // 1000  # Calcular el tiempo total
            # Una vez respondida la última pregunta, mostrar el menú principal
            mostrar_mensaje_fin(nombre_jugador, puntos, vidas, tiempo_total)
            return guardar_partida(nombre_jugador, puntos, vidas, tiempo_total)
        
        print(len(preguntas))
        
        # Mostrar la pregunta actual con el tiempo restante
        mostrar_pregunta(preguntas[pregunta_actual]["pregunta"], 
            preguntas[pregunta_actual]["opciones"], puntos, vidas)

        # Mostrar el temporizador
        mostrar_temporizador(tiempo_restante)
    
    pygame.display.flip()
    
    pygame.quit()
