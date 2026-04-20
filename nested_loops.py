# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    unica_lista = []
    for i in range(len(matrix)):
        for int in range(len(matrix[i])):
            unica_lista.append(matrix[i][int])
    return unica_lista

# print(flatten([[1], [2, 3], [4, 5]]))


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    nueva_lista = []
    
    for i in range(len(matrix)):
        suma = 0
        for int in range(len(matrix[i])):
            suma = suma + matrix[i][int]
        nueva_lista.append(suma)
    return nueva_lista

# print(row_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    num_columnas = len(matrix[0])
    num_filas = len(matrix)
    nueva_lista = []
    for j in range(num_columnas):
        suma = 0
        for i in range(num_filas):
            suma += matrix[i][j]
        nueva_lista.append(suma)

    return nueva_lista

    

print(col_sums([[1, 2, 3], [4, 5, 6]]))

