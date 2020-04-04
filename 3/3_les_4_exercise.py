def my_func_1(x, y):
    return x**y


def my_func_2(x, y, i=0, rez=1):
    while i < abs(y):
        rez = rez * x
        i += 1
    if y < 0:
        return 1 / rez
    else:
        return rez


try:
    num_1 = float(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
except ValueError:
    print('Введено неккореное значение!')
else:
    print('Результат с использованием первой функции: ', my_func_1(num_1, num_2))
    print('Результат с использованием второй функции: ', my_func_2(num_1, num_2))
