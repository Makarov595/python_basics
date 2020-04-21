"""== Лото ==

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
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.sum_num = 0
        ticket = [['__', '__', '__', '__', '__', '__', '__', '__', '__'],
                  ['__', '__', '__', '__', '__', '__', '__', '__', '__'],
                  ['__', '__', '__', '__', '__', '__', '__', '__', '__']]
        list_for_nums = self.form_list(91)

        for _ in range(3):
            list_for_lines = self.form_list(9, 0)

            for __ in range(5):
                a = list_for_lines[random.randint(0, len(list_for_lines) - 1)]
                b = list_for_nums[random.randint(0, len(list_for_nums) - 1)]
                ticket[_][a] = b
                list_for_lines.remove(a)
                list_for_nums.remove(b)

        self.ticket = ticket

    def __str__(self):
        print()
        return '\n'.join(['  '.join([str(el) for el in elem]) for elem in self.ticket])

    def cross_it_out(self, nomer2):
        for i, el in enumerate(self.ticket):
            if nomer2 in el:
                self.ticket[i].insert(self.ticket[i].index(nomer2), '__')
                self.ticket[i].pop(self.ticket[i].index(nomer2))

    def n_in(self, nomer):
        for i, el in enumerate(self.ticket):
            if nomer in el:
                return True
        return False

    @staticmethod
    def form_list(quantity, start=1):
        my_list = [i for i in range(start, quantity)]
        return my_list


class Game:
    def __init__(self, play_1, play_2):
        self.nums = Player.form_list(91)
        self.play_1 = play_1
        self.play_2 = play_2

    def start(self):
        while True:
            next_keg = random.choice(self.nums)
            print('Новый бочонок :', next_keg, '(осталось', len(self.nums) - 1, ')\n')
            print('--------- Ваша карточка: ---------', self.play_1, '\n')
            print('------ Карточка компьютера: ------', self.play_2, '\n')
            answer = input('Зачеркнуть цифру? (Y/N) выход - Q').upper()

            if answer == 'Y' and not self.play_1.n_in(next_keg) or answer == 'N' and self.play_1.n_in(next_keg):
                print('Вы проиграли, номер:', next_keg, 'есть в вашей карточке!') if answer == 'N' else print('No')
                break

            elif answer == 'N' and not self.play_1.n_in(next_keg):
                print('Действительно нет такого номера! Играем дальше!!')

            elif answer == 'Y' and self.play_1.n_in(next_keg):
                print('Внимательный вы игрок! Вычеркиваем', next_keg)
                self.play_1.cross_it_out(next_keg)
                self.play_1.sum_num += 1

            else:
                print('фара какая то')

            if self.play_2.n_in(next_keg):
                self.play_2.cross_it_out(next_keg)
                self.play_2.sum_num += 1

            if self.play_1.sum_num == 15:
                print('Выиграл игрок!')
                break

            if self.play_2.sum_num == 15:
                print('Выиграл компьютер!')
                break

            if answer == 'Q':
                break

            self.nums.remove(next_keg)


player_1 = Player('Player_1')
comp_player = Player('Computer')

game = Game(player_1, comp_player)
game.start()
