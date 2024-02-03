# Сортировка основана на идее, что сравниваются два соседних элемента
# И в случае неправильного порядка, элемента меняются местами
# В ходе таких манипуляций наибольший элемент всплывает в конец списка
# Затем мы проходим еще раз только до "всплывших" элементов
# Худший случай О(n^2)
# В среднем О(n^2)
# Лучший - О(n)
def tuple_sort(arr):
    alf = ['R', 'G', 'B', 'Y', 'W', 'P']
    for k in range(len(arr) - 1, 0, -1):
        for i in range(0, k):
            left_item = alf.index(arr[i][0])
            right_item = alf.index(arr[i + 1][0])
            if left_item > right_item:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            elif left_item == right_item:
                if arr[i][1] > arr[i + 1][1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def input_arr():
    n = int(input("Введите количество элементов: "))
    arr = []
    print("Введите элементы: ")
    for _ in range(n):
        t = tuple(input().split())
        arr.append(t)

    return arr


def print_arr(arr):
    print()
    print("Измененный массив:")
    for item1, item2 in arr:
        print(item1, item2)
