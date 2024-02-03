'''
name1 name2 name3
surname1 surname2 surname3
'''

arr_name = list(input("Введите имена через пробел: ").split())
arr_surname = list(input("Введите фамилии через пробел: ").split())

# arr_name = list('name1 name2 name3 name4 name5'.split())
# arr_surname = list('surname1 surname2 surname3 surname4 surname5'.split())


while len(arr_surname) != len(arr_name):
    print("Количество введеных имен и фамилий не равно! Повторите попытку")
    arr_name = list(input("Введите имена через пробел: ").split())
    arr_surname = list(input("Введите фамилии через пробел: ").split())

while len(arr_surname) == 0:
    print("Не введены элементы списка! Повторите попытку")
    arr_name = list(input("Введите имена через пробел: ").split())
    arr_surname = list(input("Введите фамилии через пробел: ").split())

arr_name += len(arr_name) * [None]
k = 1
iteration = 0
for i in range(len(arr_name) - 1, 0, -1):
    if iteration == len(arr_surname):
        break

    arr_name[-(k + 1)] = arr_name[i - len(arr_surname)]
    arr_name[-k] = arr_surname[i - len(arr_surname)]
    k += 2
    iteration += 1

print('Новый список: ')
for q in range(len(arr_name)):
    print(arr_name[q], end=" ")
    if q % 2 == 1:
        print()
