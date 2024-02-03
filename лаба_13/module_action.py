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
        file_path = r"football.txt"
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
    with open(file, 'w', encoding='UTF-8') as f:
        f.write('Фамилия;Возраст;Позиция;Завершена ли карьера')
        for i in range(cnt_row):
            surname, age, position, career = columns_value()
            print()
            f.write(f'\n{surname};{age};{position};{career}')

    return file


# Функция для вывода содержимого файла
def print_content(file):
    print()
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            data = line.strip().split(';')
            surname, age, position, career = data[0], data[1], data[2], data[3]
            print(
                f'{surname:<25}{age:<10}{position:<15}{career:<25}'
            )
    print()
    return file


# Функция добавления записи в конец базы данных
def add_to_end(file):
    surname, age, position, career = columns_value()

    with open(file, 'a', encoding='UTF-8') as f:
        f.write(f'\n{surname};{age};{position};{career}')

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
    with open(file, 'r', encoding='UTF-8') as f:
        is_value_found = True
        first_occurrence = True
        for line in f:
            if first_occurrence:
                first_occurrence = False
                continue
            data = line.strip().split(';')
            value = data[columns_dict[columns[column]]]
            if partial_match(search_val, value):
                is_value_found = False
                surname, age, position, career = data[0], data[1], data[2], data[3]
                print(
                    f'{surname:<25}{age:<10}{position:<15}{career:<25}'
                )

        if is_value_found:
            print("В базе нет такого поля!")
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
    with open(file, 'r', encoding='UTF-8') as f:
        is_value_found = True
        first_occurrence = True
        for line in f:
            if first_occurrence:
                first_occurrence = False
                continue
            data = line.strip().split(';')
            value_1 = data[columns_dict[columns[column_1]]]
            value_2 = data[columns_dict[columns[column_2]]]
            if partial_match(search_val_1, value_1) and partial_match(search_val_2, value_2):
                is_value_found = False
                surname, age, position, career = data[0], data[1], data[2], data[3]
                print(
                    f'{surname:<25}{age:<10}{position:<15}{career:<25}'
                )

        if is_value_found:
            print("В базе нет такого поля!")
    print()
    return file


# Функция для вывода текущей базы данных
def print_current_database(file):
    print(f"\nТекущая база данных: {file}\n")
    return file
