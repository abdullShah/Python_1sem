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

# # Алгоритм поворота на 90 градусов по часовой стрелке
for i in range(0, n // 2, 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[n - j - 1][i]
        matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
        matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
        matrix[j][n - i - 1] = temp

# # Алгоритм поворота на 90 градусов против часовой стрелке
# for i in range(n // 2):
#     for j in range(i, n - i - 1):
#         temp = matrix[i][j]
#         matrix[i][j] = matrix[j][n - i - 1]
#         matrix[j][n - i - 1] = matrix[n - i - 1][n - j - 1]
#         matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
#         matrix[n - j - 1][i] = temp

print("Итоговая матрица:")
for i in range(n):
    for j in range(n):
        print(f'{matrix[i][j]:^7}', end="")
    print()

ind_col = -1
val_col = 0

for q in range(n):
    col_this_sum = 0
    for i in range(q, q + 1):
        for j in range(n):
            elem = matrix[j][i]
            col_this_sum += elem

    cnt_for_this_q = 0

    for i in range(n):
        if i == q:
            continue
        col_sum = 0
        for j in range(n):
            elem = matrix[j][i]
            col_sum += elem
        if col_sum == col_this_sum:
            cnt_for_this_q += 1

    if val_col < cnt_for_this_q:
        val_col = cnt_for_this_q
        ind_col = q

if ind_col == -1:
    print("Не найдено")
else:
    print("Номер столбца:", ind_col + 1)
