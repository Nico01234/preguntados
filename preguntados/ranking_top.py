import pygame
import csv
from colores import *
# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ranking de Jugadores")

# Fuente
fuente = pygame.font.Font(None, 40)  # Tamaño de texto

# Funciones del sistema
def ordenar_mayor_menor(lista: list) -> list:
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def leer_ranking(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de jugadores con nombre, puntaje, respuestas correctas, y segundos totales.
    """
    jugadores = []
    with open(nombre_archivo) as archivo:
        reader = csv.reader(archivo)
        for columna in reader:
            nombre = columna[0]
            puntaje = int(columna[1])
            respuestas_correctas = int(columna[2])
            segundos_totales = int(columna[3])  # Aquí se lee la columna de segundos
            jugadores.append([nombre, puntaje, respuestas_correctas, segundos_totales])
    return jugadores

def obtener_ranking(lista):
    """
    Obtiene el top 10 de jugadores basado en puntajes.
    """
    puntajes = [jugador[1] for jugador in lista]
    jugadores_ordenados = ordenar_mayor_menor(puntajes)
    ranking_top10 = []
    for puntaje in jugadores_ordenados[:10]:
        for jugador in lista:
            if jugador[1] == puntaje and (jugador[0], puntaje) not in ranking_top10:
                ranking_top10.append((jugador[0], puntaje, jugador[2], jugador[3]))  # Incluye los segundos
                break
    return ranking_top10

def mostrar_ranking(pantalla, ranking):
    """
    Dibuja el ranking en la pantalla.
    """
    pantalla.fill(PURPLE)
    titulo = fuente.render("Top 10 Ranking", True, WHITE)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 50))

    y_inicial = 150
    for i, jugador in enumerate(ranking):
        texto = f"{i+1}. {jugador[0]} - {jugador[1]} puntos - Vidas: {jugador[2]} - {jugador[3]} Segundos"
        color = GREEN if i == 0 else WHITE
        texto_ranking = fuente.render(texto, True, color)
        pantalla.blit(texto_ranking, (50, y_inicial + i * 40))

    boton_volver = pygame.Rect(ANCHO // 2 - 100, ALTO - 100, 200, 50)
    pygame.draw.rect(pantalla, RED, boton_volver)
    texto_volver = fuente.render("Salir", True, WHITE)
    pantalla.blit(texto_volver, (ANCHO // 2 - texto_volver.get_width() // 2, ALTO - 90))
    return boton_volver
