"""Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."""

num = 1
res = 0


def func(i, number, sum):
    while i != 0:
        sum += number
        number /= (-2)
        i -= 1
    print(sum)


print('Введите число')
count = int(input("Ввод: "))

func(count, num, res)
