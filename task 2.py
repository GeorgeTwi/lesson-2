"""Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

even = 0
not_even = 0

print("Введите четные и нечетные цифры натуральных чисел.")
num = int(input('Ввод: '))


def func(a):
    global even
    global not_even
    if a != 0:
        res = a % 10
        if res % 2 == 0:
            even += 1
        elif res % 2 != 0:
            not_even += 1
        return func(a // 10)
    else:
        print(f'Кол-во четных: {even}, Кол-во нечетных {not_even}')


func(num)

