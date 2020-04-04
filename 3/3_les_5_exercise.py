def my_func(stroka_num, rez=0):
    my_list = stroka_num.split()

    for el in my_list:
        if el.upper() == 'Q':
            break
        rez += int(el)
    return rez


sum_num = 0

while True:
    stroka = input('Введите строку чисел, разделенных пробелом (для выхода введите Q): \n')
    if stroka[0].upper().count('Q') != 0:
        print('До свидания')
        break
    sum_num += my_func(stroka)
    print('Сумма введенных чисел равна: ', sum_num)
    if stroka.upper().count('Q') != 0:
        break
