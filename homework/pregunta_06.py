"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()
    # Observación
    # for fila in data[:5]:  
    #     print(fila)

    # Limpieza
    data = [linea.split() for linea in data]
    
    # Pregunta_06
    columna5 = [fila[4].split(",") for fila in data]
    
    dicAux = {}
    for fila in columna5:
        for elemento in fila:

            listAux = elemento.split(":")
            listAux[1] = int(listAux[1])

            if listAux[0] in dicAux:
                maximo = max(dicAux[listAux[0]][1], listAux[1])
                minimo = min(dicAux[listAux[0]][0], listAux[1])
                dicAux[listAux[0]] = [minimo, maximo]
            else:
                dicAux[listAux[0]] = [listAux[1], listAux[1]]

    resultado = [(letra, valor[0], valor[1]) for letra, valor in dicAux.items()]
    resultado.sort()
    
    return resultado


