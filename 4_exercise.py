stroka = input('Введите строку из нескольких слов, разделенных пробелами: ')
my_list = stroka.split()

for nomer, el in enumerate(my_list, 1):
    if len(el) < 10:
        print(nomer, el)
    else:
        print(nomer, el[1:10])

