"""
Абдуллаев Шахмар ИУ7-14Б
"""
from zach_2_mod import *


main_text = []

# main_text = [
#     'Привет, папа. Папа, у меня тоже',
#     'все хорошо папа. Увидимся.'
# ]

'''
Word ... how 
many in this
word. Maybe, word is ... Word!
Please, use another syms. Or,
maybe word. Butn numbers
'''



num_action = menu()  # Меню
func_action = define_action(num_action)  # Выбор действия
main_text = func_action(main_text)  # Выполнения действия
print_text(main_text)  # Вывод текста
while num_action:  # Проверка на продолжение работы
    num_action = menu()
    func_action = define_action(num_action)
    main_text = func_action(main_text)
    print_text(main_text)