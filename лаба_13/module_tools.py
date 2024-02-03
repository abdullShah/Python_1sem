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


# Функция для проверки корректности файла
def file_check(file, status):
    try:
        if status == 'open':
            if file[-4:] == '.txt' or file[-4:] == '.csv':
                with open(file, 'r', encoding='UTF-8') as file:
                    first_occurrence = True
                    for line in file:
                        if first_occurrence:
                            first_occurrence = False
                            data = line.strip().split(';')
                            columns = ['Фамилия', 'Возраст', 'Позиция', 'Завершена ли карьера']
                            if len(data) != 4:
                                print('База не соответствует структуре!')
                                return None
                            if data != columns:
                                print('База не соответствует структуре!')
                                return None
                            continue

                        data = line.strip().split(';')
                        if len(data) != 4:
                            print('База не соответствует структуре!')
                            return None
                        surname, age, position, career = data[0], data[1], data[2], data[3]
                        if not (check_surname(surname) and check_age(age) and
                                check_position(position) and check_career(career)):
                            print('База не соответствует структуре!')
                            return None
                return file
            else:
                print('Файл не является текстовым!')
                return None
        if status == 'init':
            if file[-4:] == '.txt' or file[-4:] == '.csv':
                with open(file, 'w', encoding='UTF-8') as f:
                    f.write('')
                return file
            else:
                print('Файл не текстовый!')
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
