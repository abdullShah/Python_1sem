from module_action import *
from module_tools import *


def all_commands():
    commands = {
        0: 'Выйти из программы.',
        1: 'Выровнять текст по левому краю.',
        2: 'Выровнять текст по правому краю.',
        3: 'Выровнять текст по ширине.',
        4: 'Удаление всех вхождений заданного слова.',
        5: 'Замена одного слова другим во всём тексте.',
        6: 'Вычисление арифметических выражений над целыми числами внутри текста (сложение и вычитание).',
        7: 'Найти (вывести на экран) и затем удалить '
           'предложение с максимальным количеством слов, в котором гласные чередуются с согласными.'
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
        1: to_left_edge,
        2: to_right_edge,
        3: to_by_width,
        4: delete_all_words,
        5: replace_in_all_text,
        6: calc_arith,
        7: find_and_del
    }
    return commands[num_action]


def check_action(num_action):
    commands = all_commands()
    while num_action not in commands:
        print("Введена несуществующая команда! Повторите попытку\n")
        num_action = input_command()

    return define_action(num_action)
