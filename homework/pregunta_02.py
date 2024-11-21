"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()

    # Observación
    # for fila in data[:5]:  
    #     print(fila)

    # Limpieza
    data = [linea.split() for linea in data]

    # Pregunta_02
    letras = [fila[0] for fila in data]

    dicAux = {}
    for letra in letras:
        if letra in dicAux:
            dicAux[letra] += 1
        else:
            dicAux[letra] = 1
    
    resultado = list(dicAux.items())
    resultado.sort(key = lambda x: x[0])
    #registros = sorted(registros, key = lambda x: x[0])

    return resultado
