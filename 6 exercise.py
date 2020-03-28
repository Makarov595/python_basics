a_km_first_day = float(input('Введите результат спортсмена в первый день, км.: '))
b_km_last_day = float(input('Введите необходимый результат спортсмена, км.: '))

i = 1
while a_km_first_day < b_km_last_day:
    i += 1
    a_km_first_day *= 1.1
print (i)