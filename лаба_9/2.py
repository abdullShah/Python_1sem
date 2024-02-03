"""
Суровцев Денис ИУ7-14Б
Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
вводить. Транспонирование не применять.
"""

n = int(input("Введите положительный размер квадратной матрицы: "))

while n <= 0:
    print('Введено неположительное число! Повторите попытку')
    n = int(input("Введите положительный размер квадратной матрицы: "))

matrix = []  # Переменная для матрицы
print("Введите целочисленные элементы строки матрицы через пробел: ")
for i in range(n):
    temp_arr = list(map(int, input().split()))
    while len(temp_arr) != n:
        print(f"Было введено {len(temp_arr)} элементов! Необходимо вводить {n} элементов")
        print("Введите заново данную сточку")
        temp_arr = list(map(int, input().split()))
    matrix.append(temp_arr)

print("Исходная матрица:")
for i in range(n):
    for j in range(n):
        print(f'{matrix[i][j]:^7}', end="")
    print()

# Алгоритм поворота на 90 градусов по часовой стрелке
for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[n - j - 1][i]
        matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
        matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
        matrix[j][n - i - 1] = temp

print("Промежуточная матрица:")
for i in range(n):
    for j in range(n):
        print(f'{matrix[i][j]:^7}', end="")
    print()

# Алгоритм поворота на 90 градусов против часовой стрелке
for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][n - i - 1]
        matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
        matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
        matrix[n - j - 1][i] = temp

print("Итоговая матрица:")
for i in range(n):
    for j in range(n):
        print(f'{matrix[i][j]:^7}', end="")
    print()
