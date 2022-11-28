from random import Random, randint

# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит
# от количества элементов в списке) в одной строке одно число.

input_number = int(input('Введите число:\n'))
numbers = []
for i in range(input_number):
    numbers.append(randint(-input_number,input_number + 1))

print(numbers)
print(numbers[1] * numbers[3])

temporary_document = open('file.txt', 'w')
while True:
    position_4_calculate = input(f'Укажите номер индекса от 0 до {input_number - 1}\nлибо exit для выхода:')
    if position_4_calculate == "exit":
        break
    temporary_document.write(position_4_calculate + "\n")
temporary_document.close()

result = 1
temporary_document = open('file.txt', 'r')
for line in temporary_document:
    if line == " ":
        break
    result *= numbers[int(line)]
temporary_document.close()
print(result)