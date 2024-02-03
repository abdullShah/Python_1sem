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


# Функция удвоения числа
def double_value(file):
    with open(file, 'rb+') as f:
        cnt_krat_3 = 0
        line_size = get_line_size()
        for i in range(get_size(file) // line_size):
            f.seek(i * line_size)
            line = f.read(line_size)
            num = unpacking_line(line)
            if abs(num) % 3 == 0:
                cnt_krat_3 += 1

        old_len = get_size(file) // line_size
        for _ in range(cnt_krat_3):
            f.write(struct.pack(f'>i', 1))
        f.seek(0)
        k = 1
        for i in range(old_len - 1, -1, -1):
            f.seek(i * line_size)
            line = f.read(line_size)
            num = unpacking_line(line)
            if abs(num) % 3 != 0:
                f.seek(-k * line_size, 2)
                f.write(line)
                k += 1
            else:
                f.seek(-k * line_size, 2)
                f.write(struct.pack(f'>i', num * 2))
                k += 1
                f.seek(-k * line_size, 2)
                f.write(line)
                k += 1
    print()
    return file


'''
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
'''


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
