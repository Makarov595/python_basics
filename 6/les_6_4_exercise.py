'''
4 Реализуйте базовый класс Car. +
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).+
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, d_speed=0, d_color='White', d_name=None, d_is_police=False):
        self.speed = d_speed
        self.color = d_color
        self.name = d_name
        self.is_police = d_is_police

    def go(self):
        print('Машина', self.name, 'поехала')

    def stop(self):
        print('Машина', self.name, ' остановилась')

    def turn(self, direction):
        print('Машина', self.name, ' повернула на', direction)

    def show_speed(self):
        print('Текущая скорость', self.name, '=', self.speed, '\n')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости! ограничение 60')
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости! ограничение 40')
        super().show_speed()


class PoliceCar(Car):
    pass


my_car = Car(80, 'Blue', 'Porshe', False)
my_town_car = TownCar(65, 'Black', 'Reno', False)
not_my_sport_car = SportCar(200, 'Golden', 'F1', False)
my_work_car = WorkCar(d_speed=45, d_name='Horse')
polise_car = PoliceCar(60, 'White-Blue', 'KIA', True)

my_car.go()
my_town_car.go()
not_my_sport_car.go()
my_work_car.go()
polise_car.go()

my_car.show_speed()
my_town_car.show_speed()
not_my_sport_car.show_speed()
my_work_car.show_speed()
polise_car.show_speed()

polise_car.turn('left')
polise_car.turn('reno car')
my_town_car.stop()
polise_car.stop()

