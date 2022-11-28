# 1. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# Решение 1 - встроенная функция в Python

# print(bin(int(input('Please input integer: '))))

# Решение 2
n = int(input('Please input integer: '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f'Binary number: {b}')

