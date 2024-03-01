from random import *


def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    return False


def input_n():
    while True:
        n = input('Введите число: ')
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            return n


x = randint(1, 100)
print('Добро пожаловать в числовую угадайку')
play = True
while play:
    attempt = 0

    guess = input_n()
    while int(guess) != x:
        if int(guess) < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Ваше число больше загаданного, попробуйте еще разок')
        guess = input_n()
        attempt += 1
    print(f'Вы угадали за {attempt} попыток, поздравляем!')
    print('Спасибо, что играли в числовую угадайку.')
    quest = input('Если хотите сыграть еще раз, скажите да: ')
    if quest.lower() != 'да' and quest.lower() != 'yes':
        play = False
    x = randint(1, 100)
