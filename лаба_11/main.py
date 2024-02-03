"""
Абдуллаев Шахмар ИУ7-14Б
Метод сортировки пирамидальная сортировка
"""
from module import *

# Ввод массива
test_arr = input_arr()

# Вывод до изменений
print_arr(test_arr, "Исходный")

# Сортировка массива
heap_sort(test_arr)

# Вывод после изменений
print_arr(test_arr, "Отсортированный")

# Ввод размерностей случайных списков
arr_dimensions = input_dimensions()

# Вывод размерностей
print_dimensions(arr_dimensions)

# Получение результатов исследований
matrix_values = get_matrix_values(arr_dimensions)

# Вывод таблицы
print_table(matrix_values, arr_dimensions)
