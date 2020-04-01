my_list = []
el = ''

while el != 's':
    el = input('Введите емемент списка, для выхода напишите "stop": ')
    if el != 's':
        my_list.append(el)
    else:
        if my_list == []:
            print('Вы не ввели ни одного значения')
        else:
            break

if my_list != []:
    print(my_list)

i = 0
while i < len(my_list) - 1:
    perem = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = perem
    i += 2

if my_list != []:
    print(my_list)
