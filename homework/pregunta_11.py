"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()
        
    # Observación
    # for fila in data[:5]:  
    #     print(fila)

    # Limpieza
    data = [linea.split() for linea in data]
    
    # Pregunta_11
    letrasValor = [(fila[3].split(','), int(fila[1])) for fila in data]

    respuesta = {}

    for tupla in letrasValor:
        letras, valor = tupla
        print(letras)
        for letra in letras:
            if letra not in respuesta:
                respuesta[letra] = valor
            else:
                respuesta[letra] += valor
    
    respuesta = dict(sorted(respuesta.items()))

    return respuesta

