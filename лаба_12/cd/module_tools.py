def input_command():
    print("Выберите команду: ", end="")
    command = input()

    try:
        corr_command = int(command)
    except:
        print("Введены некорректные данные! Повторите попытку\n")
        corr_command = input_command()

    return corr_command


def print_text(main_text):
    align, lines = main_text['align'], main_text["text"]
    width = 0
    for line in lines:
        width = max(len(line), width)

    print()
    print('+' + '-' * width + '+')
    for line in lines:
        print('|' + line + '|')
    print('+' + '-' * width + '+')
    print()


def separation_words_spaces(line):
    arr = []
    word = ''
    for symbol in line:
        if not symbol.isalpha():
            if word:
                arr.append(word)
                word = ''
            arr.append(symbol)
        else:
            word += symbol
    if word:
        arr.append(word)
    print(arr)
    return arr


def calc_string(arr):
    use_array = ''.join(arr)
    i = 0
    while i < len(use_array) - 1:
        if use_array[i].isdigit() and not use_array[i + 1].isdigit():
            use_array = use_array[:i + 1] + "!+!" + use_array[i + 1:]
            i += 3
        i += 1

    use_array = use_array.split('!+!')

    val = 0
    for num in use_array:
        if num == '':
            continue
        elif num.count("+") + num.count("-") >= 2:
            if num.count("-") % 2 == 0:
                val += int(num.replace("-", "").replace("+", ""))
            else:
                val += -int(num.replace("-", "").replace("+", ""))
        else:
            val += int(num.replace("+", ""))

    return str(val)



