import random

my_list = [random.randint(1, 50) for el in range(random.randint(1, 50))]
print(my_list)

new_list = [my_list[el] for el in range(1, len(my_list) - 1) if my_list[el] > my_list[el - 1]]
print(new_list)
