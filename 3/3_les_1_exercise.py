def delenie(arg_1, arg_2):
    rezult = arg_1 / arg_2
    if arg_1 * 10 % 10 == 0 and arg_2 * 10 % 10 == 0:
        print(f'Результат деления {arg_1:.0f} на {arg_2:.0f} = {rezult}')
    elif arg_1 * 10 % 10 == 0:
        print(f'Результат деления {arg_1:.0f} на {arg_2} = {rezult}')
    elif arg_2 * 10 % 10 == 0:
        print(f'Результат деления {arg_1} на {arg_2:.0f} = {rezult}')
    else:
        print(f'Результат деления {arg_1} на {arg_2} = {rezult}')
    return rezult


try:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    rez = delenie(num_1, num_2)
except ValueError:
    print('Введено не число!')
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
