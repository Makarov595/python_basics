import itertools

start = int(input('Введите начало для списка целых чисел : '))

for el in itertools.count(start):
    if el > start + 50:
        break
    print(el, end=' ')

my_list = []
while True:
    words = input('\nВведите значение списка, QQQ - выход: ')
    if words.upper() == 'QQQ':
        break
    my_list.append(words)

i = 0
for el in itertools.cycle(my_list):
    i += 1
    if i > 50:
        break
    print(el)
