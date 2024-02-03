def input_ends():
    a, b = list(map(float, input("Введите начало и конец отрезка: ").split()))
    return a, b


def input_iter():
    n = int(input("Введите число разбиений: "))
    return n


def left_rectangle_method(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + i * h
        s += f(x)
    return h * s

def print_val(item, a, b):
    print(f"Значение интеграла на [{a} ; {b}] равно {item:.5g}")