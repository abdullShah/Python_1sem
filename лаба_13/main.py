"""
Абдуллаев Шахмар ИУ7-14Б
Программа создана для выполнения некоторых операций с базой данных.
"""
from module_main import *

file_path = main_file_selection('')  # Первоначальное получение файла
num_action = menu()  # Меню
func_action = check_action(num_action)  # Выбор действия
file_path = func_action(file_path)  # Выполнение действия
while num_action:  # Проверка на продолжение работы
    num_action = menu()  # Меню
    func_action = check_action(num_action)  # Выбор действия
    file_path = func_action(file_path)  # Выполнение действия
