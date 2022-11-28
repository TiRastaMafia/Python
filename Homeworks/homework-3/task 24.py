# 24. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# решение № 1

# new_list = [1.33, 1.2, 3.1, 5, 10.01]
# new_list = [round(i % 1, 2) for i in new_list if i % 1 != 0]
# print(max(new_list) - min(new_list))

# решение № 2


elements = [1.61, 1.32, 3.1, 5, 10.01]
min = 1
max = 0

def fractional_output(list):  # функция извлекает дробную часть и создает новый список
    lst2 = []
    for i in range(len(list)):
        res = round((list[i] % 1), 2)
        lst2.append(res)
    return lst2

new_list = fractional_output(elements)

for i in new_list:
    if i != 0:
        if i < min:
          min = i
        if i  >= max:
            max = i

print(max)
print(min)
print(round(max - min,2))