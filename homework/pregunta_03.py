"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

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
    letrasCantidad = [(fila[0], int(fila[1])) for fila in data]
    
    dicAux = {}

    for tupla in letrasCantidad:
        if tupla[0] in dicAux:
            dicAux[tupla[0]] += tupla[1]
        else:
            dicAux[tupla[0]] = tupla[1]

    resultado = list(dicAux.items())
    resultado.sort(key = lambda x: x[0])
    #registros = sorted(registros, key = lambda x: x[0])
    # print(resultado)
    return resultado

# pregunta_03()