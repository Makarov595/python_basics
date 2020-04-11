'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
import random
from functools import reduce


# def sum2(x, y):
#     return int(x) + y


summa = 0
with open("text.txt", "w+") as my_file:
    for num in range(random.randint(5, 7)):
        a = random.randint(5, 30)
        print(a, file=my_file, end=' ')
        summa += a

print(summa)

