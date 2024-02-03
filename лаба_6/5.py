"""
5. Поменять местами элементы с характеристиками по варианту (минимальный и максимальный.
Функциями min() и max() для поиска элементов не пользоваться).
"""

arr = list(map(int, input("Введите список чисел: ").split()))

max_index = min_index = 0  # Переменные для индексов максимального и минимального элементов

# Алгоритм нахождения минимального и максимального элемента
for i in range(1, len(arr)):
    if arr[i] > arr[max_index]:
        max_index = i
    if arr[i] < arr[min_index]:
        min_index = i

# Замена значений
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print("Измененный список: ", end="")
for item_arr in arr:
    print(item_arr, end=" ")
