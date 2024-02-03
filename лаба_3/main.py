"""
Абдуллаев Шахмар ИУ7-14Б
Представлена программа, которая по введенным целочисленным
координатам трех точек на плоскости вычисляет длины сторон
образованного треугольника и длину высоты, проведенной из
наименьшего угла. Также определяет, является ли треугольник равнобедренным.

Затем вводятся координаты точки. Программа определяет, находится ли
точка внутри треугольника. Если да, то находит расстояние от точки
до ближайшей стороны треугольника.
"""

from math import sqrt, pow, acos, sin  # Импорт функций квадратного корня и возведения в степень

eps = 1e-9

# Блок ввода
x1, y1, = map(int, input("Введите координаты x и y точки A через пробел: ").split())  # Точка A
x2, y2, = map(int, input("Введите координаты x и y точки B через пробел: ").split())  # Точка B
x3, y3, = map(int, input("Введите координаты x и y точки C через пробел: ").split())  # Точка C

# Чтобы проверить, являются ли три точки вырожденными (коллинеарными), можно использовать следующий метод:
# Вычисляем значение выражения определитель следующей матрицы: | x1 y1 1 |
#                                                              | x2 y2 1 |
#                                                              | x3 y3 1 |
# Если определитель равна нулю, то три точки являются вырожденными (коллинеарными).
# Если определитель не равна нулю, то точки не являются вырожденными и образуют невырожденный треугольник.
if abs((x1 * y2 + x2 * y3 + x3 * y1) - (x3 * y2 + x1 * y3 + x2 * y1)) < eps:
    print("Треугольник вырожденный!")
elif (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x3 == x2 and y3 == y2):  # Совпадение вершин треугольника
    print("Вершины совпадают!")
else:
    # Блок вычислений и вывода
    # Формула стороны по координатам: a = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    ab = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))  # Длина стороны AB
    bc = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))  # Длина стороны BC
    ac = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))  # Длина стороны AC
    max_section = ab if ab > bc and ab > ac else (bc if bc > ac else ac)  # Наибольшая длина треугольника
    min_section = ab if ab < bc and ab < ac else (bc if bc < ac else ac)  # Наименьшая длина треугольника
    mid_section = ab + bc + ac - max_section - min_section  # Оставшаяся (средняя) длина треугольника
    # Формула угла по 3-трем сторонам: cos(a) = (b^2 + c^2 - a^2) / (2bc)
    angle_max_section = acos(
        (pow(min_section, 2) + pow(mid_section, 2) - pow(max_section, 2)) / (2 * min_section * mid_section)
    )
    # Формула угла из прямоугольного треугольника: h = sin(a) * c
    height_small_angle = sin(angle_max_section) * mid_section
    is_isosceles = (abs(ab - bc) < eps or abs(bc - ac) < eps or abs(ab - ac) < eps)  # *Проверка на равнобедренность треугольника

    # Блок вывода
    print(f'Длины сторон образованного треугольника: {ab:.6g}, {bc:.6g}, {ac:.6g}')
    print(f'Длина высоты, проведенной из наименьшего угла: {height_small_angle:.6g}')
    if is_isosceles:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник неравнобедренный")

    # Блок ввода
    x4, y4, = map(int, input("Введите координаты x и y новой точки через пробел: ").split())  # Точка Q

    # Блок вычислений
    # Полупериметр вычисляется по формуле: p = (a+b+c)/2
    # По формуле Герона площадь равна: S = sqrt(p(p-a)(p-b)(p-c))
    S_original_per = (ab + bc + ac) / 2  # Полупериметр исходного треугольника
    # Площадь исходного треугольника
    S_original = sqrt(S_original_per * (S_original_per - ab) * (S_original_per - bc) * (S_original_per - ac))
    aq = sqrt(pow(x4 - x1, 2) + pow(y4 - y1, 2))  # Длина стороны AQ
    bq = sqrt(pow(x4 - x2, 2) + pow(y4 - y2, 2))  # Длина стороны BQ
    cq = sqrt(pow(x4 - x3, 2) + pow(y4 - y3, 2))  # Длина стороны CQ

    S_1_per = (aq + bq + ab) / 2  # Полупериметр треугольника точки со 1-ой стороной треугольника
    # Площадь треугольника точки со 1-ой стороной треугольника
    S_1 = sqrt(S_1_per * (S_1_per - aq) * (S_1_per - bq) * (S_1_per - ab))
    S_2_per = (ac + aq + cq) / 2  # Полупериметр треугольника точки со 2-ой стороной треугольника
    # Площадь треугольника точки со 2-ой стороной треугольника
    S_2 = sqrt(S_2_per * (S_2_per - ac) * (S_2_per - aq) * (S_2_per - cq))
    S_3_per = (bq + cq + bc) / 2  # Полупериметр треугольника точки со 3-ой стороной треугольника
    # Площадь треугольника точки со 3-ой стороной треугольника
    S_3 = sqrt(S_3_per * (S_3_per - bq) * (S_3_per - cq) * (S_3_per - bc))

    # *Проверка на равенство сумм площадей частей и исходного треугольника
    is_inside = abs((S_1 + S_2 + S_3) - S_original) < eps
    min_p = max_section  # Минимальное расстояние до стороны. В виде заглушки стоит наибольшая сторона
    if is_inside:
        # Формула расстояния до стороны находилась, как высота в треугольнике: p = h = 2S/a
        p1 = 2 * S_1 / ab
        p2 = 2 * S_2 / ac
        p3 = 2 * S_3 / bc
        min_p = p1 if p1 < p2 and p1 < p3 else (p2 if p2 < p3 else p3)

    # Блок вывода
    if is_inside:
        print("Точка находится внутри треугольника")
        print(f"Расстояние от точки до ближайшей стороны треугольника: {min_p:.6g}")
    else:
        print("Точка не находится внутри треугольника")
