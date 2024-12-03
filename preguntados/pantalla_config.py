
import pygame
from funciones_principal import *
from colores import *
from fuentes import *
from constantes import *
from config_cantidad import *



def pantalla_configuracion_menu(tiempo_por_pregunta, cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil, cantidad_de_vidas_int):
    pygame.init()
    
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Preguntados - Configuraciones") # nombre del juego
    icono = pygame.image.load("icono.png") # path de la imagen
    icono = pygame.transform.scale(icono, (350, 200)) # redimensiono la imagen
    pygame.display.set_icon(icono) # icono del juego
    
    texto = fuente_titulo.render("CONFIGURACIONES", True, PURPLE)
    texto_boton_cantidad_de_puntos = fuente_boton.render("cantidad de puntos", True, WHITE)
    texto_boton_cantidad_de_vidas = fuente_boton.render("cantidad de vidas", True, WHITE)
    texto_boton_cantidad_de_tiempo = fuente_boton.render("cantidad de tiempo", True, WHITE)
    texto_boton_salir = fuente_boton.render("Salir", True, WHITE)
    
    
    # botones
    boton_cantidad_de_puntos = pygame.Rect(200, 300, 390, 50)
    boton_cantidad_de_vidas = pygame.Rect(200, 380, 390, 50)
    boton_cantidad_de_tiempo = pygame.Rect(200, 460, 390, 50)
    boton_salir = pygame.Rect(200, 530, 390, 50)
    
    
    bandera = True

    while bandera:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_posicion = pygame.mouse.get_pos()
                if boton_cantidad_de_puntos.collidepoint(mouse_posicion):
                    cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil = pantalla_menu_configuracion_puntos(cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil)
                if boton_cantidad_de_vidas.collidepoint(mouse_posicion):
                    cantidad_de_vidas_int = pantalla_configuracion_vidas(pantalla, fuente_boton, cantidad_de_vidas_int)
                if boton_cantidad_de_tiempo.collidepoint(mouse_posicion):
                    tiempo_por_pregunta = pantalla_configuracion_tiempo(pantalla, fuente_boton, tiempo_por_pregunta)
                if boton_salir.collidepoint(mouse_posicion):
                    bandera = False
    
        
        # rellenar pantalla con un color
        pantalla.fill(PURPLE)
        
        # dibujar el boton
        pygame.draw.rect(pantalla, (ORANGE), boton_cantidad_de_puntos)
        pygame.draw.rect(pantalla, (ORANGE), boton_cantidad_de_vidas)
        pygame.draw.rect(pantalla, (ORANGE), boton_cantidad_de_tiempo)
        pygame.draw.rect(pantalla, (ORANGE), boton_salir)
        
        pantalla.blit(icono, DIMENSION_ICONO)
        
        # dimension para texto titulo
        dimension_texto_x = centro_pantalla((ANCHO,ALTO), texto.get_size())
        dimension_texto_y = 17
        pantalla.blit(texto, (dimension_texto_x, dimension_texto_y))
        
        # dimension para texto boton cantidad de puntos
        dimension_texto_boton_cantidad_de_puntos_x = centro_pantalla((ANCHO, ALTO),texto_boton_cantidad_de_puntos.get_size())
        dimension_texto_boton_cantidad_de_puntos_y = 300
        pantalla.blit(texto_boton_cantidad_de_puntos, (dimension_texto_boton_cantidad_de_puntos_x, dimension_texto_boton_cantidad_de_puntos_y))
        
        # dimension para texto boton cantidad de vidas
        dimension_cantidad_de_vidas_x = centro_pantalla((ANCHO, ALTO), texto_boton_cantidad_de_vidas.get_size())
        dimension_cantidad_de_vidas_y = 380
        pantalla.blit(texto_boton_cantidad_de_vidas, (dimension_cantidad_de_vidas_x, dimension_cantidad_de_vidas_y))
        
        # dimension para texto boton cantidad de tiempo
        dimension_cantidad_de_tiempo_x = centro_pantalla((ANCHO, ALTO), texto_boton_cantidad_de_tiempo.get_size())
        dimension_cantidad_de_tiempo_y = 460
        pantalla.blit(texto_boton_cantidad_de_tiempo, (dimension_cantidad_de_tiempo_x, dimension_cantidad_de_tiempo_y))
        
        # dimension para texto boton salir
        dimension_salir_x = centro_pantalla((ANCHO, ALTO), texto_boton_salir.get_size())
        dimension_salir_y = 530
        pantalla.blit(texto_boton_salir, (dimension_salir_x, dimension_salir_y))
        
        pygame.display.flip()
    
    return tiempo_por_pregunta, cantidad_de_puntos_facil, cantidad_de_puntos_intermedio, cantidad_de_puntos_dificil, cantidad_de_vidas_int