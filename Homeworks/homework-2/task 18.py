from random import Random, randint
# Реализуйте алгоритм перемешивания списка

input_number = int(input('Введите количество элементов '))
numbers = []
for i in range(input_number):
    numbers.append(randint(-input_number,input_number+1))
print(numbers)

def shaffle(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(shaffle(numbers))