""". Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

count = 0


def func(num, search):
    global count
    if num != 0:
        if num % 10 == search:
            count += 1
        return func(num // 10, search)
    return count


print('Введите числа.')
enter_num = int(input('Ввод: '))
print('Какую цифру вы хотите посчитать в последователньости?')
search_num = int(input('Ввод: '))

ret = func(enter_num, search_num)
print(f'Цифра {search_num} встречается {ret} раз(a)')
