import math


def sqrt_src(t):
    if t >= 0:
        x1 = math.sqrt(t)
        x2 = -math.sqrt(t)
        return [0] if t == 0 else [x1, x2]
    return "Корней нет"


def solve_bi_rect_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        sqrt_discriminant = math.sqrt(discriminant)
        t1 = (-b + sqrt_discriminant) / (2 * a)
        t2 = (-b - sqrt_discriminant) / (2 * a)
        r1 = sqrt_src(t1)
        r2 = sqrt_src(t2)
        rez = []
        if isinstance(r1, list):
            rez += r1
        if isinstance(r2, list):
            rez += r2
        if len(rez) > 0:
            return rez

    elif discriminant == 0:
        t = -b / (2 * a)
        return list(sqrt_src(t))

    return "Действительных корней нет!"


if __name__ == "__main__":
    stop = 'y'
    while stop == 'y':
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))

        solution = solve_bi_rect_equation(a, b, c)

        print("Ответ:")
        if not isinstance(solution, str):
            for i in range(len(solution)):
                print(f'x{i} = {solution[i]}')
        else:
            print(solution)
        stop = ''
        while stop not in ('y', 'n'):
            stop = input("Еще пример? (y/n)...")