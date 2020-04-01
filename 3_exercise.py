num_month = int(input('Nomber of month: '))

my_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}

for keys, value in my_dict.items():
    if num_month in value:
        print(keys)

my_list = [['winter', 1, 2, 12], ['spring', 3, 4, 5], ['summer', 6, 7, 8], ['autumn', 9, 10, 11]]

for el in my_list:
    if num_month in el:
        print(el[0])


