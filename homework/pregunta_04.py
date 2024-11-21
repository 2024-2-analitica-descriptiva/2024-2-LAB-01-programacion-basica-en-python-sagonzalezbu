"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
        # Carga
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        data = archivo.readlines()

    # Observación
    for fila in data[:5]:  
        print(fila)

    # Limpieza
    data = [linea.split() for linea in data]
    
    #pregunta 4
    columna3 = [fila[2] for fila in data]
    columna3 = list(map(lambda fecha: fecha.split("-"), columna3))
    meses = [fecha[1] for fecha in columna3] 
    
    dicAux = {}
    for mes in meses:
        if mes in dicAux:
            dicAux[mes] += 1
        else:
            dicAux[mes] = 1
    
    resultado = list(dicAux.items())
    resultado.sort(key = lambda x: x[0])
    return resultado

# pregunta_04()