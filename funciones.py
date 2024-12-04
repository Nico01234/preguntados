import pygame
import csv
import os
from colores import *
from settings import *
from fuentes import *

def pedir_nombre_jugador():
    
    """
    ¿Que hace? : Muestra la pantalla para que el jugador ingrese su nombre
    
    ¿Que recibe? : None
    
    ¿Que devuelve? : Nombre ingresado por el jugador
    """
    
    fondo_juego = pygame.image.load("fondo_juego.jpg") # path de la imagen
    fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))  # Escala la imagen al tamaño de la ventana

    nombre = ''
    fuente = pygame.font.Font(None, 36)
    
    boton_jugar = pygame.Rect(220, 280, 350, 50)
    
    # Bucle para pedir el nombre del jugador
    pidiendo_nombre = True
    while pidiendo_nombre:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()  # Finaliza pygame si se cierra la ventana
                return None
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    pidiendo_nombre = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode
        
        # Dibuja la imagen de fondo
        pantalla.blit(fondo_juego, (0, 0))
        pygame.draw.rect(pantalla, (PURPLE), boton_jugar) #caja para introducir nombre
        texto_titulo = fuente.render(f"Introduce tu nombre:", True, (255, 255, 255))
        pantalla.blit(texto_titulo, (240, 220))
        texto_nombre = fuente.render(f"{nombre}", True, (255, 255, 255))
        pantalla.blit(texto_nombre, (240, 290))  # Mostrar el texto
        
        pygame.display.flip()  # Actualizar la pantalla

    return nombre

def cargar_preguntas(archivo : str) -> list:
    
    """
    ¿Que hace? : Carga preguntas desde un archivo csv
    
    ¿Que recibe? :
    - archivo (str) = El nombre del archivo
    
    ¿Que devuelve? : (list) Una lista de diccionarios
    """
    
    preguntas = []
    
    with open(archivo, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for columna in reader:
            datos = {
                "pregunta": columna["pregunta"],
                "opciones": (columna["opcion1"], columna["opcion2"], columna["opcion3"], columna["opcion4"]),
                "respuesta_correcta": int(columna["respuesta_correcta"]),  # Convertir la respuesta correcta a un entero
                "dificultad":  columna["dificultad"]  # Leer la dificultad de la pregunta
                }
            preguntas.append(datos)
    
    return preguntas




def mostrar_pregunta(pregunta : list, opciones : list, puntos : int, vidas : int) -> list:
    
    """
    ¿Que hace? : Muestra las preguntas, opciones, tiempo y vidas en pantalla
    
    ¿Que recibe? :
    - pregunta (list) : Una lista de preguntas
    - opciones (list) : Una lista de opciones de respuesta
    - puntos (int) : Cantidad de puntos 
    - vidad (int) : Cantidad de vidas 
    
    ¿Que devuelve? : (list) Una lista de botones de opciones
    """
    
    pantalla.fill(PURPLE)

    # Mostrar la pregunta
    texto_pregunta = fuente.render(pregunta, True, BLACK)
    pantalla.blit(texto_pregunta, (80, 80))

    # Mostrar las opciones como botones
    botones = []
    for i, opcion in enumerate(opciones):
        boton_rect = pygame.Rect(50, 130 + i * 70, 700, 50)
        botones.append(boton_rect)
        pygame.draw.rect(pantalla, ORANGE, boton_rect)  # Dibuja el botón
        texto_opcion = fuente.render(opcion, True, BLACK)
        pantalla.blit(texto_opcion, (60, 140 + i * 70))  # Texto dentro del botón
    
    if vidas <= 0:
        return 
    # Mostrar los puntos
    texto_puntos = fuente.render(f"Puntos: {puntos}", True, BLACK)
    pantalla.blit(texto_puntos, (650, 20))  # Ubicación de los puntos

    texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLACK)
    pantalla.blit(texto_vidas, (80, 20))
    
    pygame.display.flip()
    return botones



def mostrar_temporizador(tiempo_restante : int) -> None:
    
    """
    ¿Que hace? : Muestra en pantalla el tiempo restante
    
    ¿Que recibe? :
    - tiempo_restante : (int) tiempo restante del juego
    
    ¿Que devuelve? : None
    """
    
    # Convertir milisegundos a segundos de manera directa
    segundos = tiempo_restante // 1000  # Esto ya da el número de segundos (sin comprobar que no sea negativo)
    
    # Asegurarse de que el valor mostrado no sea negativo
    if segundos < 0:
        segundos = 0  # Esto evita mostrar números negativos en el temporizador

    # Mostrar el temporizador
    texto_tiempo = fuente_segundos.render(f"Tiempo: {segundos}s", True, BLACK)
    pantalla.blit(texto_tiempo, (50, 500))  # Mostrar el temporizador en la esquina superior izquierda
    pygame.display.flip()


def guardar_partida(nombre : str, puntos : int, vidas : int, duracion : int) -> None:
    
    """
    ¿Que hace? : Guarda los datos de la partida en un archivo csv
    
    ¿Que recibe? :
    - nombre (str) : Nombre del jugador ingresado por pantalla
    - puntos (int) : Cantidad de puntos obtenidos por cada respuesta correcta
    - vidas (int) : Cantidad de vidas del jugador
    - duracion (int) : Cantidad del tiempo de la partida jugada
    
    ¿Que devuelve? : None
    """
    
    
    # Ruta del archivo CSV donde se guardarán los datos
    archivo = 'resultados.csv'
    
    # Comprobar si el archivo existe, si no, crearlo con los encabezados
    with open(archivo, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, puntos, vidas, duracion])  # Escribir los datos de la partida


def mostrar_mensaje_fin(nombre : str, puntos : int, vidas : int, duracion : int) -> None:
    
    """
    ¿Que hace? : Muestra los datos del jugador al finalizar la partida
    
    ¿Que recibe? :
    - nombre (str) : Nombre del jugador ingresado por pantalla
    - puntos (int) : Cantidad de puntos obtenidos por cada respuesta correcta
    - vidas (int) : Cantidad de vidas del jugador
    - duracion (int) : Cantidad del tiempo de la partida jugada
    
    ¿Que devuelve? : None
    """
    
    pantalla.fill(FONDO)
    
    # Mostrar mensaje de fin y los datos del juego
    mensajes = [
        "¡Juego terminado!",
        f"Jugador: {nombre}",
        f"Puntos obtenidos: {puntos}",
        f"Vidas restantes: {vidas}",
        f"Duración total: {duracion} segundos"
    ]
    
    for i, mensaje in enumerate(mensajes):
        texto = fuente.render(mensaje, True, BLACK)
        pantalla.blit(texto, (100, 200 + i * 50))  # Espaciado vertical entre líneas
    
    boton_volver = pygame.Rect(ANCHO // 2 - 100, ALTO - 100, 200, 50)
    pygame.draw.rect(pantalla, RED, boton_volver)
    texto_volver = fuente.render("Salir", True, WHITE)
    pantalla.blit(texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 90))
    
    pygame.display.flip()
    
    # Esperar la interacción con el botón
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    esperando = False
    

def actualizar_estadisticas_globales(pregunta, es_correcta):
    archivo = "estadisticas_globales.csv"
    estadisticas = {}
    
    # Leer las estadísticas actuales, si el archivo existe
    if os.path.exists(archivo):
        with open(archivo, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                # estadisticas[fila["Pregunta"]] = {
                #     "aciertos" : int(fila["Aciertos"]),
                #     "fallos" : int(fila["Fallos"]),
                #     "veces_preguntadas" : int(fila["Veces Preguntadas"]) 
                # }
                {
                    "Veces Preguntada": int(fila["Veces Preguntada"]),
                    "Aciertos": int(fila["Aciertos"]),
                    "Fallos": int(fila["Fallos"])
                }
    
    # Actualizar estadísticas de la pregunta actual
    if pregunta in estadisticas:
        estadisticas[pregunta]["Veces Preguntada"] += 1
        if es_correcta:
            estadisticas[pregunta]["Aciertos"] += 1
        else:
            estadisticas[pregunta]["Fallos"] += 1
    # else:
    #     # Nueva pregunta
    #     if es_correcta:
    #         estadisticas[pregunta] = {
    #             "Veces Preguntada" : 1,
    #             "Aciertos" : 1,
    #             "Fallos" : 0
    #         }
            
    #     else:
    #         estadisticas[pregunta] = {
    #             "Veces Preguntada" : 1,
    #             "Aciertos" : 0,
    #             "Fallos" : 1
    #         }
        estadisticas[pregunta] = {
            "Veces Preguntada": 1,
            "Aciertos": 1 if es_correcta else 0,
            "Fallos": 0 if es_correcta else 1
        }
    
    # Calcular porcentaje de aciertos
    for datos in estadisticas.values():
        total = datos["Veces Preguntada"]
        datos["Porcentaje de Aciertos"] = (datos["Aciertos"] / total) * 100

    # Guardar las estadísticas actualizadas
    with open(archivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Pregunta", "Veces Preguntada", "Aciertos", "Fallos", "Porcentaje de Aciertos"])
        writer.writeheader()
        for pregunta, datos in estadisticas.items():
            writer.writerow({
                "Pregunta": pregunta,
                "Veces Preguntada": datos["Veces Preguntada"],
                "Aciertos": datos["Aciertos"],
                "Fallos": datos["Fallos"],
                "Porcentaje de Aciertos": f"{datos['Porcentaje de Aciertos']:.2f}"
            })
            
