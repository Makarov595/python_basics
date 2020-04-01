my_list = [7, 5, 3, 3, 2]
print(my_list)
my_list.reverse()

dlin = len(my_list)
i = 0

znach = input('Введите элемент для внесения в рейтинг: ')

while len(my_list) == dlin:

    if int(znach) <= my_list[i]:
        my_list.insert(i, int(znach))
        break

    else:
        i += 1

        if i + 1 == dlin:
            my_list.insert(i + 1, int(znach))

my_list.reverse()
print(my_list)
