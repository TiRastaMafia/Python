"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_dick = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __str__(self):
        return f'Имя и фамилия сотрудника: {self.name} {self.surname}'

    def get_full_name(self):
        return (f'Имя и фамилия сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        income = self._income_dick['wage'] + self._income_dick['bonus']
        return f'Доход: {income}'


obj_position = Position('Sergey', 'Ivanov', 'Manager', 15000, 7000)
print(obj_position._income_dick)
print(f'Должность: {obj_position.position}')
print(obj_position.__str__())
print(obj_position.get_full_name())
print(obj_position.get_total_income())

print()

obj_2_position = Position('Vasiliy', 'Petrov', 'Director', 30000, 27000)
print(obj_2_position._income_dick)
print(f'Должность: {obj_2_position.position}')
print(obj_2_position.__str__())
print(obj_2_position.get_full_name())
print(obj_2_position.get_total_income())