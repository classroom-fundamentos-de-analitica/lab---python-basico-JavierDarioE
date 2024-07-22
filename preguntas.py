"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from operator import itemgetter


def read_file(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


def return_as_list(content):
    content_as_list = [line.replace("\n", "") for line in content]
    content_as_list = [line.split("\t") for line in content_as_list]
    return content_as_list


def sort_by_index(sequence, index):
    f = itemgetter(index)
    sequence = sorted(sequence, key=f)
    return sequence


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    path = "./data.csv"
    with open(path, mode='r') as file:
        line = file.readline()
        result = int(line.split("\t")[1])
        while line:
            line = file.readline()
            if line != "":
                result += int(line.split("\t")[1])
            else:
                break
    return result


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    path = "./data.csv"
    with open(path, mode='r') as file:
        characters_list = []
        file_line = file.readline()
        while file_line != "":
            characters_list.append(file_line[0])
            file_line = file.readline()
    characters = list(set(characters_list))
    characters.sort()
    count_list = [(letter, characters_list.count(letter)) for letter in characters]
    return count_list


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [[line[0], int(line[1])] for line in content]
    sum_of_values = {}
    for key, value in content:
        sum_of_values[key] = sum_of_values.get(key, 0) + value
    content = list(sum_of_values.items())
    return sort_by_index(content, 0)


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    path = "./data.csv"
    dates = []
    with open(path, mode='r') as file:
        line = file.readline()
        while line != "":
            date = line.split("\t")[2]
            dates.append(date)
            line = file.readline()
    months = [date.split("-")[1] for date in dates]
    months_unique = list(set(months))
    months_unique.sort()
    month_count = [(month, months.count(month)) for month in months_unique]
    return month_count


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [[line[0], int(line[1])] for line in content]
    min_max = {}
    for line in content:
        if line[0] in min_max:
            if min_max[line[0]][0] < line[1]:
                min_max[line[0]][0] = line[1]
            elif min_max[line[0]][1] > line[1]:
                min_max[line[0]][1] = line[1]
        else:
            min_max[line[0]] = [line[1], line[1]]
    min_max_list = [(key, value[0], value[1]) for key, value in min_max.items()]
    min_max_list = sort_by_index(min_max_list, 0)
    return min_max_list


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [items for line in content for items in line[4].split(",")]
    content = [item.split(":") for item in content]
    counter = {}
    for key, value in content:
        if key in counter:
            if int(value) < counter[key][0]:
                counter[key][0] = int(value)
            elif int(value) > counter[key][1]:
                counter[key][1] = int(value)
        else:
            counter[key] = [int(value), int(value)]
    counter = [(key, value[0], value[1]) for key, value in counter.items()]
    return sort_by_index(counter, 0)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [[line[0], int(line[1])] for line in content]
    counter = {}
    for value, key in content:
        if key in counter:
            counter[key].append(value)
        else:
            counter[key] = [value]

    return sort_by_index(list(counter.items()), 0)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [[line[0], int(line[1])] for line in content]
    counter = {}
    for value, key in content:
        if key in counter:
            if value not in counter[key]:
                counter[key].append(value)
        else:
            counter[key] = [value]
    counter = {key: sorted(value) for key, value in counter.items()}
    return sort_by_index(list(counter.items()), 0)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [line[4] for line in content]
    content = [line.split(",") for line in content]
    content = [element.split(":")[0] for line in content for element in line]
    counter = {}
    for key in content:
        counter[key] = counter.get(key, 0) + 1
    return counter


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [(line[0], line[3], line[4]) for line in content]
    content = [(letter, len(letters.split(",")), len(dictionary.split(","))) for letter, letters, dictionary in content]
    return content


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [(line[1], line[3]) for line in content]
    content = [(letter, (int(line[0]))) for line in content for letter in line[1].split(",")]
    counter = {}
    for key, value in content:
        counter[key] = counter.get(key, 0) + value
    return counter


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    path = "./data.csv"
    content = return_as_list(read_file(path))
    content = [[line[0], line[4]] for line in content]
    content = [[letter, int(element.split(":")[1])] for [letter, values] in content for element in values.split(",")]
    counter = {}
    for key, value in content:
        counter[key] = counter.get(key, 0) + value
    return counter
