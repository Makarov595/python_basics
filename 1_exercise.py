my_list = [None, 15, 58.58, 'stroka', [35, 58, 88], ('tuple_1', 'example'), {1, 2, 3}, {'dict_1': 5}]

for elem in my_list:
    print(type(elem))

nomer = int(input('Введите номер, проверку типа которого осущетсвляем: '))
print(type(my_list[nomer])) # не понтяно условие задачи, сделал в двух вариантах