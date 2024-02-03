import os
import struct

'''
r - открывает файл только для чтения
w - открыт для записи (перед записью файл будет очищен)
a - открыт для добавления в конец файла
+ - символ обновления (чтение + запись)
b - символ двоичного режима
'''


# Функция для перевода в int
def input_int(prompt):
    while True:
        try:
            x = input(prompt)
            x = int(x)
            return x
        except ValueError:
            print("Введены некорректные данные! Повторите попытку\n")


# Функция для проверки команды
def input_command():
    print("Выберите команду: ", end="")
    command = input()

    try:
        corr_command = int(command)
    except:
        print("Введены некорректные данные! Повторите попытку\n")
        corr_command = input_command()

    return corr_command


# Функция для проверки количество строк
def int_row():
    cnt_row = -1
    while cnt_row < 0:
        try:
            cnt_row = int(input("Сколько будет строчек в этой базе? Ваш выбор: "))
            if cnt_row < 0:
                print("Количество строк должно быть неотрицательным! Повторите попытку")
        except ValueError:
            print("Введены некорректные данные! Повторите попытку")

    return cnt_row


# Функция для проверки столбца фамилии
def check_surname(value):
    # Фамилия начинается с большой буквы и состоит только из букв
    if len(value.strip()) != 0 and value.istitle() and value.isalpha():
        return True
    return False


# Функция для проверки столбца возраста
def check_age(value):
    try:
        value = int(value)
    except ValueError:
        return False

    if not (18 <= value <= 60):
        return False

    return True


# Функция для проверки столбца позиции
def check_position(value):
    positions = ['Нападающий', 'Полузащитник', 'Защитник', 'Вратарь']
    if value not in positions:
        return False
    return True


# Функция для проверки столбца карьеры
def check_career(value):
    if value not in ["Да", "Нет"]:
        return False
    return True


# Функция получения размера одной строки
def get_line_size():
    return 39


# Нахождение размера файла БД
def get_size(file):
    return os.path.getsize(file)


# Нахождение количества строк в БД
def find_lines_cnt(file):
    return get_size(file) // get_line_size()


# Распаковка (вывод) строки БД
def unpacking_line(string):
    # \0 используется для определения конца строк в стиле C
    text = list(struct.unpack(f'>20s i 12s 3s', string))
    text[0] = text[0].decode('CP1251').strip('\0')
    text[2] = text[2].decode('CP1251').strip('\0')
    text[3] = text[3].decode('CP1251').strip('\0')

    return text


# Функция для проверки корректности файла
def file_check(file, status):
    try:
        if status == 'open':
            if file[-4:] == '.bin':
                if (get_size(file) / get_line_size()) % 1 == 0:
                    lines = find_lines_cnt(file)
                    # if lines == 0:
                    #     print('Бинарный файл не соответствует структуре!')
                    #     return None
                    # else:
                    with open(file, 'rb') as f:
                        line_now = 0
                        while line_now < lines:
                            data = unpacking_line(f.read(get_line_size()))
                            surname, age, position, career = data[0], data[1], data[2], data[3]
                            if not (check_surname(surname) and check_age(age) and
                                    check_position(position) and check_career(career)):
                                print('База не соответствует структуре!')
                                return None
                            line_now += 1
                    return file
                print('Бинарный файл не соответствует структуре!')
                return None
            else:
                print('Файл не является бинарным!')
                return None
        if status == 'init':
            if file[-4:] == '.bin':
                with open(file, 'ab') as f:
                    pass
                return file
            else:
                print('Файл не бинарный!')
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
        if status == 'open':
            print('Файла не существует!')
            return None
    except OSError:
        print('Неверный путь к файлу!')
        return None
    return None


# Функция для частичного совпадения строки
def partial_match(search_val, value):
    return search_val.lower() == value or search_val.capitalize() == value


# Функция для получения данных строки
def columns_value():
    surname = input("Введите фамилию футболиста: ")
    while not check_surname(surname):
        print("Неверная структура фамилии! Повторите попытку")
        surname = input("Введите фамилию футболиста: ")

    age = input("Введите его возраст: ")
    while not check_age(age):
        print("Введен невозможный возраст! Повторите попытку")
        age = input("Введите его возраст: ")

    positions = {
        '1': 'Нападающий',
        '2': 'Полузащитник',
        '3': 'Защитник',
        '4': 'Вратарь'
    }
    position = input("Введите его позицию (Нападающий - 1/Полузащитник - 2/Защитник - 3/Вратарь - 4): ")
    while position not in positions or not check_position(positions[position]):
        print("Введена несуществующая позиция! Повторите попытку")
        position = input("Введите его позицию (Нападающий - 1/Полузащитник - 2/Защитник - 3/Вратарь - 4): ")

    careers = {
        '1': "Да",
        '2': "Нет"
    }
    career = input("Завершена ли его карьера (Да - 1/Нет - 2): ")
    while career not in careers or not check_career(careers[career]):
        print("Удовлетворяют ответы только Да или Нет! Повторите попытку")
        career = input("Завершена ли его карьера (Да - 1/Нет - 2): ")

    return surname, age, positions[position], careers[career]
