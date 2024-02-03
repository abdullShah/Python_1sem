"""
Абдуллаев Шахмар ИУ7-14Б
Вводит отрезок и кол разбиаев
Функция в коде
Интеграл свичаем левыми прям
"""

from module_zach import *
from math import sin, cos


def f(x):
    return sin(x)


def F(x):
    return -cos(x)


a, b = input_ends()
n = input_iter()

integral_val = left_rectangle_method(f, a, b, n)

print_val(integral_val, a, b)

print(F(b) - F(a))
