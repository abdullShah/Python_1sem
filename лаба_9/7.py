"""
Суровцев Денис ИУ7-14Б
Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
индексов начинается с 1).
"""

x, y, z = map(int, input("Введите размерность трёхмерного массива: ").split())

while x <= 0 or y <= 0 or z <= 0:
    print('Введено неположительное число! Повторите попытку')
    x, y, z = map(int, input("Введите размерность трёхмерного массива").split())

A = []  # Исходный массив

for _ in range(x):
    matrix = []  # Переменная для матрицы
    print("Введите целочисленные элементы строки матрицы через пробел: ")
    for i in range(y):
        temp_arr = list(map(int, input().split()))
        while len(temp_arr) != z:
            print(f"Было введено {len(temp_arr)} элементов! Необходимо вводить {z} элемента")
            print("Введите заново данную сточку")
            temp_arr = list(map(int, input().split()))
        matrix.append(temp_arr)
    A.append(matrix)

ind = int(input("Введите i-й срез: "))
while not (1 <= ind <= y):
    print(f"Нумерация индексов идет с 1 до {y}! Повторите попытку")
    ind = int(input("Введите i-й срез: "))

ind -= 1  # Перевод из номера строки в индекс строки
slice_matrix = []  # Матрица слайса

for i in range(x):
    matrix = A[i]  # Выделяем матрицу
    for j in range(y):
        row = matrix[ind]  # Выделяем строку по индексу
        slice_matrix.append(row)  # Добавляем в матрицу слайсов строку
        break

print("Срез")
for i in range(x):
    for j in range(z):
        print(f'{slice_matrix[i][j]:^7}', end="")
    print()

"""
3 4 2

3 6
8 3
9 10
5 1

9 7
8 4
7 5
3 5

3 8
3 2
7 10
5 8
"""