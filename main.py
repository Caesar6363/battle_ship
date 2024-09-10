from colorama import Fore


class CheckWinException(Exception):
    pass


ships = {}

def name_player() -> str:
    name = input(f'{Fore.CYAN}Введите имя  игрока: ')
    ships[name] = {}
    return name


def indentation():
    print("\n" * 20)


def play_board(name):

    print('      0  ', '1  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  ', '8  ', '9  ')
    print('   ', '_' * 41)

    for row_num in range(0, 10):
        print(f'{row_num}', end='   ')
        for j in range(0, 10):
            cell = ships[name].get((row_num, j), ' ')
            print(f'| {cell}', end=' ')
        print("|\n" + '   ', '_' * 41)


def create_ships(name: str) -> None:   # Ставим корабль

    step = 0
    while step <= 21:
        print(f'Игрок {name} выставляет корабли')
        change_ships(name, "▄")
        step += 1
        play_board(name)


def player_turn(attacker: str, defender: str) -> None:  # Выстрел
    while True:
        print(f'Ход {attacker}')
        x = int(input(f'Выберете строку: '))
        y = int(input(f'Выберете столбец: '))

        if int(x) in range(0, 10) and int(y) in range(0, 10):

            if (x, y) in ships[defender] and ships[defender][(x, y)] == '▄':
                ships[defender][(x, y)] = 'Х'
                ships[attacker][(x, y)] = 'Х'
                play_board(attacker)
                print('Попал')
                return player_turn(attacker, defender)

            else:
                ships[defender][(x, y)] = '☼'
                ships[attacker][(x, y)] = '☼'
                play_board(attacker)
                indentation()
                print(f'Промах')
                break


        print('Неверные координаты')



def check_win(player: str):  # Проверка победы

    if "▄" not in ships[player].values():
        raise CheckWinException


def change_ships(player: str, new_symbol: str):  # Проверка на правильность постановки кораблей
    while True:
        create_ships_line = int(input(f'Выберете строку: '))
        create_ships_colum = int(input(f'Выберете столбец: '))


        if (int(create_ships_line) in range(0, 10) and int(create_ships_colum) in range(0, 10) and
                ships[player].get((create_ships_line, create_ships_colum)) is None):
            ships[player][(create_ships_line, create_ships_colum)] = new_symbol
            break
        else:
            print('Место занято или вы ввели некорректные координаты')


def main():
    name1 = name_player()  # имена игроков
    name2 = name_player()


    play_board(name1)
    create_ships(name1)



    play_board(name2)
    create_ships(name2)
    indentation()

    while True:
        player_turn(name1, name2)
        try:
            check_win(name2)
        except CheckWinException:
            print(f'Победитель - {name1}')
            print(f' {name2} проиграл')
            break

        player_turn(name2, name1)
        try:
            check_win(name1)
        except CheckWinException:
            print(f'Победитель - {name2}')
            print(f' {name1} проиграл')
            break


main()


