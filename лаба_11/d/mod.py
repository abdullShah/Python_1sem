# Метод шейкер-сортировки
# Ускоренный метод пузырька. При первом проходе мы сортируем слева направо, при втором - наоборот.
# Сортируем пока мы не пересечемся с двумя метками, которые отвечают за левую и правую границу
# Худший случай О(n^2), лучший - О(n)
def sheiker(arr):
    low, up = 0, len(arr) - 1
    while low < up:
        last = -1
        for i in range(low, up):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last = i
        up = last
        if last == -1:
            break

        last = len(arr)
        for i in range(up - 1, low - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last = i
        low = last + 1
    return arr


# Метод простых вставок
# Есть левая часть, которая условно отсортированная, и в нее мы вставляем с помощью свапов первый элемент
# из неотсортированной части
def simple_insert(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i
        while item < arr[j - 1] and j > 0:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item
    return arr


# Метод вставок с бинарным поиском
# Это метода вставок, только вставляем в отсортированную часть с помощью бин поиска
# # Примерно O(n log n)
def bin_search(arr, val, start, end):
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start


def bin_insert(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = bin_search(arr, item, 0, i)
        arr = arr[:j] + [item] + arr[j:i] + arr[i + 1:]
    return arr


# Метод Шелла
# Метод основан на методе ставок: числа делятся на группки и сортируются внутри вставками, и так пока шаг не станет 1
# Примерно O(n log n)
def med_shell(arr):
    h = len(arr) // 2
    while h > 0:
        for i in range(1, len(arr), h):
            item = arr[i]
            j = i
            while j > 0 and item < arr[j - 1]:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = item
        h //= 2

    return arr


# Метод сортировки "пузырьком" с флагом
# Наибольший элемент всплывает в конец списка
# Худший случай, среднем О(n^2), лучший - О(n)
def bubble_flag(arr):
    for k in range(len(arr) - 1, 0, -1):
        is_swap = True
        for i in range(0, k):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_swap = False
        if is_swap:
            break

    return arr


# Метод простого выбора
# Выбирается минимальный (или максимальный элемент) и он ставиться на соотв. место
# Для больших массивов долго будет работать
# Сложность: худший случай O(n^2)
def simple_selection(arr):
    for k in range(0, len(arr)):
        ind_min = arr[k:].index(min(arr[k:])) + k
        arr[ind_min], arr[k] = arr[k], arr[ind_min]
    return arr


# Метод "расчёски"
# Это метод Шелла только шаг деления не на 2, а на 1,247
# Сложность: O(n^2)
def hairbrush(arr):
    const = 1.247
    h = int(len(arr) // const)
    while h > 0:
        for i in range(0, len(arr), h):
            item = arr[i]
            j = i
            while j > 0 and item < arr[j - 1]:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = item

        h = int(h // const)

    return arr


# Метод вставок с барьером
# Применение элемента-барьера позволяет избежать проверки индекса при выполнении
# вставок и упрощает логику алгоритма.
# Сложность О(n^2)
def insert_barrier(arr):
    arr = [0] + arr
    for i in range(1, len(arr)):
        arr[0] = arr[i]
        j = i - 1
        while arr[0] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[0]
    return arr[1:]


# "гномья" сортировка
# Проходимся по массиву. Если видим, что число стоит не на своем месте, свапаем до тех пор обратно,
# пока не встанет на свое место. Затем возвращаемся и продолжаем так же искать элементы
# Сложность O(n^2)
def gnom(arr):
    ind = 1
    while ind < len(arr):
        if ind == 0:
            ind = 1
        if arr[ind - 1] < arr[ind]:
            ind += 1
        else:
            arr[ind - 1], arr[ind] = arr[ind], arr[ind - 1]
            ind -= 1
    return arr

