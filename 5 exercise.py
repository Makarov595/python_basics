vir = float(input('Введите значение выручки: '))
izder = float(input('Введите значение издержек: '))

rez = vir - izder

if rez == 0:
    print('Фирма работает в ноль')
elif rez > 0:
    print('Фирма работает с прибылью:', vir-izder)
else:
    print('Фирма работает с убытками:', izder-vir)

