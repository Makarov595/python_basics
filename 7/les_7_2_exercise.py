'''
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    sum_tkan = 0

    def __init__(self, name1):
        self.name = name1

    @abstractmethod
    def kol_tkani(self):
        pass


class Palto(Clothes):
    def __init__(self, name1, razmer):
        super().__init__(name1)
        self.razmer = razmer

    @property
    def kol_tkani(self):
        if self.razmer < 30:
            return print('Введите корректное значение')
        else:
            tkan = self.razmer / 6.5 + 0.5
            Clothes.sum_tkan += tkan
            print('{0:.2f}'.format(tkan))


class Kostum(Clothes):
    def __init__(self, name1, rost):
        super().__init__(name1)
        self.rost = rost

    @property
    def kol_tkani(self):
        if self.rost < 100:
            return print('Рост в см! Введите корректное значение')
        else:
            Clothes.sum_tkan += self.rost * 2 + 0.3
            return print(self.rost * 2 + 0.3)


my_palto = Palto('Krutoe', 50)
print(my_palto.name)
my_palto.kol_tkani

my_kostum = Kostum('Modnuy', 180)
print(my_kostum.name)
my_kostum.kol_tkani

print('Общее количество ткани = {0:.2f}'.format(Clothes.sum_tkan))
