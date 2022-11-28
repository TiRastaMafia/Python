# № 1) Напишите программу, удаляющую из текста все слова, содержащие "абв".

def Delete_words(s):
    return False if part in s else True


print('Введите текст в котором нужно искать: ')
input_text = input()

print('Введите текст который нужно искать: ')
part = input()

input_text = input_text.split()

input_text = list(filter(Delete_words, input_text))
print(f'в этих словах не содержится заданный ключ ->', " ".join(input_text))