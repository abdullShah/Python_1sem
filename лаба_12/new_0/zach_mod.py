# разделение по предложениям
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


main_text = [
    '1Папаааааа. 2Паа',
    'паа. 3Ппаа. 4Па.'
]

print(main_text)
print(separation_by_offers(main_text))
print(revers_separation_by_offers(separation_by_offers(main_text)))
