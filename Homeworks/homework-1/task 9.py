# 9.	Напишите программу, которая по заданному 
# номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def input_numbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def check_number(inputText):
    if inputText < 1 or inputText > 4:
        print('Please, repeat the input')
    elif inputText == 1:
        print('x > 0 and y > 0')
    elif inputText == 2:
        print('x < 0 and y > 0')
    elif inputText == 3:
        print('x < 0 and y < 0')
    elif inputText == 4:
        print('x > 0 and y < 0')

num = input_numbers("Введите число: ")
check_number(num)