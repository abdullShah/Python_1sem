########main
from module_main import *

file_path = main_file_selection('')  # Первоначальное получение файла
num_action = menu()  # Меню
func_action = check_action(num_action)  # Выбор действия
file_path = func_action(file_path)  # Выполнение действия
while num_action:  # Проверка на продолжение работы
    num_action = menu()  # Меню
    func_action = check_action(num_action)  # Выбор действия
    file_path = func_action(file_path)  # Выполнение действия




########module_main
from module_action import *
from module_tools import *


def all_commands():
    commands = {
        0: 'Выйти из программы.',
        1: 'Выбрать файл для работы.',
        2: 'Инициализировать базу данных.',
        3: 'Вывести содержимое базы данных.',
        4: 'Добавить запись в произвольное место базы данных.',
        5: 'Удалить произвольную запись из базы данных',
        6: 'Поиск по одному полю.',
        7: 'Поиск по двум полям.',
        8: 'Вывод текущей базы данных.'
    }
    return commands.copy()


def menu():
    print("Список команд")
    commands = all_commands()
    for num_command, command in commands.items():
        print(f'{num_command}. {command}')
    print()

    user_command = input_command()

    return user_command


def define_action(num_action):
    commands = {
        0: exit_of_program,
        1: main_file_selection,
        2: initialize_database,
        3: print_content,
        4: add_to_place,
        5: del_note,
        6: search_by_one_field,
        7: search_by_two_fields,
        8: print_current_database
    }
    return commands[num_action]


def check_action(num_action):
    commands = all_commands()
    while num_action not in commands:
        print("Введена несуществующая команда! Повторите попытку\n")
        num_action = input_command()

    return define_action(num_action)




########module_action
from module_tools import *


# Функция для выхода из программы
def exit_of_program(file):
    print('Вы вышли из программы! До следующего запуска!')
    return file


# Функция для итогового выбора файла
def main_file_selection(pas):
    success = file_selection()
    while success == "back":
        success = file_selection()

    print(f"\nТекущая база данных: {success}\n")
    return success


# Функция для выбора файла
def file_selection():
    print('Укажем путь файла для работы!')
    print('Хотите выбрать заранее созданную базу данных (1) или выбрать любой файл (2)? Ваш выбор: ', end="")
    choose_num = input()
    while choose_num not in ['1', '2']:
        print("Некорректный ввод! Повторите попытку")
        print('Хотите выбрать заранее созданную базу данных (1) или выбрать любой файл (2)? ', end="")
        choose_num = input()
    choose_num = int(choose_num)

    file_path = ''
    if choose_num == 1:
        file_path = r"E:\Программирование\лаба_14\football.bin"
    elif choose_num == 2:
        file = input('Введите директорию (0-назад): ')
        if file == "0":
            return 'back'
        while file_check(file, 'open') is None:
            file = input('Введите директорию (0-назад): ')
            if file == "0":
                return 'back'
        file_path = file

    return file_path


# Функция для инициализации базы данных
def initialize_database(pas):
    file = input('Введите путь создаваемого файла: ')
    while file_check(file, 'init') is None:
        file = input('Введите путь создаваемого файла: ')

    cnt_row = int_row()
    print()
    with open(file, 'ab') as f:
        for i in range(cnt_row):
            surname, age, position, career = columns_value()
            print()
            f.write(struct.pack(f'>20s', surname.encode('CP1251')))
            f.write(struct.pack(f'>i', int(age)))
            f.write(struct.pack(f'>12s', position.encode('CP1251')))
            f.write(struct.pack(f'>3s', career.encode('CP1251')))

    return file


# Функция для вывода содержимого файла
def print_content(file):
    print()
    lines = find_lines_cnt(file)
    print(f'{"id":<5}{"Фамилия":<25}{"Возраст":<10}{"Позиция":<15}{"Завершена ли карьера":<25}')
    with open(file, 'rb') as f:
        line_now = 0
        while line_now < lines:
            data = unpacking_line(f.read(get_line_size()))
            surname, age, position, career = data[0], data[1], data[2], data[3]
            print(
                f'{line_now + 1:<5}{surname:<25}{age:<10}{position:<15}{career:<25}'
            )
            line_now += 1
    print()
    return file


# Функция добавления записи в произвольное место базы данных
def add_to_place(file):
    count_of_lines = find_lines_cnt(file)
    prompt = f'Введите номер строки от 1 до {count_of_lines}, на место которой добавиться новый элемент: '
    index = input_int(prompt)
    while index < 1 or index > count_of_lines:
        print(f'Число должно быть от {1} до {count_of_lines}! Повторите попытку\n')
        index = input_int(prompt)

    with open(file, 'rb+') as f:
        for i in range(count_of_lines - index + 1):
            if i == 0:
                f.seek(-get_line_size(), 2)
            else:
                f.seek(-get_line_size() * 3, 1)
            cur_line = f.read(get_line_size())
            f.write(cur_line)
        f.seek((index - 1) * get_line_size())
        surname, age, position, career = columns_value()
        print()
        f.write(struct.pack(f'>20s', surname.encode('CP1251')))
        f.write(struct.pack(f'>i', int(age)))
        f.write(struct.pack(f'>12s', position.encode('CP1251')))
        f.write(struct.pack(f'>3s', career.encode('CP1251')))

    return file


# Функция удаления произвольной записи из базы данных
def del_note(file):
    count_of_lines = find_lines_cnt(file)
    if count_of_lines == 0:
        print("Невозможно удалить строку в пустом файле!")
        print()
        return file

    prompt = f'Введите номер удаляемой записи от 1 до {count_of_lines}: '
    index = input_int(prompt)
    while index < 1 or index > count_of_lines:
        print(f'Число должно быть от {1} до {count_of_lines}! Повторите попытку\n')
        index = input_int(prompt)

    with open(file, 'rb+') as f:
        line_size = get_line_size()
        f.seek(index * line_size, 0)
        for i in range(count_of_lines - index):
            line = f.read(line_size)
            f.seek(-2 * line_size, 1)
            f.write(line)
            f.seek(line_size, 1)
        f.seek(-line_size, 1)
        f.truncate()  # Происходит усечение файла до текущей позиции в файле

    print()
    return file


# Функция для поиска по одному полю
def search_by_one_field(file):
    column = input("Введите номер столбца, по которому будет осуществляться поиск "
                   "(Фамилия - 1/Возраст - 2/Позиция - 3/Завершена ли карьера 4): ")
    columns = {
        '1': 'Фамилия',
        '2': 'Возраст',
        '3': 'Позиция',
        '4': 'Завершена ли карьера'
    }
    while column not in columns:
        print("Введен несуществующий столбец! Повторите попытку")
        column = input("Введите номер столбца, по которому будет осуществляться поиск "
                       "(Фамилия - 1/Возраст - 2/Позиция - 3/Завершена ли карьера 4): ")
    search_val = input("Введите значение, которое будет найдено: ")
    while len(search_val.strip()) == 0:
        print("Введена пустая строка! Повторите попытку")
        search_val = input("Введите значение, которое будет найдено: ")

    columns_dict = {
        'Фамилия': 0,
        'Возраст': 1,
        'Позиция': 2,
        'Завершена ли карьера': 3
    }
    print()
    with open(file, 'rb') as f:
        is_value_found = True
        lines = find_lines_cnt(file)
        line_now = 0
        while line_now < lines:
            data = unpacking_line(f.read(get_line_size()))
            value = data[columns_dict[columns[column]]]
            if partial_match(search_val, value):
                is_value_found = False
                surname, age, position, career = data[0], data[1], data[2], data[3]
                print(
                    f'{line_now + 1:<5}{surname:<25}{age:<10}{position:<15}{career:<25}'
                )
            line_now += 1

        if is_value_found:
            print("В базе нет такой строки!")

    print()
    return file


# Функция для поиска по двум полям
def search_by_two_fields(file):
    columns = {
        '1': 'Фамилия',
        '2': 'Возраст',
        '3': 'Позиция',
        '4': 'Завершена ли карьера'
    }
    column_1 = input("Введите номер первого столбца, по которому будет осуществляться поиск "
                     "(Фамилия - 1/Возраст - 2/Позиция - 3/Завершена ли карьера 4): ")
    while column_1 not in columns:
        print("Введен несуществующий столбец! Повторите попытку")
        column_1 = input("Введите номер первого столбца, по которому будет осуществляться поиск "
                         "(Фамилия - 1/Возраст - 2/Позиция - 3/Завершена ли карьера 4): ")
    search_val_1 = input("Введите его значение, которое будет найдено: ")
    while len(search_val_1.strip()) == 0:
        print("Введена пустая строка! Повторите попытку")
        search_val_1 = input("Введите его значение, которое будет найдено: ")

    column_2 = input("Введите номер второго столбца, по которому будет осуществляться поиск "
                     "(Фамилия - 1/Возраст - 2/Позиция - 3/Завершена ли карьера 4): ")
    while column_2 not in columns or column_1 == column_2:
        while column_2 not in columns:
            print("Введен несуществующий столбец! Повторите попытку")
            column_2 = input("Введите номер второго столбца, по которому будет осуществляться поиск "
                             "(Фамилия - 1/Возраст - 2/Позиция - 3/Завершена ли карьера 4): ")
        while column_1 == column_2:
            print("Такой столбец уже введен! Повторите попытку")
            column_2 = input("Введите номер второго столбца, по которому будет осуществляться поиск "
                             "(Фамилия - 1/Возраст - 2/Позиция - 3/Завершена ли карьера 4): ")

    search_val_2 = input("Введите его значение, которое будет найдено: ")
    while len(search_val_2.strip()) == 0:
        print("Введена пустая строка! Повторите попытку")
        search_val_2 = input("Введите его значение, которое будет найдено: ")

    columns_dict = {
        'Фамилия': 0,
        'Возраст': 1,
        'Позиция': 2,
        'Завершена ли карьера': 3
    }
    print()

    with open(file, 'rb') as f:
        is_value_found = True
        lines = find_lines_cnt(file)
        line_now = 0
        while line_now < lines:
            data = unpacking_line(f.read(get_line_size()))
            value_1 = data[columns_dict[columns[column_1]]]
            value_2 = data[columns_dict[columns[column_2]]]
            if partial_match(search_val_1, value_1) and partial_match(search_val_2, value_2):
                is_value_found = False
                surname, age, position, career = data[0], data[1], data[2], data[3]
                print(
                    f'{line_now + 1:<5}{surname:<25}{age:<10}{position:<15}{career:<25}'
                )
            line_now += 1

        if is_value_found:
            print("В базе нет такого поля!")

    print()
    return file


# Функция для вывода текущей базы данных
def print_current_database(file):
    print(f"\nТекущая база данных: {file}\n")
    return file





########module_tools
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
