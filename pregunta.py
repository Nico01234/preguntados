import pygame
import csv
from colores import *


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Preguntas")


font = pygame.font.Font(None, 36)


preguntas = []


def mostrar_texto(texto, x, y, color=(WHITE), tamano=36):
    """
    Muestra un texto en la pantalla en las coordenadas especificadas.
    """
    texto_renderizado = font.render(texto, True, color)
    screen.blit(texto_renderizado, (x, y))
    
def guardar_pregunta(pregunta,opcion1,opcion2,opcion3,opcion4,respuesta_correcta,dificultad) -> None:
    
    """
    ¿Que hace? : Guarda los datos de la partida en un archivo csv
    
    ¿Que recibe? :
    - 
    
    ¿Que devuelve? : None
    """
    
    
    # Ruta del archivo CSV donde se guardarán los datos
    archivo = 'preguntas.csv'
    
    # Comprobar si el archivo existe, si no, crearlo con los encabezados
    with open(archivo, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([pregunta,opcion1,opcion2,opcion3,opcion4,respuesta_correcta,dificultad])  # Escribir los datos de la partida



def agregar_pregunta():
    """
    Permite al usuario ingresar una pregunta junto con sus opciones de respuesta, la respuesta correcta y la dificultad.
    Las preguntas se guardan en la lista 'preguntas' una vez completadas.
    """
    pregunta = ''
    opciones = []
    respuesta_correcta = ''
    dificultad = ''
    estado = "pregunta"
    input_active = True

    while input_active:
        
        screen.fill((ORANGE))
        mostrar_texto("Ingrese una pregunta y las respuestas:", 20, 20)

        
        if estado == "pregunta":
            mostrar_texto(f"Pregunta: {pregunta}", 20, 100)
            mostrar_texto("Presione ENTER para pasar a las opciones", 20, 150)
        
        elif estado == "opciones":
            mostrar_texto("Ingrese opciones de respuesta (máximo 4):", 20, 100)
            for i, opcion in enumerate(opciones):
                mostrar_texto(f"Opción {i + 1}: {opcion}", 20, 150 + i * 40)
            if len(opciones) < 4:
                mostrar_texto("Presione ENTER para pasar a la respuesta correcta", 20, 350)
            else:
                mostrar_texto("Presione ENTER para pasar a la respuesta correcta (máximo 4 opciones)", 20, 350)
        
        elif estado == "respuesta":
            mostrar_texto(f"Respuesta correcta: {respuesta_correcta}", 20, 100)
            mostrar_texto("Presione ENTER para pasar a la dificultad", 20, 150)
        
        elif estado == "dificultad":
            mostrar_texto(f"Dificultad (opcional): {dificultad}", 20, 100)
            mostrar_texto("Presione ENTER para guardar la pregunta", 20, 150)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    
                    if estado == "pregunta" and pregunta:
                        estado = "opciones"
                    elif estado == "opciones" and len(opciones) == 4:
                        estado = "respuesta"
                    elif estado == "respuesta" and respuesta_correcta:
                        estado = "dificultad"
                    elif estado == "dificultad":
                        preguntas.append({
                            'pregunta': pregunta,
                            'opciones': opciones,
                            'respuesta_correcta': respuesta_correcta,
                            'dificultad': dificultad
                        })
                        
                        guardar_pregunta(
                            pregunta,
                            opciones[0],
                            opciones[1],
                            opciones[2],
                            opciones[3],
                            respuesta_correcta,
                            dificultad
                        )
                        mostrar_texto("Pregunta agregada exitosamente", 20, 400)
                        pygame.display.flip()
                        pygame.time.delay(2000)  
                        input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    
                    if estado == "pregunta":
                        pregunta = pregunta[:-1]
                    elif estado == "opciones" and opciones:
                        opciones[-1] = opciones[-1][:-1]
                    elif estado == "respuesta":
                        respuesta_correcta = respuesta_correcta[:-1]
                    elif estado == "dificultad":
                        dificultad = dificultad[:-1]
                else:
                    
                    if estado == "pregunta":
                        pregunta += event.unicode
                    elif estado == "opciones":
                        if len(opciones) < 4:
                            if len(opciones) == 0 or len(opciones[-1]) > 0:
                                opciones.append(event.unicode)
                            else:
                                opciones[-1] += event.unicode
                    elif estado == "respuesta":
                        respuesta_correcta += event.unicode
                    elif estado == "dificultad":
                        dificultad += event.unicode
