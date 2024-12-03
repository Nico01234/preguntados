
import pygame
from funciones_principal import *
from colores import *
from fuentes import *
from constantes import *
from estadisticas import *

porcentaje = leer_archivo("estadisticas_globales.csv", "porcentaje_aciertos", "Porcentaje de Aciertos")
fallos = leer_archivo("estadisticas_globales.csv", "porcentaje_aciertos", "Fallos")
veces_preguntadas = leer_archivo("estadisticas_globales.csv", "porcentaje_aciertos", "Veces Preguntada")
aciertos = leer_archivo("estadisticas_globales.csv", "porcentaje_aciertos", "Aciertos")

def pantalla_estadisticas():
    
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Preguntados") # nombre del juego
    icono = pygame.image.load("icono.png") # path de la imagen
    icono = pygame.transform.scale(icono, (350, 200)) # redimensiono la imagen
    pygame.display.set_icon(icono) # icono del juego
    
    texto = fuente_titulo.render("ESTADISTICAS", True, PURPLE)
    texto_boton_porcentaje_aciertos = fuente_boton.render("Porcentaje de aciertos", True, WHITE)
    texto_boton_fallos = fuente_boton.render("Fallos", True, WHITE)
    texto_boton_aciertos = fuente_boton.render("Cantidad de aciertos", True, WHITE)
    texto_boton_veces_preguntadas = fuente_boton.render("Veces preguntadas", True, WHITE)
    texto_boton_salir = fuente_boton.render("Salir", True, WHITE)
    
    
    # botones
    boton_porcentaje_aciertos = pygame.Rect(190, 250, 410, 50)
    boton_fallos = pygame.Rect(190, 320, 410, 50)
    boton_aciertos = pygame.Rect(190, 390, 410, 50)
    boton_veces_preguntadas = pygame.Rect(190, 460, 410, 50)
    boton_salir = pygame.Rect(190, 530, 410, 50)
    
    
    bandera = True
    bandera_mostrar_porcentaje_aciertos = False
    bandera_mostrar_fallos = False
    bandera_mostrar_veces_preguntadas = False
    bandera_mostrar_aciertos = False
    
    while bandera:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_posicion = pygame.mouse.get_pos()
                if boton_porcentaje_aciertos.collidepoint(mouse_posicion):
                    bandera_mostrar_porcentaje_aciertos = True
                if boton_fallos.collidepoint(mouse_posicion):
                    bandera_mostrar_fallos = True
                if boton_aciertos.collidepoint(mouse_posicion):
                    bandera_mostrar_aciertos = True
                if boton_veces_preguntadas.collidepoint(mouse_posicion):
                    bandera_mostrar_veces_preguntadas = True
                if boton_salir.collidepoint(mouse_posicion):
                    bandera = False # cambia la bandera para salir
        
        if bandera_mostrar_porcentaje_aciertos:
            mostrar_porcentaje_aciertos(pantalla, porcentaje, fuente_texto, ANCHO, ALTO)
            pygame.display.flip()
            continue
        
        if bandera_mostrar_fallos:
            mostrar_fallos(pantalla, fallos, fuente_texto, ANCHO, ALTO)
            pygame.display.flip()
            continue
        
        if bandera_mostrar_veces_preguntadas:
            mostrar_veces_preguntadas(pantalla, veces_preguntadas, fuente_texto, ANCHO, ALTO)
            pygame.display.flip()
            continue
        
        if bandera_mostrar_aciertos:
            mostrar_veces_preguntadas(pantalla, aciertos, fuente_texto, ANCHO, ALTO)
            pygame.display.flip()
            continue
        
        # rellenar pantalla con un color
        pantalla.fill(PURPLE)
        
        
        # dibujar el boton
        pygame.draw.rect(pantalla, (ORANGE), boton_porcentaje_aciertos)
        pygame.draw.rect(pantalla, (ORANGE), boton_fallos)
        pygame.draw.rect(pantalla, (ORANGE), boton_aciertos)
        pygame.draw.rect(pantalla, (ORANGE), boton_veces_preguntadas)
        pygame.draw.rect(pantalla, (ORANGE), boton_salir)
        
        pantalla.blit(icono, DIMENSION_ICONO)
        
        # dimension para texto titulo
        dimension_texto_x = centro_pantalla((ANCHO,ALTO), texto.get_size())
        dimension_texto_y = 17
        pantalla.blit(texto, (dimension_texto_x, dimension_texto_y))
        
        # dimension para texto boton jugar
        dimension_porcentaje_aciertos_x = centro_pantalla((ANCHO, ALTO), texto_boton_porcentaje_aciertos.get_size())
        dimension_porcentaje_aciertos_y = 250
        pantalla.blit(texto_boton_porcentaje_aciertos, (dimension_porcentaje_aciertos_x, dimension_porcentaje_aciertos_y))
        
        # dimension para texto boton ranking
        dimension_fallos_x = centro_pantalla((ANCHO, ALTO), texto_boton_fallos.get_size())
        dimension_fallos_y = 320
        pantalla.blit(texto_boton_fallos, (dimension_fallos_x, dimension_fallos_y))
        
        # dimension para texto boton estadisticas
        dimension_aciertos_x = centro_pantalla((ANCHO, ALTO), texto_boton_aciertos.get_size())
        dimension_aciertos_y = 390
        pantalla.blit(texto_boton_aciertos, (dimension_aciertos_x, dimension_aciertos_y))
        
        # dimension para texto boton configuracion
        dimension_veces_preguntadas_x = centro_pantalla((ANCHO, ALTO), texto_boton_veces_preguntadas.get_size())
        dimension_veces_preguntadas_y = 460
        pantalla.blit(texto_boton_veces_preguntadas, (dimension_veces_preguntadas_x, dimension_veces_preguntadas_y))
        
        # dimension para texto boton salir
        dimension_salir_x = centro_pantalla((ANCHO, ALTO), texto_boton_salir.get_size())
        dimension_salir_y = 530
        pantalla.blit(texto_boton_salir, (dimension_salir_x, dimension_salir_y))
        
        
        pygame.display.flip()
        
        
    
    