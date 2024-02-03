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
