"""
1b. Добавить элемент в заданное место списка (по индексу) алгоритмически.
"""
arr = list(map(int, input("Введите список чисел: ").split()))
n = int(input("Введите элемент: "))
i = int(input(f"Введите индекс от 0 до {len(arr)}, на котором будет находиться элемент: "))

while not(0 <= i <= len(arr)):
    print(f"Некорректные данные! Индекс должен быть от 0 до {len(arr)}")
    i = int(input(f"Введите индекс от 0 до {len(arr)}, на котором будет находиться элемент: "))

# Алгоритм добавления элемента
arr.append(None)
for q in range(len(arr) - 1, i, -1):
    arr[q] = arr[q - 1]
arr[i] = n

print("Измененный список: ", end="")
for item_arr in arr:
    print(item_arr, end=" ")



























# if i <= -len(arr):  # Случай, когда индекс выходит за нижний диапазон
#     arr = [n] + arr
# elif i < 0:  # Случай, когда индекс меньше нуля, но в диапазоне
#     arr.reverse()  # Переворачиваем массив
#     i *= -1  # Переводим индекс в положительный диапазон
#     i -= 1
#     # Алгоритм добавления элемента
#     arr.append(None)
#     for q in range(len(arr) - 1, i, -1):
#         arr[q] = arr[q - 1]
#     arr[i] = n
#     arr.reverse()  # Переворачиваем массив обратно
# elif i < len(arr):  # Случай, когда индекс больше нуля, но в диапазоне
#     # Алгоритм добавления элемента
#     arr.append(None)
#     for q in range(len(arr) - 1, i, -1):
#         arr[q] = arr[q - 1]
#     arr[i] = n
# else:  # Случай, индекс выходит за верхний диапазон
#     arr.append(n)

# if i < 0:
#     arr.reverse()
#     arr = arr[0:abs(i)] + [n] + arr[abs(i):]
#     arr.reverse()
# else:
#     arr = arr[0:i] + [n] + arr[i:]

# если нужно, чтобы работал, как insert, нужно удалить 13 строку