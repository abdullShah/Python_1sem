"""
Абдуллаев Шахмар ИУ7-14Б
Выполнить транспонирование квадратной матрицы.
"""

n = int(input("Введите положительный размер квадратной матрицы: "))

while n <= 0:
    print('Введено неположительное число! Повторите попытку')
    n = int(input("Введите положительный размер квадратной матрицы: "))

matrix = []  # Переменная для матрицы
print("Введите целочисленные элементы строки матрицы через пробел: ")
for _ in range(n):
    matrix.append(
        list(map(int, input().split()))
    )

for i in range(n - 1):
    level_move = 1  # Переменная для списка вниз по строке и для смещения вправо по столбцам
    for j in range(i + 1, n):
        matrix[i][j], matrix[i + level_move][j - level_move] = matrix[i + level_move][j - level_move], matrix[i][j]
        level_move += 1

print("Измененная матрица:")
for i in range(n):
    for j in range(n):
        print(f'{matrix[i][j]:^7}', end="")
    print()
