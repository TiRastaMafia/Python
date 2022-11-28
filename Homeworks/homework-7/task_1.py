"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time


class traffic_light():
    # Определение атрибутов класса

# задаем цвета светофора
    red_light_name = 'Красный'
    yellow_light_name = 'Желтый'
    green_light_name = 'Зеленый'

    # задаем время горения сигналов светофора
    red_glow_time = 3
    yellow_glow_time = 1
    green_glow_time = 2

# Определение методов класса
    def __init__(self, color):
        self._color = color
        print(f'\nСоздан новый объект TrafficLight с именем {self._color}')

    def switch_light(self, color, glow_time):
        self.glow_time = glow_time
        print(f'Включен {color} свет на время {self.glow_time} сек')
        time.sleep(self.glow_time)

    def running(self, color=''):

        # Если при вызове метода цвет не указан, берем из родительского класса
        # В противном случае стартуем с цвета, объявленного при вызове метода

        if not color:
            loc_color = self._color
        else:
            loc_color = color
        if loc_color == self.red_light_name:
            self.switch_light('Красный', self.red_glow_time)
            self.switch_light('Желтый', self.yellow_glow_time)
            self.switch_light('Зеленый', self.green_glow_time)
        elif loc_color == self.yellow_light_name:
            self.switch_light('Желтый', self.yellow_glow_time)
            self.switch_light('Зеленый', self.green_glow_time)
        elif loc_color == self.green_light_name:
            self.switch_light('Зеленый', self.green_glow_time)

        else:
            print('Введите Красный, Желтый или Зеленый')


# Инициализируем класс, а метод запускаем с другого цвета
tl1 = traffic_light('Красный')
tl1.running()

tl1 = traffic_light('Красный')
tl1.running('Красный')

tl1 = traffic_light('Старт!')
tl1.running('Зеленый')