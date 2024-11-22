"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()
        
    # Observación
    # for fila in data[:5]:  
    #     print(fila)

    # Limpieza
    data = [linea.split() for linea in data]
    
    # Pregunta_12
    letraValores = [(fila[0], fila[4].split(',')) for fila in data]

    respuesta = {}

    for tupla in letraValores:
        letra, valores = tupla
        for valor in valores:
            valor = int(valor.split(':')[1])
            if letra not in respuesta:
                respuesta[letra] = valor
            else:
                respuesta[letra] += valor
    
    respuesta = dict(sorted(respuesta.items()))
    return respuesta

# pregunta_12()