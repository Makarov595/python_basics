'''
3 Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, dict_class):
        self.name = dict_class['name']
        self.surname = dict_class['surname']
        self.position = dict_class['position']
        try:
            self._income = int(dict_class['wage']) + int(dict_class['bonus'])
        except ValueError:
            self._income = int(dict_class['wage'])


class Position(Worker):
    def __init__(self, dict_class):
        super().__init__(dict_class)

    def get_full_name(self):
        print('Full Name:', self.name, self.surname)

    def get_total_income(self):
        print('Income : ', self._income, '\n')


my_dict_1 = {'surname': 'Ivanov', 'name': 'Vasilii', 'position': 'Engineer', 'wage': '104', 'bonus': '140'}
my_dict_2 = {'surname': 'Sidorov', 'name': 'Ivan', 'position': 'Engineer', 'wage': '105', 'bonus': '150'}
my_dict_3 = {'surname': 'Glavnii', 'name': 'Personash', 'position': 'Director', 'wage': '312', 'bonus': '320'}
my_dict_4 = {'surname': 'Ogorodnikov', 'name': 'Stepan', 'position': 'Technician', 'wage': '70', 'bonus': '-'}

pers_1 = Position(my_dict_1)
pers_2 = Position(my_dict_2)
pers_3 = Position(my_dict_3)
pers_4 = Position(my_dict_4)


pers_1.get_full_name()
pers_1.get_total_income()

pers_2.get_full_name()
pers_2.get_total_income()

pers_3.get_full_name()
pers_3.get_total_income()

pers_4.get_full_name()
pers_4.get_total_income()
