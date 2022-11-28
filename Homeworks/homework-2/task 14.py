# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

input_number = input('Введите вещественное число ')

def summa(input_number):
    if float(input_number) < 0:
        input_number = float(input_number) * (-1)
    number = 0

    for i in str(input_number):
        if i != '.':
            number += int(i)
    return number

print(f'Сумма чисел равна {summa(input_number)}')