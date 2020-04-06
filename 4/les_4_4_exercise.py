import random

my_list = [random.randint(1, 25) for el in range(random.randint(1, 50))]
print(my_list)
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
