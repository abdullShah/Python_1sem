"""
4. Найти наиболее длинную непрерывную убывающей последовательности целых чётных чисел
"""
arr = list(map(int, input("Введите список чисел: ").split()))
# Добавление "пустого/не нужного" элемента, что рассмотреть ситуацию,
# когда у нас элемент подходящего ряда является последним элементом
# Например, 1 6 2 4 2 0
arr.append(1)

arr_chet = []  # Список для убывающей последовательности целых чётных чисел
max_len = 0  # Переменная дял максимальной длины

max_len_arr = []

for i in range(1, len(arr)):
    # Добавление первого элемента
    if abs(arr[i - 1]) % 2 == 0 and len(arr_chet) == 0:
        arr_chet.append(arr[i - 1])
    # Проверка, что соседние элементы образуют убывающую четную последовательность
    if abs(arr[i]) % 2 == 0 and abs(arr[i - 1]) % 2 == 0 and arr[i - 1] > arr[i]:
        arr_chet.append(arr[i])
    else:  # Проверка на максимальность и обнуление
        if max_len < len(arr_chet):
            max_len = len(arr_chet)
            max_len_arr = arr_chet.copy()
        arr_chet.clear()

print(f"Наибольшая длина последовательности : {max_len}")
print("Последовательность: ", end="")
for item_arr in max_len_arr:
    print(item_arr, end=" ")
