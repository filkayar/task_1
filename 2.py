import pandas as pd
import matplotlib.pyplot as plt
import math

def func(x):
    a = -7.213
    b = -3.2
    if a * x * x - b <= 0:
        return math.sin(a * x)
    else:
        if math.fabs(a) >= math.pow(x, 3):
            return math.cos(math.fabs(a*a*x/b))
        else:
            return x*x - a*x + b*x*math.log(math.fabs(x-a), math.exp(1))

# Ввод пользователем значений xn, xk, h
xn = float(input("Введите значение xn: "))
xk = float(input("Введите значение xk: "))
h = float(input("Введите значение h: "))

# Генерация списка значений аргумента x
x_values = []
current_x = xn
while current_x <= xk:
    x_values.append(current_x)
    current_x += h

# Расчет списка значений функции t
t_values = [func(x) for x in x_values]

# Печать таблицы значений функции t
table = pd.DataFrame({'x': x_values, 't': t_values})
print(table)

# Конвертация списка в словарь
data_dict = {'x': x_values, 't': t_values}

# Конвертация списка в датафрейм
df = pd.DataFrame(data_dict)

# Построение графика функции t=f(x)
plt.plot(df['x'], df['t'])
plt.xlabel('x')
plt.ylabel('t')
plt.title('График функции t=f(x)')
plt.show()