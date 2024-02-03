# Метод сред. прям.
def rectangle_method(f, a, b, n):
    h = (b - a) / n  # Определение шага разбиения
    s = 0  # Расчет подынтегральной суммы
    for i in range(n):
        x = (a + (i + 0.5) * h)
        s += f(x)
    return h * s


# Метод параболы
def parabola_method(f, a, b, n):
    if n % 2 != 0:
        return None
    h = (b - a) / n
    x = [a + i * h for i in range(1, n)]  # Иксы в диапазоне (a, b) с шагом h
    s1 = 0  # Сумма элементов с нечетными индексами
    s2 = 0  # Сумма элементов с четными индексами
    for i in range(len(x)):
        if i % 2:
            s1 += f(x[i])
        else:
            s2 += f(x[i])

    return h / 3 * (f(a) + 2 * s1 + 4 * s2 + f(b))


# Метод трапеций
def trap_method(f, a, b, n):
    h = (b - a) / n
    # Заполним значения х
    x = [a + i * h for i in range(n + 1)]
    # Расчет подынтегральной суммы
    s = 0
    for i in range(n):
        s += h * (f(x[i]) + f(x[i + 1])) / 2
    return s


# Метод левых прям.
def left_rectangle_method(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + i * h
        s += f(x)
    return h * s


# Метод правых прям.
def right_rectangle_method(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + (i + 1) * h  # изменение: использование правой границы интервала
        s += f(x)
    return h * s


# Метод 3/8
def method_3_8(f, a, b):
    h = (b - a) / 3
    sum_of_ends = f(a) + f(b)
    sum_of_others = 3 * (f(a + h) + f(a + 2 * h))
    return (3 * h / 8) * (sum_of_ends + sum_of_others)


def method_3_8(f, a, b, n):
    if n % 3 != 0:  # Проверка, что количество шагов кратно 3
        return None
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]  # Иксы в диапазоне [a, b] с шагом h
    s1 = 0  # Сумма элементов, кратных 3
    s2 = 0  # Сумма элементов соответствует модифицированным коэффициентам
    for i in range(1, n):  # итерация по иксам с шагом 1
        if i % 3 == 0:
            s1 += f(x[i])  # добавить к сумме элементов, кратных 3
        else:
            s2 += f(x[i])  # добавить к сумме остальных элементов

    return (3 / 8) * h * (f(a) + f(b) + 2 * s2 + 3 * s1)  # возврат значения интеграла методом 3/8
