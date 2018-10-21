#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

# Делал, сверяясь с чужим форком. Создание карточки сделал своим способом.
import random


def make_card():
    """
    Makes a card
    """
    card = [[], [], []]

    for line in card:
        for _ in range(9):
            line.append(' ')

    numbers = random.sample(range(1, 91), 15)
    n = 5
    m = 0
    for line in card:
        numbers_pos = random.sample(range(9), 5)
        for i, el in enumerate(numbers_pos):
            line[el] = numbers[m:n][i]
        n += 5
        m += 5
    return card


def print_card(card):
    """
    Prints a card in an appropriate format
    """
    for line in card:
        for el in line:
            print('{:>2}'.format(el), end=' ')
        print('\n')


def cross_out(card, keg):
    """
    Crosses out a number if it's in a card. Also checks for correct player decision.
    """
    for line in card:
        for i, el in enumerate(line):
            if el == keg:
                line[i] = '-'
                return True
    return False


def check_card(card):
    """
    Checks whether there's still numbers in a card.
    """
    for line in card:
        for el in line:
            if type(el) == int:
                return False
    return True


# player_card = [[1, 2, 3, 4, 5, '', '', '', ''], [6, 7, 8, 9, 10, '', '', '', '']
# [11, 12, 13, 14, 15, '', '', '', '']]
player_card = make_card()
comp_card = make_card()

kegs = random.sample(range(1, 91), 90)

print("Добро пожаловать в игру лото")
for n, keg in enumerate(kegs):
    print("Новый бочонок: {}. Осталось бочонков: {}.".format(keg, len(kegs) - n - 1))
    print("------ Ваша карточка -----")
    print_card(player_card)
    print("--------------------------")
    print("-- Карточка компьютера ---")
    print_card(comp_card)
    print("--------------------------")

    while True:
        answer = input("Зачеркнуть бочонок? Выйти? y/n/q: ")
        if answer == 'q':
            print("Игра закончена.")
            exit()
        elif answer == 'y':
            if not cross_out(player_card, keg):
                print("Такого бочонка в карточке нет. Вы проиграли.")
                exit()
            break
        elif answer == 'n':
            if cross_out(player_card, keg):
                print("Такой бочонок в карточке есть. Вы проиграли.")
                exit()
            break
        else:
            print("Неправильный ввод")
            
    cross_out(comp_card, keg)
    if check_card(player_card) and check_card(comp_card):
        print("Ничья.")
    elif check_card(player_card):
        print("Вы зачеркнули все цифры. Победа!")
    elif check_card(comp_card):
        print("Компьютер зачеркул все цифры. Поражение!")
