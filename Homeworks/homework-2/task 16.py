# Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

input_lenght = int(input('Введите количество чисел в списке:\n'))

def numbers(input_lenght):
    summ = 0
    for i in range(input_lenght):
        input_number = int(input(f'Введите число № {i + 1}:\n'))
        input_number = (1+1/input_number)**input_number
        summ = input_number + summ
        i += 1
    return summ

print('Сумма чисел равна:',round((numbers(input_lenght)), 2))