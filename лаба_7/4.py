"""
Абдуллаев Шахмар ИУ7-14Б
Замена всех строчных согласных английских букв на заглавные.
"""

arr = list(input("Введите элементы списка: ").split())
if len(arr) == 0:
    print("Введен пустой список!")
    arr = list(input("Введите элементы списка: ").split())

letters = 'bcdfghjklmnpqrstvwxz'

for i in range(0, len(arr)):
    # Переменная для строчки
    string = arr[i]
    # Переменная для измененной строчки
    new_str = ''
    for letter in string:
        # Проверка на то, что буква строчная согласная английская
        if letter in letters:
            # Изменяем регистр
            new_str += letter.upper()
        else:
            # Не изменяем букву
            new_str += letter
    arr[i] = new_str

print("Измененный список: ", end="")
for q in range(len(arr)):
    print(arr[q], end=" ")
