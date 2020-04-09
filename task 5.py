"""Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число."""

res_first = 0
count = 1


def func(num):
    global res_first
    global count
    res_second = num * (num + 1) / 2
    while num != 0:
        res_first += count
        count += 1
        num -= 1
    if res_first == res_second:
        print('Они равны')
    else:
        print("Они не равны")


print('Введите натуральное число.')
enter_num = int(input('Ввод: '))
func(enter_num)
