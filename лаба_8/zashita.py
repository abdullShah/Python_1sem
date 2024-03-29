"""
1
1

2
1 2
3 4

3
1 2 3
4 5 6
7 8 9

4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

Абдуллаев Шахмар ИУ7-14Б
4. Вводится квадратная целочисленная матрица. Матрица разбивается главной и побочной диагоналями на 4 сектора
(треугольника), отразить левый и правый сектор (не включая диагонали) относительно
вертикали проведенной через центр. Вывести итоговую матрицу. Транспонировать матрицу нельзя.
"""

n = int(input("Введите положительный размер квадратной матрицы: "))

while n <= 0:
    print('Введено неположительное число! Повторите попытку')
    n = int(input("Введите положительный размер квадратной матрицы: "))

matrix = []

for i in range(n):
    temp_arr = list(map(int, input().split()))
    while len(temp_arr) != n:
        print(f"Было введено {len(temp_arr)} элементов! Необходимо вводить {n} элемента")
        print("Введите заново данную сточку")
        temp_arr = list(map(int, input().split()))
    matrix.append(temp_arr)


for i in range(1, n - 1):
    for j in range(min(i, n - i - 1)):
        matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


print("Измененная матрица:")
for i in range(n):
    for j in range(n):
        print(f'{matrix[i][j]:^7}', end="")
    print()
