# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2


def the_product_of_prime_numbers(number):
	input_number = number
	i = 2
	result_list = []

	while i <= number:
		if number % i == 0:
			result_list.append(i)
			number //= i
		else:
			i += 1
	print(f"Простые множители числа {input_number} приведены в списке: {result_list}")

the_product_of_prime_numbers(int(input('Введите число  ')))