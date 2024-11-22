"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()

    # Observación
    # for fila in data[:5]:  
    #     print(fila)

    # Limpieza
    data = [linea.split() for linea in data]
    
    # Pregunta_05
    letrasCantidad = [(fila[0], int(fila[1])) for fila in data]
    
    dicAux = {}
    for tupla in letrasCantidad:
        if tupla[0] in dicAux:
            maximo = max(dicAux[tupla[0]][0], tupla[1])
            minimo = min(dicAux[tupla[0]][1], tupla[1])
            dicAux[tupla[0]] = [maximo, minimo]
        else:
            dicAux[tupla[0]] = [tupla[1], tupla[1]]
    
    # resultado = list(dicAux.items())
    # resultado = [(letra, *numeros) for letra, numeros in resultado]

    resultado = [(letra, maxMin[0], maxMin[1]) for letra, maxMin in dicAux.items()]

    resultado.sort()

    # print(resultado)
    return resultado

# pregunta_05()
