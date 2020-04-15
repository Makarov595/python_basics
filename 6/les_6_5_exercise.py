'''
5 Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки..')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой..')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом..')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером..')


insrtrument_1 = Stationery('ruler')
insrtrument_2 = Pen('Parker')
insrtrument_3 = Pencil('KOH-I-NOOR')
insrtrument_4 = Handle('Marker')

insrtrument_1.draw()
insrtrument_2.draw()
insrtrument_3.draw()
insrtrument_4.draw()
