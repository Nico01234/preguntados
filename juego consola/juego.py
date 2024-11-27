from funciones_preguntas import *
from config import *
from cantidad import *
from funciones_generales import *

def jugar(archivo_preguntas, puntos_respuesta_correcta, cantidad_vidas, cantidad_limite):
    preguntas = cargar_preguntas(archivo_preguntas)
    vidas = cantidad_vidas
    puntaje = 0
    respuestas_correctas = 0
    tiempo_limite = cantidad_limite
    
    
    print("¡Bienvenido al juego de preguntas!")
    nombre = input("Por favor, ingresa tu nombre: ")
    
    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i+1}: {pregunta['pregunta']}")
        for j, opcion in enumerate(pregunta["opciones"], start=1):
            print(f"{j}. {opcion}")
            
        respuesta_usuario = preguntar_con_tiempo("elige una opcion (1-4)", tiempo_limite)
    
        if respuesta_usuario is None or not respuesta_usuario.isdigit():
            print("se acabo el tiempo")
            vidas -= 1
            if vidas == 0:
                print("game over\nvidas = 0")
                break
            continue
        else:
            print("")
        
        respuesta_usuario = int(respuesta_usuario)
        if respuesta_usuario >= 1 and respuesta_usuario <= 4:
            if respuesta_usuario == int(pregunta["respuesta_correcta"]):
                print("CORRECTO")
                puntaje += puntos_respuesta_correcta
                respuesta_usuario += 1
        
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta_correcta']}")
            vidas -= 1

        if vidas == 0:
            print("game over")
            print(f"Vidas: {vidas}")
            print(f"puntaje: {puntaje}")
            print(f"respuestas correctas: {respuestas_correctas}")
            break
        
        else:
            print("Por favor, elige un número entre 1 y 4.")
            
    guardar_puntaje(nombre, puntaje, respuestas_correctas)
    
    jugadores = leer_ranking("ranking.csv")
    
    ranking_top10 = obtener_ranking(jugadores)
    
    print("Top 10")
    for i, (nombre, puntaje, respuestas_correctas) in enumerate(ranking_top10, 1):
        print(f"{i}. {nombre}: {puntaje} puntos, respuestas correctas: {respuestas_correctas}")
