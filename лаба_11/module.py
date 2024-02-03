from random import randint, sample
from time import time


def input_arr():
    arr = input("Введите элементы списка через пробел: ").split()

    while len(arr) == 0:
        print('Длина списка равна нулю! Повторите попытку')
        arr = input_arr()

    try:
        arr = list(map(int, arr))
        return arr
    except:
        print("Введены некорректные данные! Повторите попытку")
        arr = input_arr()
        return arr


# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i и с функцией
# просеивания: будет перемещаться самый верхний элемент вниз, чтобы получить новый верхний элемент
def heapify(arr, n, i):
    cnt = 0

    root = i  # Корневой элемент
    # Зададим переменные, по которым сможем обращаться к дочерним элементам
    l = 2 * i + 1
    r = 2 * i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        root = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and arr[root] < arr[r]:
        root = r

    # Заменяем корень, если нужно
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]  # Замена соседних элементов списка, обмен значениями
        cnt += 1

        # Применяем heapify к корню.
        heapify(arr, n, root)

    return cnt


# Основная функция для сортировки массива заданного размера
def heap_sort(arr):
    n = len(arr)
    cnt = 0

    # Построение max-heap
    for i in range(n, -1, -1):
        cnt += heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        cnt += 1
        arr[i], arr[0] = arr[0], arr[i]  # Замена соседних элементов списка, обмен значениями

        cnt += heapify(arr, i, 0)

    return cnt


def print_arr(arr, text):
    print(f"{text} список: ", end="")
    for i in arr:
        print(i, end=" ")
    print()


def dict_create(arr):
    dictionary = {}
    for i in range(len(arr)):
        dictionary[f"N{i + 1}"] = arr[i]
    return dictionary


def input_dimensions():
    arr = input("Введите три размерности через пробел: ").split()

    while len(arr) != 3:
        print('Не введены три размерности! Повторите попытку')
        arr = input_arr()

    try:
        arr = list(map(int, arr))
        return dict_create(arr)
    except:
        print("Введены некорректные данные! Повторите попытку")
        arr = input_arr()
        return dict_create(arr)


def generate_rand_matrix(arr_cnt):
    matrix = []
    for cnt in arr_cnt.values():
        matrix.append(
            # [randint(-10_000, 10_000) for _ in range(cnt)]
            sample(range(-10_000, 10_000 + 1), cnt)
        )
    return matrix


def print_dimensions(arr):
    for key, val in arr.items():
        print(f'{key}: {val}')


def measurement(matrix):
    arr_val = []
    for arr in matrix:
        time_start = time()
        cnt = heap_sort(arr)
        time_end = time()
        delta_time = time_end - time_start
        arr_val.append({'time': delta_time, 'cnt': cnt})
    return arr_val


def get_matrix_values(arr_dimensions):
    matrix_values = []
    work_matrix = generate_rand_matrix(arr_dimensions)

    # Случайный список
    matrix_values.append(measurement(work_matrix))
    # Упорядоченный список
    matrix_values.insert(0, measurement(work_matrix))
    # Упорядоченный в обратном порядке
    for arr in range(len(work_matrix)):
        work_matrix[arr] = work_matrix[arr][::-1]
    matrix_values.append(measurement(work_matrix))

    return matrix_values


def print_head(arr, width):
    print(f"{'':^{width}}", end="")
    for item in arr:
        print(f"{item:^{width}}", end="")
    print()

    print(f"{'':^{width}}", end="")
    for _ in range(len(arr)):
        print(f"{'время, с.':^{width // 2}}", end="")
        print(f"{'перестановки, кол.':^{width // 2}}", end="")

    print()


def print_body(matrix, width):
    texts = ['Упорядоченный список', 'Случайный список', 'Упорядоченный в обратном порядке']
    for i in range(len(texts)):
        print(f"{texts[i]:^{width}}", end="")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]['time']:^{width // 2}.5g}", end="")
            print(f"{matrix[i][j]['cnt']:^{width // 2}}", end="")
        print()


def print_table(matrix, arr, width=50):
    print_head(arr, width)
    print_body(matrix, width)
