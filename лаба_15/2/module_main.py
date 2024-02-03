from module_action import *
from module_tools import *


def all_commands():
    commands = {
        0: 'Выйти из программы.',
        1: 'Ввод чисел в файл.',
        2: 'После каждого числа, кратного трём, добавить его удвоенное значение.',
        3: 'Вывод изменённого содержимого файла.',
        4: 'Вывод текущего файла.'
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
        1: input_numbers_to_file,
        2: double_value,
        3: print_content,
        4: print_current_file
    }
    return commands[num_action]


def check_action(num_action):
    commands = all_commands()
    while num_action not in commands:
        print("Введена несуществующая команда! Повторите попытку\n")
        num_action = input_command()

    return define_action(num_action)
