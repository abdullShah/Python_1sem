# Преобразование во float
def new_float(x):
    x = str(x)

    # Удаление незначащих пробелов
    x = x.strip()

    # Пустая строка
    if len(x) == 0:
        return False, x, 'Введена пустая строка!'

    # Строка с пробелами внутри
    if len(x.replace(' ', '')) != len(x):
        return False, x, 'Присутствуют пробелы между символами!'

    # Неарифметические символы
    if not (all(i in '0123456789+-.e ' for i in x)):
        return False, x, 'Присутствуют неарифметические символы!'

    # Большое количество e
    if x.count('e') > 1:
        return False, x, "Большое количество элемента 'e'!"

    # Проверка строки на e
    if x == 'e':
        return False, x, 'Строка не может состоять только из e!'

    # Много точек
    if x.count('.') > 1:
        return False, x, 'В строке много разделителей в виде точки!'

    # Проверка строки на точку
    if x == '.':
        return False, x, 'Строка не может состоять только из точки!'

    # Проверка строки на знаки
    if x == '-' or x == '+':
        return False, x, 'Строка не может состоять только из аримфтических операторов!'

    # Проверка на количество знаков
    if x.count('+') + x.count('-') >= 3:
        return False, x, 'Большое количество арифметических знаков!'

    # Число с e
    if x.count('e') == 1:
        ind_e = x.index('e')

        # Проверка на положение e
        if ind_e == 0 or ind_e == len(x) - 1:
            return False, x, "Неправильная запись числа с 'e'!"

        # Общая проверка на минус
        if x[-1] == '-' or x[ind_e - 1] == '-':
            return False, x, 'Знак минуса расположен в неподходящем месте!'

        # Частная проверка на минус
        if x.count('-') == 1:
            if not (x[0] == '-' or x[ind_e + 1] == '-'):
                return False, x, 'Знак минуса расположен в неподходящем месте!'

        # Частная проверка на минус
        if x.count('-') == 2:
            if not (x[0] == '-' and x[ind_e + 1] == '-'):
                return False, x, 'Знак минуса расположен в неподходящем месте!'

        # Много минусов
        if x.count('-') > 2:
            return False, x, 'В строке много знаков минуса!'

        # Положение точек
        if x.count('.') == 1:
            if x[0] == '.' or x.index('.') > ind_e:
                return False, x, 'Неправильное расположение точки!'

        # Общая проверка на плюс
        if x[-1] == '+' or x[ind_e - 1] == '+':
            return False, x, 'Знак плюса расположен в неподходящем месте!'

        # Частная проверка на плюсы
        if x.count('+') == 1:
            if not (x[0] == '+' or x[ind_e + 1] == '+'):
                return False, x, 'Знак плюса расположен в неподходящем месте!'

        # Частная проверка на плюсы
        if x.count('+') == 2:
            if not (x[0] == '+' and x[ind_e + 1] == '+'):
                return False, x, 'Знак плюса расположен в неподходящем месте!'

        # Много плюсов
        if x.count('+') > 2:
            return False, x, 'В строке много знаков плюса!'

    # Число без e
    if x.count('e') == 0:
        # Проверка на минус
        if x.count('-') == 1 and x[0] != '-':
            return False, x, 'Неверное расположение минуса!'

        # Много минусов
        if x.count('-') > 1:
            return False, x, 'В строке много знаков минуса!'

        # Проверка на плюс
        if x.count('+') == 1 and x[0] != '+':
            return False, x, 'Неверное расположение плюса!'

        # Много плюсов
        if x.count('+') > 1:  # Проверка на плюс
            return False, x, 'В строке много знаков плюса!'

        # Проверка на точку
        if x.count('.') == 1 and x[-1] == '.':
            return False, x, 'Неверное расположение точки!'

    return True, float(x), ''


# Преобразование во int
def new_int(x):
    x = str(x)

    # Удаление незначащих пробелов
    x = x.strip()

    # Пустая строка
    if len(x) == 0:
        return False, x, 'Введена пустая строка!'

    # Строка с пробелами внутри
    if len(x.replace(' ', '')) != len(x):
        return False, x, 'Присутствуют пробелы между символами!'

    # Неарифметические символы
    if not (all(i in '0123456789+- ' for i in x)):
        return False, x, 'Присутствуют неарифметические символы!'

    # Проверка строки на знаки
    if x == '-' or x == '+':
        return False, x, 'Строка не может состоять только из аримфтических операторов!'

    # Проверка на количество знаков
    if x.count('+') + x.count('-') >= 2:
        return False, x, 'Большое количество арифметических знаков!'

    # Проверка на минус
    if x.count('-') == 1 and x[0] != '-':
        return False, x, 'Неверное расположение минуса!'

    # Много минусов
    if x.count('-') > 1:
        return False, x, 'В строке много знаков минуса!'

    # Проверка на плюс
    if x.count('+') == 1 and x[0] != '+':
        return False, x, 'Неверное расположение плюса!'

    # Много плюсов
    if x.count('+') > 1:  # Проверка на плюс
        return False, x, 'В строке много знаков плюса!'

    return True, int(x), ''


# Ввод концов отрезка
def input_ends():
    arr_input = input("Введите начало и конец отрезка через пробел: ").split()
    while len(arr_input) != 2:
        print("Должно быть введено 2 элемента! Повторите попытку")
        arr_input = input("Введите начало и конец отрезка через пробел: ").split()

    a, b = arr_input

    ok_a, a, err_a = new_float(a)
    ok_b, b, err_b = new_float(b)
    while not ok_a or not ok_b:
        if not ok_a and not ok_b:
            print(err_a, err_b, "Повторите попытку")
        elif not ok_a:
            print(err_a, "Повторите попытку")
        else:
            print(err_b, "Повторите попытку")

        arr_input = input("Введите начало и конец отрезка через пробел: ").split()
        while len(arr_input) != 2:
            print("Должно быть введено 2 элемента! Повторите попытку")
            arr_input = input("Введите начало и конец отрезка через пробел: ").split()

        a, b = arr_input

        ok_a, a, err_a = new_float(a)
        ok_b, b, err_b = new_float(b)

    # while a >= b:
    #     print("Конец меньше или равен началу отрезка! Повторите попытку")
    # a, b = input_ends()

    return a, b


# Ввод числа разбиений
def input_partitions():
    N = input(f"Введите количество участков разбиения: ")
    ok, N, err_n1 = new_int(N)
    while not ok:
        print(err_n1, "Повторите попытку")
        N = input(f"Введите количество участков разбиения: ")
        ok, N, err_n1 = new_int(N)

    return N


# Вывод таблицы вида метод-разбиение
def print_table_partition(arr):
    width = 40
    for i in range(len(arr)):
        if arr[i] is None:
            arr[i] = 'Нет значения'
        else:
            arr[i] = float(f'{arr[i]:.5g}')
    print()
    print('Таблица вида метод-разбиение')
    print(f"{'':^{width}}{'N1':^{width}}{'N2':^{width}}")
    print(f"{'Метод сред. прям.':^{width}}{arr[0]:^{width}}{arr[1]:^{width}}")
    print(f"{'Метод параболы':^{width}}{arr[2]:^{width}}{arr[3]:^{width}}")
    print()


# Подсчет абсолютной погрешности
def calc_absolut_values(val, arr):
    absolut_values = []
    for i in range(len(arr)):
        if arr[i] is None:
            absolut_values.append("—")
        else:
            absolut_values.append(float(f'{abs(val - arr[i]):.5g}'))
    return absolut_values


# Подсчет относительной погрешности
def calc_relative_values(val, arr, absolut_values):
    relative_values = []
    for i in range(len(arr)):
        if val == 0:
            relative_values.append('Деление на ноль!')
        elif arr[i] is None:
            relative_values.append("—")
        else:
            relative_values.append(float(f'{abs(absolut_values[i] / val) * 100:.5g}'))

    return relative_values


# Вывод таблицы вида метод-погрешность
def print_table_accuracy(val, arr):
    width = 40

    absolut_values = calc_absolut_values(val, arr.copy())
    relative_values = calc_relative_values(val, arr.copy(), absolut_values.copy())

    print()
    print('Таблица вида метод-погрешность')
    print(f"{'':^{width}}{'Абсолютная погрешность':^{width}}{'Относительная погрешность, %':^{width}}")
    print(f"{'Метод сред. прям. для N1':^{width}}{absolut_values[0]:^{width}}{relative_values[0]:^{width}}")
    print(f"{'Метод сред. прям. для N2':^{width}}{absolut_values[1]:^{width}}{relative_values[1]:^{width}}")
    print(f"{'Метод параболы для N1':^{width}}{absolut_values[2]:^{width}}{relative_values[2]:^{width}}")
    print(f"{'Метод параболы для N2':^{width}}{absolut_values[3]:^{width}}{relative_values[3]:^{width}}")
    print()

    return absolut_values


# Определение неточного метода
def find_inaccurate_method(absolut_values):
    methods = [
        'метод сред. прям. для N1',
        'метод сред. прям. для N2',
        'метод параболы для N1',
        'метод параболы для N2'
    ]

    for i in range(len(absolut_values)):
        if absolut_values[i] == "—":
            absolut_values[i] = float("-inf")

    less_inaccurate_value = max(absolut_values)
    less_inaccurate_method = methods[absolut_values.index(less_inaccurate_value)]
    print()
    print('Самый неточный', less_inaccurate_method)
    print()
    return less_inaccurate_method, less_inaccurate_value


def find_current_method(absolut_arr):
    for i in range(len(absolut_arr)):
        if absolut_arr[i] == "—":
            absolut_arr[i] = float("inf")

    rectangle_method_vals = absolut_arr[:2]
    parabola_method_vals = absolut_arr[2:]
    rectangle_method_vals_min = min(rectangle_method_vals)
    parabola_method_vals_min = min(parabola_method_vals)

    if rectangle_method_vals_min > parabola_method_vals_min:
        print('Самый неточный', 'метод сред. прям.')
        return rectangle_method_vals_min, 'метод сред. прям.'

    print('Самый неточный', 'метод параболы')
    return parabola_method_vals_min, 'метод параболы'



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


# Ввод точности
def input_eps():
    eps = input('Введите точность: ')
    ok, eps, err_eps = new_float(eps)
    while not ok:
        print(err_eps, "Повторите попытку")
        eps = input_eps()
        ok, eps, err_eps = new_float(eps)

    while eps <= 0:
        print("Точность не может быть отрицательным! Повторите попытку")
        eps = input_eps()

    return eps


# Вычисление количество участков разбиения
def calc_partition_sections(method, eps, a, b, f, correct_value):
    print('Точное значение интеграла на отрезке:', f'{correct_value:.5g}')

    if 'метод сред. прям.' in method:
        # Методом сред. прям.
        func_method = rectangle_method
        step = 1
        N = 1
    else:
        # Методом параболы
        func_method = parabola_method
        step = 2
        N = 2

    while abs(func_method(f, a, b, N) - func_method(f, a, b, N * 2)) >= eps:
        N += step

    print(f"Для необходимой точности необходимо {N} итераций")


