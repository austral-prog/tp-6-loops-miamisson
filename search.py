# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    if target in lst:
        for i in range(0, len(lst)):
            if lst[i] == target:
                return i
    else: return -1

# print(index_of("Blue", ["Red", "Green"]))

def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """
    if target in lst[start:]:
        for i in range(start, len(lst)):
            if lst[i] == target:
                return i

    else: return -1

# print(index_of_by_index("Black", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"], 4))

def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    if "" in lst:
        for i in range(0, len(lst)):
            if lst[i] == "":
                return i

    else: return -1

# print(index_of_empty(["Red", "Green", "", "", "Pink"]))