
import pygame
from funciones_principal import *
from colores import *
from fuentes import *
from constantes import *
from funciones_ranking import *

jugadores = leer_ranking("resultados.csv")
# Obtener el ranking Top 10
ranking_top_10 = obtener_ranking(jugadores)

def pantalla_ranking():
    
    """
    ¿Que hace? : Muestra la pantalla de ranking
    
    ¿Que recibe? : None
    
    ¿Que devuelve? : None
    """
    
    pygame.init()
    
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Preguntados - Configuraciones") # nombre del juego
    icono = pygame.image.load("icono.png") # path de la imagen
    icono = pygame.transform.scale(icono, (350, 200)) # redimensiono la imagen
    pygame.display.set_icon(icono) # icono del juego
    
    texto = fuente_titulo.render("RANKING", True, PURPLE)
    texto_boton_cantidad_de_puntos = fuente_boton.render("Top 10", True, WHITE)
    texto_boton_salir = fuente_boton.render("Salir", True, WHITE)
    
    
    # botones
    boton_top10 = pygame.Rect(200, 300, 390, 50)
    boton_salir = pygame.Rect(250, 530, 300, 50)
    
    
    bandera = True
    
    while bandera:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_posicion = pygame.mouse.get_pos()
                if boton_top10.collidepoint(mouse_posicion):
                    while True:
                        if mostrar_ranking(pantalla, ranking_top_10):
                            break
                if boton_salir.collidepoint(mouse_posicion):
                    bandera = False
    
        
        # rellenar pantalla con un color
        pantalla.fill(FONDO)
        
        
        # dibujar el boton
        pygame.draw.rect(pantalla, (PURPLE), boton_top10)
        pygame.draw.rect(pantalla, (PURPLE), boton_salir)
        
        pantalla.blit(icono, DIMENSION_ICONO)
        
        # dimension para texto titulo
        dimension_texto_x = centro_pantalla((ANCHO,ALTO), texto.get_size())
        dimension_texto_y = 17
        pantalla.blit(texto, (dimension_texto_x, dimension_texto_y))
        
        # dimension para texto boton cantidad de puntos
        dimension_texto_boton_top10_x = centro_pantalla((ANCHO, ALTO),texto_boton_cantidad_de_puntos.get_size())
        dimension_texto_boton_top10_y = 300
        pantalla.blit(texto_boton_cantidad_de_puntos, (dimension_texto_boton_top10_x, dimension_texto_boton_top10_y))
        
        # dimension para texto boton salir
        dimension_salir_x = centro_pantalla((ANCHO, ALTO), texto_boton_salir.get_size())
        dimension_salir_y = 530
        pantalla.blit(texto_boton_salir, (dimension_salir_x, dimension_salir_y))
        
        
        pygame.display.flip()
    