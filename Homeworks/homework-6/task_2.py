''' Напишите программу, которая принимает на вход вещественное число и показывает
сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
'''


print('Enter the value: ')
value = input()

# old code
# def sum_of_numbers(number):
#     sum = 0
#     for value in number:
#         if value.isdigit():
#             sum+=int(value)
#     print(round(sum))


# sum_of_numbers(user_number)

# new code
lst = [int(x) for x in value if x.isdigit()]

print('The sum of the elements is', sum(lst))