"""
Абдуллаев Шахмар ИУ7-14Б
Удалить все элементы целочисленного списка, имеющие свойство - нулевые элементы - за один цикл.
Без del pop remove срезов
"""

arr = list(map(int, input("Введите элементы списка: ").split()))
if len(arr) == 0:
    print("Введен пустой список!")
    arr = list(map(int, input().split("Введите элементы списка: ")))

# Алгоритм удаления элементов по условию со сдвигом
k = 0  # Указатель места
for i in range(len(arr)):
    if arr[i] == 0:
        k += 1
    else:
        arr[i - k] = arr[i]
    # print(arr)


# Вывод элементов
print("Измененный список: ", end="")
for q in range(len(arr) - k):
    print(arr[q], end=" ")
