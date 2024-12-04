import pygame
from funciones_principal import *
from colores import *
from fuentes import *
from constantes import *
from pantalla_juego import *
from config_cantidad import *
from pantalla_config import *
from pantalla_ranking import *
from funciones_ranking import *
from pantalla_estadist import *
from pantalla_puntos import *

pygame.init()


cantidad_de_vidas_int = 3 # cantidad de vidas por defecto
tiempo_por_pregunta = 10  # Tiempo por defecto en segundos


pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Preguntados") # nombre del juego
icono = pygame.image.load("icono.png") # path de la imagen
icono = pygame.transform.scale(icono, (360, 180)) # redimensiono la imagen
pygame.display.set_icon(icono) # icono del juego

texto = fuente_titulo.render("PREGUNTADOS", True, PURPLE)
texto_boton_jugar = fuente_boton.render("Jugar", True, WHITE)
texto_boton_ranking = fuente_boton.render("Ranking", True, WHITE)
texto_boton_estadisticas = fuente_boton.render("Estadisticas", True, WHITE)
texto_boton_configuracion = fuente_boton.render("Configuracion", True, WHITE)
texto_boton_agregar_pregunta = fuente_boton.render("Agregar preguntas", True, WHITE)
texto_boton_salir = fuente_boton.render("Salir", True, WHITE)

# botones                 #izq #alto #der #bajo
boton_jugar = pygame.Rect(190, 250, 410, 50)
boton_ranking = pygame.Rect(190, 320, 410, 50)
boton_estadisticas = pygame.Rect(190, 390, 410, 50)
boton_configuracion = pygame.Rect(190, 460, 410, 50)
boton_agregar_pregunta = pygame.Rect(190, 530, 410, 50)
boton_salir = pygame.Rect(640, 18, 100, 50)


bandera = True

while bandera:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_posicion = pygame.mouse.get_pos()
            if boton_jugar.collidepoint(mouse_posicion):
                jugar(tiempo_por_pregunta, cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil, cantidad_de_vidas_int)
            if boton_ranking.collidepoint(mouse_posicion):
                pantalla_ranking()
            if boton_estadisticas.collidepoint(mouse_posicion):
                pantalla_estadisticas()
            if boton_configuracion.collidepoint(mouse_posicion):
                tiempo_por_pregunta, cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil, cantidad_de_vidas_int = pantalla_configuracion_menu(tiempo_por_pregunta, cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil, cantidad_de_vidas_int)
            if boton_salir.collidepoint(mouse_posicion):
                bandera = False # cambia la bandera para salir
    

    
    # rellenar pantalla con un color
    pantalla.fill(ORANGE)
    pantalla.blit(icono, DIMENSION_ICONO)
    
    # dibujar el boton
    pygame.draw.rect(pantalla, (PURPLE), boton_jugar)
    pygame.draw.rect(pantalla, (PURPLE), boton_ranking)
    pygame.draw.rect(pantalla, (PURPLE), boton_estadisticas)
    pygame.draw.rect(pantalla, (PURPLE), boton_configuracion)
    pygame.draw.rect(pantalla, (PURPLE), boton_agregar_pregunta)
    pygame.draw.rect(pantalla, (PURPLE), boton_salir)
    
    # pantalla.blit(icono, DIMENSION_ICONO)
    
    # dimension para texto titulo
    dimension_texto_x = centro_pantalla((ANCHO,ALTO), texto.get_size())
    dimension_texto_y = 17
    pantalla.blit(texto, (dimension_texto_x, dimension_texto_y))
    
    # dimension para texto boton jugar
    dimension_jugar_x = centro_pantalla((ANCHO, ALTO), texto_boton_jugar.get_size())
    dimension_jugar_y = 250
    pantalla.blit(texto_boton_jugar, (dimension_jugar_x, dimension_jugar_y))
    
    # dimension para texto boton ranking
    dimension_ranking_x = centro_pantalla((ANCHO, ALTO), texto_boton_ranking.get_size())
    dimension_ranking_y = 320
    pantalla.blit(texto_boton_ranking, (dimension_ranking_x, dimension_ranking_y))
    
    # dimension para texto boton estadisticas
    dimension_estadisticas_x = centro_pantalla((ANCHO, ALTO), texto_boton_estadisticas.get_size())
    dimension_estadisticas_y = 390
    pantalla.blit(texto_boton_estadisticas, (dimension_estadisticas_x, dimension_estadisticas_y))
    
    # dimension para texto boton configuracion
    dimension_configuracion_x = centro_pantalla((ANCHO, ALTO), texto_boton_configuracion.get_size())
    dimension_configuracion_y = 460
    pantalla.blit(texto_boton_configuracion, (dimension_configuracion_x, dimension_configuracion_y))
    
    # dimension para texto boton configuracion
    dimension_agregar_pregunta_x = centro_pantalla((ANCHO, ALTO), texto_boton_agregar_pregunta.get_size())
    dimension_agregar_pregunta_y = 530
    pantalla.blit(texto_boton_agregar_pregunta, (dimension_agregar_pregunta_x, dimension_agregar_pregunta_y))
    
    # dimension para texto boton salir
    dimension_salir_x = 650 #centro_pantalla((ANCHO, ALTO), texto_boton_salir.get_size())
    dimension_salir_y = 18
    pantalla.blit(texto_boton_salir, (dimension_salir_x, dimension_salir_y))
    
    
    pygame.display.flip()
    pygame.display.update()

    
    


pygame.quit()
            