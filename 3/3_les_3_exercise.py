def my_func(list):
    max_1 = max(list)
    list.remove(max_1)
    max_2 = max(list)
    return max_1, max_2


def int_float(argum):
    try:
        arg = int(argum)
        return arg
    except ValueError:
        try:
            arg = float(argum)
            return arg
        except ValueError:
            arg = 'Введено не число!'
            return arg


arg_1 = ''
my_list = []

while True:
    rez_func = ''

    while type(rez_func) == str:
        arg_1 = input('Введите число для определения суммы наибольших двух, выход - Q: \n')
        rez_func = int_float(arg_1)
        if type(rez_func) != str or arg_1.upper() == 'Q':
            break
        else:
            print('Введено некоррекное число (не число),')

    if arg_1.upper() == 'Q':
        break
    my_list.append(rez_func)
    print('Ваши значения: ', my_list)

print('\n \nВаши  итоговые значения:\n', my_list)

if len(my_list) > 1:
    my_tuple = my_func(my_list)
    print(f'\n \nМаксимальные значения: \n {my_tuple[0]}, {my_tuple[1]}\nсумма которых равна = {sum(my_tuple)}')
else:
    print('До свидания')

