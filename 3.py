# Ввод пользователем одномерного массива чисел
numbers = input("Введите одномерный массив чисел, разделенных пробелом: ")
numbers = numbers.split()
numbers = [float(num) for num in numbers]

# Пересохранение массива в обратном порядке
numbers_reversed = numbers[::-1]

# Вычисление среднего арифметического всех элементов
average = sum(numbers) / len(numbers)

# Вычитание среднего арифметического из каждого элемента
result = [num - average for num in numbers_reversed]

# Вывод результата в консоль
print(result)