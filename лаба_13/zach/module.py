# Функция для проверки файла
def file_check(file, status):
    try:
        if status == 'open':
            if file[-4:] == '.txt':
                with open(file, 'r', encoding='CP1251') as file:
                    pass
                return file
            else:
                print('Файл не является текстовым!')
                return None
        if status == 'init':
            if file[-4:] == '.txt':
                with open(file, 'w', encoding='CP1251') as f:
                    f.write('')
                return file
            else:
                print('Файл не текстовый!')
                return None
    except:
        print('Произошла ошибка с файлом! Повторите попытку')
        return None


# Функция для переворацивания файла
def revers_files(file_1, file_2):
    with open(file_1, 'r+', encoding='CP1251') as f1:
        with open(file_2, 'w+', encoding='CP1251') as f2:
            f1.seek(0, 2)
            pos = f1.tell()
            old_line = '/'
            while pos > 0:
                pos -= 1
                f1.seek(pos)
                char = f1.read(1)
                # print(char)
                # print(char == "\n")
                cur_pos = pos
                if char == "\n":
                    line = f1.readline()
                    print(line)
                    if pos != 0 and old_line != line:
                        old_line = line
                        print('я тут')
                        # print(line)
                        # print(line == '\n')
                        f2.write(line.replace('\n', '') + '\n')
                        f1.seek(cur_pos)
                    # if pos == 0 and old_line != line and line != '\n':
                    #     old_line = line
                    #     f2.write(line.replace('\n', ''))
                    #     f1.seek(cur_pos-1)
            else:
                f1.seek(cur_pos)
                line = f1.readline().replace('\n', '')
                f2.write(line)


# Получение длины файла
def get_len(file_2):
    lens_file_2 = []
    with open(file_2, 'r+', encoding='CP1251') as f2:
        lines = f2.readlines()
        for line in lines:
            lens_file_2.append(len(line))
    lens_file_2 = lens_file_2[::-1]

    return lens_file_2
