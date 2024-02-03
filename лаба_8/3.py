"""
Абдуллаев Шахмар ИУ7-14Б
Найти столбец, имеющий определённое свойство - наибольшее количество простых чисел.
"""

n, m = map(int, input("Введите положительные числа количества строк и столбцов через пробел: ").split())

while n <= 0 or m <= 0:
    print('Введено неположительное число! Повторите попытку')
    n, m = map(int, input("Введите положительные числа количества строк и столбцов через пробел: ").split())

len_resheto = 1  # Переменная для нахождения оптимальной длины Решето Эратосфена

matrix = []  # Переменная для матрицы
print("Введите целочисленные элементы строки матрицы через пробел: ")
for z in range(n):
    now_arr = list(map(int, input().split()))
    for el in now_arr:
        if len_resheto < el:
            len_resheto = el
    matrix.append(now_arr)


# Нахождение Решето Эратосфена
is_prime = [True] * (len_resheto + 1)
d = 2
while d * d <= len_resheto:
    if is_prime[d]:
        for i in range(d ** 2, len_resheto + 1, d):
            is_prime[i] = False
    d += 1


ind_max_prime = 0  # Переменная для индекса столбца с наибольшим количество простых чисел
val_max_prime = 0  # Переменная для значения наибольшего количество простых чисел
for j in range(m):  # Перебираем столбцы
    cnt_prime = 0  # Переменная для количества простых чисел в столбце
    for i in range(n):  # Перебираем элементы в столбце
        element = matrix[i][j]
        if element > 1 and is_prime[element]:  # Проверка на простоту
            cnt_prime += 1
    if val_max_prime < cnt_prime:  # Проверка на максимальность
        val_max_prime = cnt_prime
        ind_max_prime = j


print(f'Наибольшее количество простых чисел в столбце под индексом {ind_max_prime}: {val_max_prime}')
print('Столбец: ')
for q in range(n):
    print(f'{matrix[q][ind_max_prime]:^7}')
