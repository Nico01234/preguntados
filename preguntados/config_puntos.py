import pygame
from colores import *
from fuentes import *
from constantes import *
from funciones_principal import *

def pantalla_puntos_facil(pantalla, fuente, puntos_facil):
    configurando = True
    nuevo_puntos_facil = str(puntos_facil)  # Mostrar el tiempo actual como texto
    
    while configurando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Presionar ENTER para confirmar
                    configurando = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar el último carácter
                    nuevo_puntos_facil = nuevo_puntos_facil[:-1]
                else:
                    nuevo_puntos_facil += evento.unicode  # Añadir carácter

        # Dibujar la pantalla de configuración
        pantalla.fill(FONDO)
        texto_titulo = fuente.render("Configurar puntos de nivel facil:", True, WHITE)
        texto_puntos_facil = fuente.render(nuevo_puntos_facil, True, GREEN)
        texto_instrucciones = fuente.render("Presiona ENTER para guardar.", True, WHITE)
        
        pantalla.blit(texto_titulo, (150, 200))
        pantalla.blit(texto_puntos_facil, (350, 300))
        pantalla.blit(texto_instrucciones, (150, 400))
        pygame.display.flip()
    