#  Задача 6.
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:# o	6 -> да;  o	7 -> да;  o	1 -> нет.

# def define_the_day(day):
#     input_day = int(input('Enter day number: '))
#     if input_day > 7 or input_day < 1:
#         print('Введите число от 1 до 7')
#     elif input_day == 6 or input_day == 7:
#         print("it's weekend!")
#     else:
#         print("No, it's not weekend")
# define_the_day(0)

# ______________________________________________  ЛИБО __________________________________________
# С проверкой на число

def input_numbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(input_day):
    if input_day > 7 or input_day < 1:
        print('Введите число от 1 до 7')
    elif input_day == 6 or input_day == 7:
        print("it's weekend!")
    else:
        print("No, it's not weekend")

num = input_numbers("Введите число: ")
checkNumber(num)