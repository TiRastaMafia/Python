# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

input_number = int(input('Введите число '))

result = 1 # так как при умножении на 0 будет всегда ноль
for i in range(input_number):
    i = i + 1
    result = i * result

    print(result, end=" ")