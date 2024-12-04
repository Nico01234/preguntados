import pygame
from constantes import *
from fuentes import *
from colores import *
from funciones_principal import *

#-------facil----

def config_puntos_facil(pantalla : any, fuente : any, puntos_facil : int) -> int:
    
    """
    ¿Que hace? : Configura la cantidad de puntos para el nivel facil y lo muestra por pantalla
    
    ¿Que recibe? : 
    - pantalla (any) : Superficie de pantalla
    - fuente (any) : Fuente para el texto en pantalla
    - puntos_facil (int) : Cantidad inicial de puntos para nivel facil
    
    ¿Que devuelve? : 
    - (int) : Cantidad actualizada de puntos para nivel facil
    """
    
    boton_nuevos_punto_facil = pygame.Rect(190, 290, 410, 50)
    
    configurando = True
    nuevo_puntos_facil = str(puntos_facil)  # Mostrar el tiempo actual como texto
    
    while configurando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Presionar ENTER para confirmar
                    if nuevo_puntos_facil == "":
                        nuevo_puntos_facil = 1
                    configurando = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar el último carácter
                    nuevo_puntos_facil = nuevo_puntos_facil[:-1]
                elif evento.unicode.isdigit():
                    nuevo_puntos_facil += evento.unicode
                    
        # Dibujar la pantalla de configuración
        pantalla.fill(ORANGE)
        
        pygame.draw.rect(pantalla, (PURPLE), boton_nuevos_punto_facil)
        
        texto_titulo = fuente.render("Configurar cantidad de puntos facil:", True, WHITE)
        texto_puntos = fuente.render(nuevo_puntos_facil, True, WHITE)
        texto_salir = fuente.render("Presiona ENTER para guardar.", True, WHITE)
        
        
        pantalla.blit(texto_titulo, (180, 200))
        pantalla.blit(texto_puntos, (400, 300))
        pantalla.blit(texto_salir, (200, 550))
        
        pygame.display.flip()
        pygame.display.update()
    
    nuevo_puntos_facil = int(nuevo_puntos_facil)
    return nuevo_puntos_facil


#-----intermedio-----
def config_puntos_intermedio(pantalla : any, fuente : any, puntos_intermedio : int) -> int:
    
    """
    ¿Que hace? : Configura la cantidad de puntos para el nivel intermedio y lo muestra por pantalla
    
    ¿Que recibe? : 
    - pantalla (any) : Superficie de pantalla
    - fuente (any) : Fuente para el texto en pantalla
    - puntos_intermedio (int) : Cantidad inicial de puntos para nivel intermedio
    
    ¿Que devuelve? : 
    - (int) : Cantidad actualizada de puntos para nivel intermedio
    """
    
    boton_nuevos_punto_intermedio = pygame.Rect(190, 290, 410, 50)
    
    configurando = True
    nuevo_puntos_intermedio = str(puntos_intermedio)  # Mostrar el tiempo actual como texto
    
    while configurando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Presionar ENTER para confirmar
                    if nuevo_puntos_intermedio == "":
                        nuevo_puntos_intermedio = 1
                    configurando = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar el último carácter
                    nuevo_puntos_intermedio = nuevo_puntos_intermedio[:-1]
                elif evento.unicode.isdigit():
                    nuevo_puntos_intermedio += evento.unicode
                    
        # Dibujar la pantalla de configuración
        pantalla.fill(ORANGE)
        
        pygame.draw.rect(pantalla, (PURPLE), boton_nuevos_punto_intermedio)
        
        texto_titulo = fuente.render("Configurar cantidad de puntos intermedio:", True, WHITE)
        texto_puntos = fuente.render(nuevo_puntos_intermedio, True, WHITE)
        texto_instrucciones = fuente.render("Presiona ENTER para guardar.", True, WHITE)
        
        pantalla.blit(texto_titulo, (150, 200))
        pantalla.blit(texto_puntos, (350, 300))
        pantalla.blit(texto_instrucciones, (150, 400))
        pygame.display.flip()
        pygame.display.update()
        
    nuevo_puntos_intermedio = int(nuevo_puntos_intermedio)
    return nuevo_puntos_intermedio



#-----dificil-----
def config_puntos_dificil(pantalla : any, fuente : any, puntos_dificil : int) -> int:
    
    """
    ¿Que hace? : Configura la cantidad de puntos para el nivel dificil y lo muestra por pantalla
    
    ¿Que recibe? : 
    - pantalla (any) : Superficie de pantalla
    - fuente (any) : Fuente para el texto en pantalla
    - puntos_dificil (int) : Cantidad inicial de puntos para nivel dificil
    
    ¿Que devuelve? : 
    - (int) : Cantidad actualizada de puntos para nivel dificil
    """
    
    boton_nuevos_punto_dificil = pygame.Rect(190, 290, 410, 50)
    
    configurando = True
    nuevo_puntos_dificil = str(puntos_dificil)  # Mostrar el tiempo actual como texto
    
    while configurando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Presionar ENTER para confirmar
                    if nuevo_puntos_dificil == "":
                        nuevo_puntos_dificil = 1
                    configurando = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar el último carácter
                    nuevo_puntos_dificil = nuevo_puntos_dificil[:-1]
                elif evento.unicode.isdigit():
                    nuevo_puntos_dificil += evento.unicode
                    
        # Dibujar la pantalla de configuración
        pantalla.fill(ORANGE)
        
        pygame.draw.rect(pantalla, (PURPLE), boton_nuevos_punto_dificil)
        
        texto_titulo = fuente.render("Configurar cantidad de puntos dificil:", True, WHITE)
        texto_puntos = fuente.render(nuevo_puntos_dificil, True, WHITE)
        texto_instrucciones = fuente.render("Presiona ENTER para guardar.", True, WHITE)
        
        pantalla.blit(texto_titulo, (150, 200))
        pantalla.blit(texto_puntos, (350, 300))
        pantalla.blit(texto_instrucciones, (150, 400))
        
        pygame.display.flip()
        pygame.display.update()
    nuevo_puntos_dificil = int(nuevo_puntos_dificil)
    return nuevo_puntos_dificil


