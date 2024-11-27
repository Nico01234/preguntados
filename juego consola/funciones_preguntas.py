import csv

def cargar_preguntas(archivo):
    preguntas = []
    
    with open(archivo, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for columna in reader:
            datos = {
                "pregunta" : columna["pregunta"],
                "opciones" : (columna["opcion1"], columna["opcion2"], columna["opcion3"], columna["opcion4"]),
                "respuesta_correcta" : columna["respuesta_correcta"]
            }
            preguntas.append(datos)
    
    return preguntas

            
def guardar_puntaje(nombre, puntaje, respuestas_correctas, archivo="ranking.csv"):
    with open(archivo, mode="a", encoding="utf-8") as f:
        f.write(f"{nombre},{puntaje},{respuestas_correctas}\n")


def ordenar_mayor_menor(lista :list) -> list:
    """
    ¿Que hace? = Ordena de mayor a menor el total de lista de una matriz
    ¿Que recibe? 
    -  lista (list) = lista con elementos a sumar
    ¿Que retorna? = (list) lista ordenada de mayor a menor
    """
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return lista



def leer_ranking(nombre_archivo):
    jugadores = []
    with open(nombre_archivo) as archivo:
        reader = csv.reader(archivo)
        for columna in reader:
            nombre = columna[0]
            puntaje = int(columna[1])
            respuestas_correctas = int(columna[2])
            jugadores.append([nombre, puntaje, respuestas_correctas])
    return jugadores

def obtener_ranking(lista):
    puntajes = []
    for jugador in lista:
        puntajes.append(jugador[1])
        
    jugadores_ordenados = ordenar_mayor_menor(puntajes)
    
    ranking_top10 = []
    for puntaje in jugadores_ordenados[:10]:
        for jugador in lista:
            if  jugador[1] == puntaje and (jugador[0], puntaje) not in ranking_top10:
                ranking_top10.append((jugador[0], puntaje, jugador[2]))
                break
    return ranking_top10
            
        
    
def capturar_opcion(minimo, maximo, rectangulos):
    import pygame
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit
            
            if evento.type == pygame.KEYDOWN:
                if pygame.K_1 <= evento.key and pygame.K_9 >= evento.key:
                    opcion = evento.key - pygame.K_0
                    if opcion >= minimo and opcion <= maximo:
                        return opcion
                    
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    pass 
