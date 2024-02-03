'''
Абдуллаев Шахмар ИУ7-14Б

1 1 2 3
5 6 7 8
1 2 3 4
6 7 8 9
'''
from math import sqrt


n = int(input("Введите размерность матрицы: "))

while n <= 0:
    print('Введено неположительное число! Повторите попытку')
    n = int(input("Введите размерность матрицы: "))

matrix = []
print("Введите целочисленные элементы строки матрицы через пробел: ")
for i in range(n):
    temp_arr = list(map(int, input().split()))
    while len(temp_arr) != n:
        print(f"Было введено {len(temp_arr)} элементов! Необходимо вводить {n} элемента")
        print("Введите заново данную строчку")
        temp_arr = list(map(int, input().split()))
    matrix.append(temp_arr)

arr = list(map(int, input('Введите список: ').split()))

# q = 1
# right_n = True
# while right_n:
#     if len(arr) >= q * q:
#         q += 1
#     else:
#         q -= 1
#         right_n = False


q = int(sqrt(len(arr)))

arr_iter = 0
for i in range(n - q, n):
    for j in range(0, q):
        matrix[i][j] = arr[arr_iter]
        arr_iter += 1
        # print(matrix[i][j])


print("Итоговая матрица:")
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(f'{matrix[i][j]:^7}', end="")
    print()

