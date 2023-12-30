import random


# n - количество строк матрицы
# m - количество строк матрицы
# Элементы матрицы генерируются в диапазоне [an;ak]
# Функция генерации целочисленной матрицы
def Gen_Matrix_Int(n, m, an, ak):
    A = []
    for i in range(0, n):
        x = [random.randint(an, ak) for j in range(0,m)]
        A.append(x)
    return A


# Функция печати целочисленной матрицы (n*m)
def Print_Matrix_Int (n,Z):
    for i in range(0,n):
        for x in Z[i]:
            print ('{0:4} '.format(x), end=' ')
        print('\n')


# Функция печати целочисленного массива
def Print_Mas_Int(Z):
    for x in Z:
        print(x, end=' ')
    print()

