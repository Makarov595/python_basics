def int_func(my_str):
    if 123 > ord(my_str[0]) > 96 or 1103 > ord(my_str[0]) > 1072:
        s = chr(ord(my_str[0]) - 32)
        my_str = s + my_str[1:]
    return my_str


rez = ''
my_str_1 = input('Введите фразу: ')
my_list = my_str_1.split()

for el in my_list:
    rez = rez  + int_func(el) + ' '

print(rez)