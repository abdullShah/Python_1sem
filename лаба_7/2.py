"""
Абдуллаев Шахмар ИУ7-14Б
После каждого элемента целочисленного списка, имеющего свойство - элементы, кратные трём - добавить
его удвоенное значение, без использования вложенных циклов.
Без insert append срезов
"""

arr = list(map(int, input("Введите элементы списка: ").split()))
if len(arr) == 0:
    print("Введен пустой список!")
    arr = list(map(int, input().split("Введите элементы списка: ")))

# Алгоритм перестановки элемента на 2 шага вперед, кроме первого
# Это сделано для того, чтобы оставить место для удвоенного значения числа, если тот подходит под условие
old_len = len(arr)
arr += [None] * len(arr)
cnt = 1
for j in range(old_len - 1, 0, -1):
    arr[-2 * cnt] = arr[j]
    arr[j] = None
    cnt += 1

# Алгоритм вставки удвоенного произведения в заготовленные для них места по условию
for q in range(0, len(arr), 2):
    if abs(arr[q]) % 3 == 0:
        arr[q + 1] = arr[q] * 2

# Алгоритм удаления пустых заготовленных мест (реализация первого задания)
k = 0
for j in range(len(arr)):
    if arr[j] is None:
        k += 1
    else:
        arr[j - k] = arr[j]

# Вывод элементов
print("Измененный список: ", end="")
for w in range(len(arr) - k):
    print(arr[w], end=" ")
