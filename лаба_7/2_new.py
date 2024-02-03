"""
После каждого элемента целочисленного списка, имеющего свойство - элементы, кратные трём - добавить
его удвоенное значение, без использования вложенных циклов.
Без insert append срезов
1 3 9 5 3 4
"""

arr = list(map(int, input("Введите элементы списка: ").split()))
if len(arr) == 0:
    print("Введен пустой список!")
    arr = list(map(int, input().split("Введите элементы списка: ")))

cnt_krat_3 = 0
for i in range(len(arr)):
    if abs(arr[i]) % 3 == 0:
        cnt_krat_3 += 1

old_len = len(arr)
arr += [None] * cnt_krat_3

k = 1
for i in range(old_len - 1, -1, -1):
    print('Было ', arr)
    if abs(arr[i]) % 3 != 0:
        arr[-k] = arr[i]
        k += 1
    else:
        arr[-k] = arr[i] * 2
        k += 1
        arr[-k] = arr[i]
        k += 1
    print('Стало ', arr)
    print()

# print(arr)

# Вывод элементов
print("Измененный список: ", end="")
for w in range(len(arr)):
    print(arr[w], end=" ")
