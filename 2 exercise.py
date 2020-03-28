time_sec = int(input('Введите время в секундах, (сек.): '))

hour = time_sec // 3600
if 10 > hour > 0:
    hour = '0' + str(hour)

kol_min = (time_sec - int(hour) * 3600) // 60
if 10 > kol_min > 0:
    kol_min = '0' + str(kol_min)

sec = (time_sec - int(hour) * 3600 - int(kol_min) * 60)
if 10 > sec > 0:
    sec = '0' + str(sec)

print(f'Введенное время в формате "чч:мм:сс": {hour}:{kol_min}:{sec}')
