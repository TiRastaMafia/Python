# 	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input('input x:\n'))
# y = int(input('input y:\n'))
# if x > 0 and y > 0:
#     text = 1
# if x < 0 and y > 0:
#     text = 2
# if x < 0 and y < 0:
#     text = 3
# if x > 0 and y < 0:
#     text = 4
# print(f"Точка находится в {text} четверти плоскости")

# ______________________________  ЛИБО ______________________________________________

def input_koord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координата не должна быть равна 0 ")
            except ValueError:
                print("Надо ввести числа!")
    return a

def check_Coordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")

koordinate = input_koord(2)
check_Coordinates(koordinate)