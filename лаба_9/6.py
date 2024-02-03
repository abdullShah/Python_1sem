"""
Суровцев Денис ИУ7-14Б
Сформировать матрицу C путём построчного перемножения матриц A и B
одинаковой размерности (элементы в i-й строке матрицы A умножаются на
соответствующие элементы в i-й строке матрицы B), потом сложить все
элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
A, B, C и массив V
"""

n, m = map(int, input("Введите положительные числа количества строк и "
                      "столбцов матрицы A или B через пробел: ").split())

while n <= 0 or m <= 0:
    print('Введено неположительное число! Повторите попытку')
    n, m = map(int, input("Введите положительные числа количества строк и "
                          "столбцов матрицы A или B через пробел: ").split())

A = []  # Переменная для матрицы
print("Зададим матрицу A")
print("Введите целочисленные элементы строки матрицы через пробел: ")
for i in range(n):
    temp_arr = list(map(int, input().split()))
    while len(temp_arr) != m:
        print(f"Было введено {len(temp_arr)} элементов! Необходимо вводить {m} элементов")
        print("Введите заново данную сточку")
        temp_arr = list(map(int, input().split()))
    A.append(temp_arr)

B = []  # Переменная для матрицы
print("Зададим матрицу B")
print("Введите целочисленные элементы строки матрицы через пробел: ")
for i in range(n):
    temp_arr = list(map(int, input().split()))
    while len(temp_arr) != m:
        print(f"Было введено {len(temp_arr)} элементов! Необходимо вводить {m} элементов")
        print("Введите заново данную сточку")
        temp_arr = list(map(int, input().split()))
    B.append(temp_arr)

C = []  # Переменная для матрицы
for i in range(n):
    row = []  # Строка матрицы
    for j in range(m):
        row.append(A[i][j] * B[i][j])  # Добавление перемножения соответствующих элементов матриц
    C.append(row)  # Добавление строки

print(C)

V = []  # Сумма столбцов матрицы С
for k in range(m):
    column = []
    for i in range(n):
        column.append(C[i][k])
    sum_column = sum(column)  # Сумма столбца
    V.append(sum_column)  # Добавление суммы столбца

print('Матрица A')
for i in range(n):
    for j in range(m):
        print(f'{A[i][j]:^7}', end="")
    print()

print('Матрица B')
for i in range(n):
    for j in range(m):
        print(f'{B[i][j]:^7}', end="")
    print()

print('Матрица C')
for i in range(n):
    for j in range(m):
        print(f'{C[i][j]:^7}', end="")
    print()

print("Список V:", end=" ")
for i in range(len(V)):
    print(V[i], end=" ")
