# 8.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# o	x=34; y=-30 -> 4
# o	x=2; y=4-> 1
# o	x=-34; y=-30 -> 3

def quarter_position(x, y):
    if x > 0 and y > 0:
        quarter = 1
    elif x < 0 and y > 0:
        quarter = 2
    elif x < 0 and y < 0:
        quarter = 3
    else:
        quarter = 4
    return 