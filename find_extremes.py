# Replace the "ANSWER HERE" for your answer

def find_min(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el menor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_min([3, 1, 7, 2]) -> 1
    Ejemplo: find_min([5, 5, 5]) -> 5
    Ejemplo: find_min([-3, -1, -7]) -> -7
    """
    num_min = numbers[0]
    for i in range(len(numbers)):
        if num_min >= numbers[i]:
            num_min = numbers[i]
    return num_min
# print(find_min([-3, -1, -7]))


def find_max(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el mayor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_max([3, 1, 7, 2]) -> 7
    Ejemplo: find_max([5, 5, 5]) -> 5
    Ejemplo: find_max([-3, -1, -7]) -> -1
    """
    num_max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] >= num_max:
            num_max = numbers[i]
    return num_max
# print(find_max([3, 1, 7, 2]))


def count_negatives(numbers):
    """
    Dada una lista de numeros, retorna la cantidad de numeros negativos.
    Si la lista esta vacia, retorna 0.

    Ejemplo: count_negatives([3, -1, -7, 2]) -> 2
    Ejemplo: count_negatives([1, 2, 3]) -> 0
    Ejemplo: count_negatives([-1, -2, -3]) -> 3
    """
    if numbers == "":
        return []
    else: 
        contador_negativos = 0
        for i in range(len(numbers)):
            if numbers[i] < 0:
                contador_negativos = contador_negativos + 1
        return contador_negativos
    
# print(count_negatives([]))
