"""В программе генерируется случайное целое число от 0 до 100.
 Пользователь должен его отгадать не более чем за 10 попыток.
 После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
 Если за 10 попыток число не отгадано, вывести правильный ответ."""

from random import randrange

try_numb = 10
rand_num = randrange(1, 101)


def func(num_comp, try_num):
    if try_num == 0:
        print(f'Вы не отгадали! Это число {num_comp}')
    else:
        enter_num = int(input('Ввод: '))
        if enter_num > num_comp:
            print('Вы ввели число больше загаданного')
            return func(rand_num, try_num - 1)
        elif enter_num < num_comp:
            print('Вы ввели число меньше загаданного')
            return func(rand_num, try_num - 1)
        else:
            print(f'Вы угадали! Это число {rand_num}')


print('Попробуйте отгадать число и введите свое положительное число от 1 до 100')
func(rand_num, try_numb)
