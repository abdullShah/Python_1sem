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

# Функция удаления всех нулевых чисел
def remove_null_numbers(file):
    with open(file, 'rb+') as f:
        line_size = get_line_size()
        k = 0
        for i in range(get_size(file) // line_size):
            f.seek(i * line_size)
            line = f.read(line_size)
            num = unpacking_line(line)
            if num == 0:
                k += 1
            else:
                f.seek((i - k) * line_size)
                f.write(line)
        f.seek(-k * line_size, 2)
        f.truncate()  # Происходит усечение файла до текущей позиции в файле

    print()
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
