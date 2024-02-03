'''
Абдуллаев Шахмар ИУ7-14Б
'''
from module import *

# Получение первого файла
file_1 = input('Введите путь первого файла: ')
while file_check(file_1, "open") is None:
    file_1 = input('Введите путь первого файла: ')

# Получение второго файла
file_2 = input('Введите путь второго файла: ')
while file_check(file_2, "init") is None:
    file_2 = input('Введите путь второго файла: ')

# Переворацивание второго файла
revers_files(file_1, file_2)
