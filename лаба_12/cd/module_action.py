from module_tools import *


def exit_of_program(main_text):
    print('Вы вышли из программы! До следующего запуска!')
    print('Итоговый текст:')
    return main_text


def to_left_edge(main_text):
    align, lines = main_text['align'], main_text['text']
    max_len = 0
    for i in range(len(lines)):
        lines[i] = ' '.join(lines[i].split())
        line = lines[i]
        max_len = max(max_len, len(line))

    for i in range(len(lines)):
        lines[i] = lines[i].strip() + ' ' * (max_len - len(lines[i].strip()))

    return_main_text = {
        'align': 0,
        'text': lines
    }
    return return_main_text


def to_right_edge(main_text):
    align, lines = main_text['align'], main_text['text']
    max_len = 0
    for i in range(len(lines)):
        lines[i] = ' '.join(lines[i].split())
        line = lines[i]
        max_len = max(max_len, len(line))

    for i in range(len(lines)):
        lines[i] = ' ' * (max_len - len(lines[i].strip())) + lines[i].strip()

    return_main_text = {
        'align': 1,
        'text': lines
    }
    return return_main_text


def to_by_width(main_text):
    align, lines = main_text['align'], main_text['text']

    max_len = 0
    for i in range(len(lines)):
        lines[i] = ' '.join(lines[i].split())
        line = lines[i]
        max_len = max(max_len, len(line))

    for i in range(len(lines)):
        words = lines[i].split()
        free_spaces = max_len - len(''.join(words))
        if len(words) == 1:
            lines[i] = words[0] + free_spaces * ' '
            continue
        interval = free_spaces // (len(words) - 1)
        remaining_spaces = free_spaces - (interval * (len(words) - 1))
        new_line = words[0]
        for item in words[1:]:
            if remaining_spaces == 0:
                all_interval = interval
            else:
                all_interval = interval + 1
                remaining_spaces -= 1
            new_line = new_line + ' ' * all_interval + item
        lines[i] = new_line

    return_main_text = {
        'align': 2,
        'text': lines
    }
    return return_main_text


def delete_all_words(main_text):
    align, lines = main_text['align'], main_text['text']

    del_word = input("Введите слово, которое будет удаленно: ")
    while len(del_word) == 0:
        print("Вы ввели пустую строку! Повторите попытку")
        del_word = input("Введите слово, которое будет удаленно: ")

    for i in range(len(lines)):
        syllables_sentence = separation_words_spaces(lines[i])
        for q in range(len(syllables_sentence)):
            if syllables_sentence[q].isalpha() and del_word in syllables_sentence[q] and len(del_word) == len(
                    syllables_sentence[q]):
                syllables_sentence[q] = ''

        lines[i] = ''.join(syllables_sentence)

    align_main_text = {
        'align': align,
        'text': lines
    }

    if align == 0:
        return_main_text = to_left_edge(align_main_text)
    elif align == 1:
        return_main_text = to_right_edge(align_main_text)
    else:
        return_main_text = to_by_width(align_main_text)

    return return_main_text


def replace_in_all_text(main_text):
    align, lines = main_text['align'], main_text['text']

    old_word = input("Введите слово, которое будет заменено: ")
    while len(old_word) == 0:
        print("Вы ввели пустую строку! Повторите попытку")
        old_word = input("Введите слово, которое будет заменено: ")

    new_word = input("Введите слово, на которое будет заменено: ")
    while len(new_word) == 0:
        print("Вы ввели пустую строку! Повторите попытку")
        new_word = input("Введите слово, на которое будет заменено: ")

    for i in range(len(lines)):
        syllables_sentence = separation_words_spaces(lines[i])
        for q in range(len(syllables_sentence)):
            if syllables_sentence[q].isalpha() and old_word in syllables_sentence[q] and len(old_word) == len(
                    syllables_sentence[q]):
                syllables_sentence[q] = new_word

        lines[i] = ''.join(syllables_sentence)

    align_main_text = {
        'align': align,
        'text': lines
    }

    if align == 0:
        return_main_text = to_left_edge(align_main_text)
    elif align == 1:
        return_main_text = to_right_edge(align_main_text)
    else:
        return_main_text = to_by_width(align_main_text)

    return return_main_text


def calc_arith(main_text):
    align, lines = main_text['align'], main_text['text']

    for i in range(len(lines)):
        arith_arr = []
        ind_start = -1
        is_expression = False
        q = 0
        while q < len(lines[i]):
            sym = lines[i][q]
            if sym == '-':
                if ind_start == -1:
                    ind_start = q
                arith_arr.append(sym)
            elif sym == '+':
                if ind_start == -1:
                    ind_start = q
                arith_arr.append(sym)
            elif sym.isdigit():
                if ind_start == -1:
                    ind_start = q
                arith_arr.append(sym)
                is_expression = True
            elif sym != " ":
                if is_expression and arith_arr[-1] not in "+-" and sym not in '0123456789':
                    left_shift = len(lines[i][ind_start:q]) - len(lines[i][ind_start:q].strip())
                    new_str = calc_string(arith_arr)
                    lines[i] = lines[i][:ind_start] + new_str + lines[i][q - left_shift:]
                    q = ind_start
                    arith_arr = []
                    ind_start = -1
                    is_expression = False
                else:
                    arith_arr = []
                    ind_start = -1
                    is_expression = False
            if q == len(lines[i]) - 1 and is_expression and arith_arr[-1] not in "+-":
                new_str = calc_string(arith_arr)
                lines[i] = lines[i][:ind_start] + new_str
                q = ind_start
                arith_arr = []
                ind_start = -1
                is_expression = False

            q += 1

    align_main_text = {
        'align': align,
        'text': lines
    }

    if align == 0:
        return_main_text = to_left_edge(align_main_text)
    elif align == 1:
        return_main_text = to_right_edge(align_main_text)
    else:
        return_main_text = to_by_width(align_main_text)

    return return_main_text


def find_and_del(main_text):
    align, lines = main_text['align'], main_text['text']

    cnt_not_len = 0
    for item in lines:
        if len(item) != 0:
            cnt_not_len += 1

    if cnt_not_len == 1:
        print("Нельзя удалить последнее предложение в тексте!")

        align_main_text = {
            'align': align,
            'text': lines
        }

        return align_main_text

    '''
    Код, который переводит из этого:
    lines = [
        '1Папа папа папа',
        'папа. 2Папа папа',
        'папа папа папа. 3Папа.'
    ]
    в это:
    lines_to = [
        ['1Папа', 'папа', 'папа'],
        ['папа', '.' ,'2Папа', 'папа'],
        ['папа', 'папа', '.', '3Папа', '.']
    ]
    '''
    lines_to = []
    for line in lines:
        chunks = []
        current_chunk = ''
        for char in line:
            if char.isdigit() or char.isalpha():
                current_chunk += char
            elif char.isspace() or char in '.!?':
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ''
                if char in '.!?':
                    chunks.append(char)
            elif char in ',;:/(){}[]-':
                if current_chunk:
                    current_chunk += char
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ''
                chunks.append(char)
        if current_chunk:
            chunks.append(current_chunk)
        lines_to.append(chunks)
    lines = lines_to.copy()

    cnt_max = -1
    max_start_offer = {
        "line": -1,
        "ind": -1
    }
    max_end_offer = {
        "line": -1,
        "ind": -1
    }
    is_start_offer = False
    start_offer = {
        "line": 0,
        "ind": 0
    }
    end_offer = {
        "line": -1,
        "ind": -1
    }

    cur_cnt = 0
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            word = line[j]

            if not is_start_offer:
                is_start_offer = True
                start_offer["line"] = i
                start_offer["ind"] = j

            if word not in ".?!":
                if word.isalpha():
                    if check_alternates(word):
                        cur_cnt += 1
            else:
                end_offer["line"] = i
                end_offer["ind"] = j

                if cnt_max < cur_cnt:
                    cnt_max = cur_cnt
                    max_start_offer['line'] = start_offer['line']
                    max_start_offer['ind'] = start_offer['ind']
                    max_end_offer['line'] = end_offer['line']
                    max_end_offer['ind'] = end_offer['ind']

                cur_cnt = 0
                is_start_offer = False

    deleted_offer = ''
    if max_start_offer['line'] == max_end_offer['line']:
        # +1 для удаления точки
        deleted_offer += " ".join(lines[max_start_offer['line']][max_start_offer['ind']:max_end_offer['ind'] + 1])
        lines[max_start_offer['line']] = lines[max_start_offer['line']][:max_start_offer['ind']] \
                                         + lines[max_start_offer['line']][max_end_offer['ind'] + 1:]
    else:
        ind_arr = {}
        q = max_start_offer['line']
        while q <= max_end_offer['line']:
            if q == max_start_offer['line']:
                ind_arr[q] = {
                    "start": max_start_offer['ind'],
                    "end": None
                }
            elif q == max_end_offer['line']:
                ind_arr[q] = {
                    "start": 0,
                    "end": max_end_offer['ind']
                }
            else:
                ind_arr[q] = {
                    "start": 0,
                    "end": None
                }
            q += 1

        for ind_line, arr_borders in ind_arr.items():
            start = arr_borders['start']
            end = arr_borders['end']
            if end is None:
                deleted_offer += " ".join(lines[ind_line][start:])
                deleted_offer += " "
                lines[ind_line] = lines[ind_line][:start]
            else:
                deleted_offer += " ".join(lines[ind_line][start:end])
                deleted_offer += " "
                lines[ind_line] = lines[ind_line][:start] + lines[ind_line][end + 1:]
        deleted_offer += "."

    for mark in '.!?':
        deleted_offer = deleted_offer.replace(f' {mark}', mark)

    print()
    print('Удаленное предложение:')
    print(deleted_offer)

    lines = [line for line in lines if line]

    for z in range(len(lines)):
        line = lines[z]
        line_str = ''
        for item in line:
            line_str += item + " "

        for mark in '.!?':
            line_str = line_str.replace(f' {mark}', mark)

        lines[z] = line_str

    align_main_text = {
        'align': align,
        'text': lines
    }

    if align == 0:
        return_main_text = to_left_edge(align_main_text)
    elif align == 1:
        return_main_text = to_right_edge(align_main_text)
    else:
        return_main_text = to_by_width(align_main_text)

    return return_main_text
