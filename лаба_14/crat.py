import os
import struct as s

f = open('football.bin', "rb+")
with open('football.txt', encoding='utf-8') as g:
    form = [f'>20s', f'>i', f'>12s', f'>3s']
    first_occurrence = True
    for l in g:
        if first_occurrence:
            first_occurrence = False
            continue
        line = l.split(";")
        for i in range(len(line)):
            if 'i' in form[i]:
                f.write(s.pack(form[i], int(line[i])))
            else:
                f.write(s.pack(form[i], line[i].replace('\n', '').encode('CP1251')))

f.close()

# f.write(s.pack(f'>20s', 'Бэкхем'.encode('CP1251')))
# f.write(s.pack(f'>i', 46))
# f.write(s.pack(f'>12s', 'Полузащитник'.encode('CP1251')))
# f.write(s.pack(f'>3s', 'Да'.encode('CP1251')))

print(os.path.getsize('football.bin'))
