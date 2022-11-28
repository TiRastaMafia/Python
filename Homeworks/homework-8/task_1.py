'''
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        result = '\n'.join(map(str, self.list))
        return result

    def __add__(self, other):
        new_sum = []
        result = []
        
        for i in range(len(self.list)):
            for k in range(len(self.list[i])):
                result.append(self.list[i][k] + other.list[i][k])
            new_sum.append(result)
            result = []
        result = '\n'.join(map(str, new_sum))
        return result


new = Matrix([[2, 3, 4], [3, 4, 1], [0, 2, 3]])
new2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
# print(new.list)
print(f'{new}\n')
print(new2)
print()
print(f'Результат сложения\n{new2 + new}')