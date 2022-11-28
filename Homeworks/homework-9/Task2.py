"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""

class Road:
    weight = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_asphalt_mass(self):
        result = (self._length * self._width * self.weight * self.thickness) / 1000
        print(f'Необходимая масса асфальта {round(result, 2)} т')

# obj_road = Road(5000, 20)
# obj_road.calculation_asphalt_mass()