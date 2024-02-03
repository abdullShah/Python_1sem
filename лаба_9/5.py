"""
Суровцев Денис ИУ7-14Б
Дана матрица символов. Заменить в ней все гласные английские буквы на
точки. Напечатать матрицу до и после преобразования
"""

n, m = map(int, input("Введите положительные числа количества строк и столбцов через пробел: ").split())

while n <= 0 or m <= 0:
    print('Введено неположительное число! Повторите попытку')
    n, m = map(int, input("Введите положительные числа количества строк и столбцов через пробел: ").split())

matrix = []  # Переменная для матрицы
print("Введите целочисленные элементы строки матрицы через пробел: ")
for i in range(n):
    temp_arr = input().split()
    while len(temp_arr) != m:
        print(f"Было введено {len(temp_arr)} элементов! Необходимо вводить {m} элементов")
        print("Введите заново данную сточку")
        temp_arr = input().split()
    matrix.append(temp_arr)

old_matrix = [row[:] for row in matrix]  # Копирование исходной матрицы
letters = "aoeiuyAOEIUY"  # Все гласные английские буквы

for i in range(n):
    row = matrix[i]  # Строка матрицы
    for j in range(m):
        el = list(row[j])  # Элемент строки матрицы
        for q in range(len(el)):
            if el[q] in letters:  # Перебор элемента строки матрицы
                el[q] = "."  # Замена гласной буквы на строку
        matrix[i][j] = "".join(el)  # Замена старого элемента на измененное

print('Матрица до преобразований')
for i in range(n):
    for j in range(m):
        print(f'{old_matrix[i][j]:^7}', end="")
    print()

print('Матрица после преобразований')
for i in range(n):
    for j in range(m):
        print(f'{matrix[i][j]:^7}', end="")
    print()
