import os
import struct


# Функция для проверки элементов списка:
def arr_el_check(arr):
    try:
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return True
    except ValueError:
        return False


# Функция для проверки команды
def input_command():
    print("Выберите команду: ", end="")
    command = input()

    try:
        corr_command = int(command)
    except ValueError:
        print("Введены некорректные данные! Повторите попытку\n")
        corr_command = input_command()

    return corr_command


# Функция получения размера одной строки
def get_line_size():
    return 4


# Нахождение размера файла БД
def get_size(file):
    return os.path.getsize(file)


# Нахождение количества строк в БД
def find_lines_cnt(file):
    return get_size(file) // get_line_size()


# Распаковка (вывод) строки БД
def unpacking_line(string):
    # \0 используется для определения конца строк в стиле C
    text = list(struct.unpack(f'>i', string))

    return text[0]


# Функция для проверки корректности файла
def file_check(file, arr):
    try:
        if file[-4:] == '.bin':
            with open(file, 'wb+') as f:
                for item in arr:
                    f.write(struct.pack(f'>i', item))
            return file
        else:
            print('Файл не является бинарным!')
            return None
    except IsADirectoryError:
        print('Указанное место на диске является директорией!')
        return None
    except PermissionError:
        print('Нет доступа к файлу!')
        return None
    except UnicodeError:
        print('Ошибка кодировки!')
        return None
    except FileNotFoundError:
        print('Файла не существует!')
    except OSError:
        print('Неверный путь к файлу!')
        return None
