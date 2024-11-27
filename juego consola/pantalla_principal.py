import pygame
from constantes import *

pygame.init()


def mostrar_ranking(pantalla, ranking, ancho, alto, fuente, margen=20):
    """
    Muestra el ranking en una tabla usando pygame.
    :param pantalla: La superficie de pygame donde se renderizará la tabla.
    :param ranking: Lista de tuplas con el formato (nombre, puntaje, respuestas_correctas).
    :param ancho: Ancho total de la tabla.
    :param alto: Alto total de la tabla.
    :param fuente: Fuente de pygame para el texto.
    :param margen: Espacio entre las filas y columnas.
    """
    pantalla.fill((255, 255, 255))  # Fondo blanco
    color_titulo = (0, 0, 0)  # Color del título
    color_filas = (50, 50, 50)  # Color del texto de las filas

    # Coordenadas iniciales para la tabla
    x_inicio = margen
    y_inicio = margen

    # Títulos de las columnas
    encabezados = ["Posición", "Nombre", "Puntaje", "Correctas"]
    columnas = len(encabezados)

    # Calcular el ancho de cada columna
    ancho_columna = (ancho - 2 * margen) // columnas

    # Dibujar encabezados
    for i, titulo in enumerate(encabezados):
        texto = fuente.render(titulo, True, color_titulo)
        pantalla.blit(texto, (x_inicio + i * ancho_columna, y_inicio))

    # Dibujar líneas horizontales para la separación
    y_inicio += margen

    # Dibujar filas del ranking
    for i, (nombre, puntaje, correctas) in enumerate(ranking, start=1):
        fila = [str(i), nombre, str(puntaje), str(correctas)]
        for j, dato in enumerate(fila):
            texto = fuente.render(dato, True, color_filas)
            pantalla.blit(texto, (x_inicio + j * ancho_columna, y_inicio + i * margen))

    pygame.display.flip()
