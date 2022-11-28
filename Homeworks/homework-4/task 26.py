# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_list = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_list.insert(0, a)
        a, b = b, a - b
    return fibo_list

fibo_list = get_fibonacci(n)
print(get_fibonacci(n))