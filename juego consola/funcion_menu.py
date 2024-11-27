from pantalla_principal import *
from colores import *
from fuentes import *
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# def mostrar_menu():
#     pantalla.fill(BLANCO)
#     print("MENU PRINCIPAL")
#     print("1. jugar")
#     print("2. ranking")
#     print("3. estadisticas")
#     print("4. configuracion")
    
# def mostrar_submenu():
#     print("CONFIGURACION")
#     print("1. modificar puntaje")
#     print("2. modificar cantidad de vidas")
#     print("3. modificar cantidad de tiempo")
#     print("4. salir")
    
def mostrar_texto(texto, x, y, color=NEGRO, fuente=fuente_opciones):
    render = fuente.render(texto, True, color)
    pantalla.blit(render, (x, y))

def mostrar_menu():
    pantalla.fill(BLANCO)
    mostrar_texto("Menú Principal", 300, 50, NEGRO, fuente_titulo)
    mostrar_texto("1. Jugar", 300, 150)
    mostrar_texto("2. Ranking", 300, 200)
    mostrar_texto("3. Estadisticas", 300, 250)
    mostrar_texto("4. Configuración", 300, 300)
    mostrar_texto("5. Salir", 300, 350)
    pygame.display.flip()

def mostrar_submenu():
    pantalla.fill(BLANCO)
    mostrar_texto("Configuración", 300, 50, NEGRO, fuente_titulo)
    mostrar_texto("1. Modificar puntos por respuesta correcta", 150, 150)
    mostrar_texto("2. Modificar cantidad de vidas", 150, 200)
    mostrar_texto("3. Modificar tiempo por pregunta", 150, 250)
    mostrar_texto("4. Volver al menú principal", 150, 300)
    pygame.display.flip()

    
