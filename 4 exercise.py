number = int(input('Введите целое положительное число: '))

max_number = number % 10

while number // 10 > 10:
    if number % 10 > max_number:
        max_number = number % 10
    number = int(number / 10)

print(max_number)
