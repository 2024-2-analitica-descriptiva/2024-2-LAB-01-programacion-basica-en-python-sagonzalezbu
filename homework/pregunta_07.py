"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()
    # Observación
    # for fila in data[:5]:  
    #     print(fila)

    # Limpieza
    data = [linea.split() for linea in data]
    
    # Pregunta_07
    letraValor = [(fila[0], fila[1]) for fila in data]

    dicAux = {}

    for tupla in letraValor:
        letra = tupla[0]
        valor = int(tupla[1])
        if valor not in dicAux:
            dicAux[valor] = [letra]
        else:
            dicAux[valor].append(letra)

    resultado = [(clave, valor) for clave, valor in dicAux.items()]
    resultado.sort()
    
    return resultado

