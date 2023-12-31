def get_perimeter_elements(matrix):
    perimeter_elements = []
    # Получение размеров матрицы
    rows = len(matrix)
    if rows == 0:
        return perimeter_elements
    columns = len(matrix[0])
    # Запись верхней строки
    for i in range(columns):
        perimeter_elements.append(matrix[0][i])
    # Запись правого столбца
    for i in range(1, rows):
        perimeter_elements.append(matrix[i][columns - 1])
    # Запись нижней строки (если есть)
    if rows > 1:
        for i in range(columns - 2, -1, -1):
            perimeter_elements.append(matrix[rows - 1][i])

    # Запись левого столбца (если есть)
    if columns > 1:
        for i in range(rows - 2, 0, -1):
            perimeter_elements.append(matrix[i][0])

    return perimeter_elements


def remove_zeros(array):
    filtered_array = [element for element in array if element != 0]
    return filtered_array


def average_even_elements(array):
    even_elements = [element for element in array if element % 2 == 0]
    if len(even_elements) == 0:
        return 0
    sum_even_elements = sum(even_elements)
    average = sum_even_elements / len(even_elements)
    return average