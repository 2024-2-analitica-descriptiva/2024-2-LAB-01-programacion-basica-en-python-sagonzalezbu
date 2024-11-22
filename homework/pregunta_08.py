"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

        # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()
    # Observación
    # for fila in data[:5]:  
    #     print(fila)

    # Limpieza
    data = [linea.split() for linea in data]
    
    # Pregunta_08
    letraValor = [(fila[0], fila[1]) for fila in data]

    dicAux = {}

    for tupla in letraValor:
        letra = tupla[0]
        valor = int(tupla[1])
        if valor not in dicAux:
            dicAux[valor] = [letra]
        else:
            if letra not in dicAux[valor]:
                dicAux[valor].append(letra)

    for lista in dicAux.values():
        lista.sort()

    resultado = [(clave, valor) for clave, valor in dicAux.items()]
    resultado.sort()
    
    return resultado

