from module_tools import *


# Функция для выхода из программы
def exit_of_program(file):
    print('Вы вышли из программы! До следующего запуска!')
    return file


# Функция для ввода чисел в файл
def input_numbers_to_file(pas):
    arr = input("Введите элементы списка: ").split()
    while len(arr) == 0 or not arr_el_check(arr):
        while len(arr) == 0:
            print("Введен пустой список!\n")
            arr = input("Введите элементы списка: ").split()
        while not arr_el_check(arr):
            print("Введены нечисловые элементы! Повторите попытку\n")
            arr = input("Введите элементы списка: ").split()
    arr = map(int, arr)

    file = input('Укажите путь файла для работы: ')
    while file_check(file, arr) is None:
        file = input('Укажите путь файла для работы: ')

    print(f"\nТекущая база данных: {file}\n")

    return file


# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i и с функцией
# просеивания: будет перемещаться самый верхний элемент вниз, чтобы получить новый верхний элемент
def heapify(f, n, i):
    root = i  # Корневой элемент
    # Зададим переменные, по которым сможем обращаться к дочерним элементам
    l = 2 * i + 1
    r = 2 * i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and get_element(f, root) < get_element(f, l):
        root = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and get_element(f, root) < get_element(f, r):
        root = r

    # Заменяем корень, если нужно
    if root != i:
        swap_elements(f, i, root)  # Замена соседних элементов списка, обмен значениями
        # Применяем heapify к корню
        heapify(f, n, root)


# Основная функция для сортировки массива заданного размера
def heap_sort(file):
    n = find_lines_cnt(file)
    with open(file, 'rb+') as f:
        # Построение max-heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(f, n, i)
        # Один за другим извлекаем элементы
        for i in range(n - 1, 0, -1):
            swap_elements(f, i, 0)  # Замена соседних элементов списка, обмен значениями
            heapify(f, i, 0)


# Функция для сортировки файла
def sort_file(file):
    heap_sort(file)
    print("Файл отсортирован!\n")
    return file


# Функция для вывода содержимого файла
def print_content(file):
    print()
    lines = find_lines_cnt(file)
    with open(file, 'rb') as f:
        line_now = 0
        while line_now < lines:
            num = unpacking_line(f.read(get_line_size()))
            print(num, end=' ')
            line_now += 1
    print('\n')
    return file


# Функция для вывода текущего файла
def print_current_file(file):
    print(f"\nТекущая файл: {file}\n")
    return file
