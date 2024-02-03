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
        file_path = "football.bin"
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
    prompt = f'Введите номер строки от 1 до {count_of_lines + 1}, на место которой добавиться новый элемент: '
    index = input_int(prompt)
    while index < 1 or index > count_of_lines + 1:
        print(f'Число должно быть от {1} до {count_of_lines + 1}! Повторите попытку\n')
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
            value_1 = str(value_1)
            value_2 = data[columns_dict[columns[column_2]]]
            value_2 = str(value_2)
            # print(partial_match(search_val_1, value_1), type(search_val_1), type(value_1))
            # print(partial_match(search_val_2, value_2), type(search_val_2), type(value_2))
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
