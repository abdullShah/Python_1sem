"""
Абдуллаев Шахмар ИУ7-14Б
Программа создана для выполнения некоторых операций с бинарным файлом:
0) Выход из программы.
1) Ввод чисел в файл (если файл существует - перезаписывать).
2) Сортировка пирамидальным методом.
3) Вывод изменённого содержимого файла.
"""
from module_main import *

file_path = input_numbers_to_file('')  # Первоначальное получение файла
num_action = menu()  # Меню
func_action = check_action(num_action)  # Выбор действия
file_path = func_action(file_path)  # Выполнение действия
while num_action:  # Проверка на продолжение работы
    num_action = menu()  # Меню
    func_action = check_action(num_action)  # Выбор действия
    file_path = func_action(file_path)  # Выполнение действия
