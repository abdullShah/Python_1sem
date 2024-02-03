"""
Абдуллаев Шахмар ИУ7-14Б
Переставить местами столбцы с максимальной и минимальной суммой элементов.
"""

n, m = map(int, input("Введите положительные числа количества строк и столбцов через пробел: ").split())

while n <= 0 or m <= 0:
    print('Введено неположительное число! Повторите попытку')
    n, m = map(int, input("Введите положительные числа количества строк и столбцов через пробел: ").split())


matrix = []  # Переменная для матрицы
print("Введите целочисленные элементы строки матрицы через пробел: ")
for _ in range(n):
    matrix.append(
        list(map(int, input().split()))
    )


max_sum_ind = 0  # Переменная для индекса столбца с наибольшей суммой
max_sum_val = 0  # Переменная для наибольшей суммы
min_sum_ind = 0  # Переменная для индекса столбца с наименьшей суммой
min_sum_val = 0  # Переменная для наименьшей суммы

for j in range(m):  # Перебираем столбцы
    now_sum = 0  # Переменная для суммы
    for i in range(n):  # Перебираем элементы в столбце:
        element = matrix[i][j]
        now_sum += element

    if j == 0:  # Условие для заполнения начальными данными переменные
        # Задаем переменные начальными данными
        max_sum_val = now_sum
        max_sum_ind = j
        min_sum_val = now_sum
        min_sum_ind = j
        continue

    if max_sum_val < now_sum:  # Проверка на максимальность
        max_sum_val = now_sum
        max_sum_ind = j
    if min_sum_val > now_sum:  # Проверка на минимальность
        min_sum_val = now_sum
        min_sum_ind = j


# Меняем местами столбцы
for row in matrix:
    row[max_sum_ind], row[min_sum_ind] = row[min_sum_ind], row[max_sum_ind]


print("Измененная матрица:")
for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:^7}', end="")
    print()
