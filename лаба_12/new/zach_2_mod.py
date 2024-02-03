# Функция для добавления пробелов, выравнивание слева
def to_left_edge(main_text):
    lines = main_text
    max_len = 0
    for i in range(len(lines)):
        lines[i] = ' '.join(lines[i].split())
        line = lines[i]
        max_len = max(max_len, len(line))

    for i in range(len(lines)):
        lines[i] = lines[i].strip() + ' ' * (max_len - len(lines[i].strip()))

    return_main_text = lines

    return return_main_text

# Функция для красивого вывода текста
def print_text(main_text):
    lines = main_text
    width = 0
    for line in lines:
        width = max(len(line), width)

    print()
    print('+' + '-' * width + '+')
    for line in lines:
        print('|' + line + '|')
    print('+' + '-' * width + '+')
    print()

# Функция создания списка предложений с определенными правилами
def separation_by_offers(input_strings):
    output_strings = []
    for i in range(len(input_strings)):
        string = input_strings[i]
        parts = string.split(".")
        if parts[-1] == "":
            # В конце строки точка
            del parts[-1]
            parts[-1] += '.'

        if i != len(input_strings) - 1:
            parts[-1] += '@'

        for j in range(len(parts)):
            part = parts[j]
            if j != len(parts) - 1:
                part += "."

            output_strings.append(part)

    itog = []
    old_str = ''
    for item in output_strings:
        if '.' in item:
            if old_str:
                itog.append(old_str + item)
                old_str = ""
            else:
                itog.append(item)
        else:
            old_str = item

    return itog

# Обратная функция separation_by_offers: перевод из особого текста в нормальный
def revers_separation_by_offers(input_strings):
    output_strings = []
    cur_str = ""
    for i in range(len(input_strings)):
        string = input_strings[i]
        if '@' not in string:
            cur_str += string
        else:
            ind_sp = string.index("@")
            cur_str += string[:ind_sp]
            output_strings.append(cur_str)
            cur_str = string[ind_sp + 1:]
    output_strings.append(cur_str)
    return output_strings

# Функция для команд программы
def all_commands():
    commands = {
        0: 'Выйти из программы.',
        1: 'Считать текст с клавиатуры, как список строк',
        2: 'Удалить предложение, содержащее самое встречающееся слово в тексте'
    }
    return commands.copy()

# Функция вывода меню
def menu():
    print("Список команд")
    commands = all_commands()
    for num_command, command in commands.items():
        print(f'{num_command}. {command}')
    print()

    print("Выберите команду: ", end="")
    user_command = input()

    return int(user_command)

# Функция для ввода текста
def read_text(main_text):
    n = int(input("Введите количество строк: "))
    print("Введите строки:")
    output_text = []
    for _ in range(n):
        row = input()
        output_text.append(row)

    output_text = to_left_edge(output_text)
    return output_text

# Функция для удаления предложения с популярным словом
def del_sentence(main_text):
    if main_text[-1] == "":
        return main_text
    split_arr = separation_by_offers(main_text)
    split_arr_without = split_arr.copy()
    for i in range(len(split_arr_without)):
        if i >= len(split_arr_without):
            break

        row = split_arr_without[i]
        if '.' in row:
            split_arr_without[i] = split_arr_without[i].replace('.','')
        if '@' in row:
            new_row = ' '.join(row.split("@"))
            del split_arr_without[i]
            split_arr_without = split_arr_without[i:] + [new_row] + split_arr_without[i:]


    words_in_text = {}
    for i in range(len(split_arr_without)):
        row = split_arr_without[i]
        words = row.split()
        for word in words:
            if word not in words_in_text:
                words_in_text[word] = 0
            words_in_text[word] += 1

    popular_word = ""
    cnt_popular_word = 0
    for key, val in words_in_text.items():
        if val > cnt_popular_word:
            popular_word = key
            cnt_popular_word = val

    for i in range(len(split_arr)):
        if popular_word in split_arr[i]:
            del split_arr[i]
            break

    return_main_text = revers_separation_by_offers(split_arr)
    return_main_text = to_left_edge(return_main_text)

    return return_main_text

# Функция для выхода из текста
def exit_of_program(main_text):
    print('Вы вышли из программы! До следующего запуска!')
    print('Итоговый текст:')
    return main_text

# Функция для распределения команд
def define_action(num_action):
    commands = {
        0: exit_of_program,
        1: read_text,
        2: del_sentence
    }
    return commands[num_action]