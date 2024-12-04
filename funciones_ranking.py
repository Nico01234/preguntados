import pygame
import csv
from colores import *
from constantes import *
from funciones import *
from fuentes import *
# Inicializar pygame
pygame.init()


# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ranking de Jugadores")

# ordena de mayor a menor
def ordenar_mayor_menor(lista: list) -> list:
    """
    ¿Que hace? : Ordena de mayor a menor una lista recibida por parametro
    ¿Que recibe? : 
    - lista : (list) Lista de enteros
    ¿Que devuelve? : (list) Lista de enteros ordenados de mayor a menor
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

# leer archivo csv
def leer_ranking(nombre_archivo: str) -> list:
    """
    ¿Que hace? : Lee un archivo csv 
    ¿Que recibe? : 
    - nombre_archivo : (str) nombre del archivo csv
    ¿Que devuelve? : (list) Una lista de listas
    """
    jugadores = []
    
    with open(nombre_archivo) as archivo:
        read = csv.reader(archivo)
        for columna in read:
            nombre = columna[0]
            puntaje = int(columna[1])
            respuestas_correctas = int(columna[2])
            segundos_totales = int(columna[3])  # Aquí se lee la columna de segundos
            jugadores.append([nombre, puntaje, respuestas_correctas, segundos_totales])
    return jugadores


def obtener_ranking(lista):
    """
    ¿Que hace? : Lee un archivo csv 
    ¿Que recibe? : 
    - nombre_archivo : (str) nombre del archivo csv
    ¿Que devuelve? : (list) Una lista de listas
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
    ¿Que hace? : dibuja la pantalla de ranking 
    ¿Que recibe? : 
    - nombre_archivo : superficie a dibujar los datos
    ¿Que devuelve? : (list) Una lista de listas
    """
    pantalla.fill(PURPLE)
    titulo = fuente_titulo.render("TOP 10", True, WHITE)
    pantalla.blit(titulo, (300, 50))

    for i, jugador in enumerate(ranking):
        texto = f"{i+1}. {jugador[0]} - {jugador[1]} puntos - Vidas: {jugador[2]} - {jugador[3]} Segundos"
        if i == 0:
            color = YELLOW
        else:
            color = WHITE
        texto_ranking = fuente.render(texto, True, color)
        pantalla.blit(texto_ranking, (50, 100 + i * 45))

    boton_volver = DIMENSION_BOTON_SALIR_RANKING
    pygame.draw.rect(pantalla, ORANGE, boton_volver)
    texto_volver = fuente_boton.render("menu", True, WHITE)
    pantalla.blit(texto_volver, (350, 535))
    
    # Actualiza la pantalla
    pygame.display.update()

    # Manejo de eventos
    respuesta = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver.collidepoint(event.pos):
                respuesta = True  # El botón fue presionado
    
    return respuesta # El botón no fue presionado