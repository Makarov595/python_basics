from functools import reduce


def proiz(x, y):
    return x * y


def fact(n):
    my_list = []
    for el in range(1, n + 1):
        my_list.append(el)
    yield reduce(proiz, my_list)


i = 0
n = int(input('n = '))

for elem in range(1, n + 1):
    for el in fact(elem):
        print(el)

