import random as rd


Table = '\n   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'
choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
user_wins = 0
comp_wins = 0


def table():
    print(Table)


def index_convertor(pos):
    key = {1: 2, 2: 6, 3: 10,
           4: 26, 5: 30, 6: 34,
           7: 50, 8: 54, 9: 58}
    ans = key[int(pos)]
    return ans


def comp_pos(tab):
    while True:
        key = {2: 1, 6: 2, 10: 3,
               26: 4, 30: 5, 34: 6,
               50: 7, 54: 8, 58: 9}
        comp_placement = 0
        # Check if the user is currently winning
        if tab[2] == tab[6] and tab[2] == 'X':
            comp_placement = 10
        elif tab[10] == tab[6] and tab[10] == 'X':
            comp_placement = 2
        elif tab[2] == tab[10] and tab[2] == 'X':
            comp_placement = 6
        elif tab[30] == tab[26] and tab[26] == 'X':
            comp_placement = 34
        elif tab[26] == tab[34] and tab[26] == 'X':
            comp_placement = 30
        elif tab[30] == tab[34] and tab[30] == 'X':
            comp_placement = 26
        elif tab[50] == tab[54] and tab[50] == 'X':
            comp_placement = 58
        elif tab[54] == tab[58] and tab[54] == 'X':
            comp_placement = 50
        elif tab[50] == tab[58] and tab[50] == 'X':
            comp_placement = 54
        elif tab[2] == tab[26] and tab[2] == 'X':
            comp_placement = 50
        elif tab[26] == tab[50] and tab[26] == 'X':
            comp_placement = 2
        elif tab[50] == tab[2] and tab[50] == 'X':
            comp_placement = 50
        elif tab[10] == tab[34] and tab[10] == 'X':
            comp_placement = 58
        elif tab[34] == tab[58] and tab[34] == 'X':
            comp_placement = 10
        elif tab[58] == tab[10] and tab[58] == 'X':
            comp_placement = 34
        elif tab[6] == tab[30] and tab[6] == 'X':
            comp_placement = 54
        elif tab[30] == tab[54] and tab[30] == 'X':
            comp_placement = 6
        elif tab[54] == tab[6] and tab[54] == 'X':
            comp_placement = 30
        elif tab[2] == tab[30] and tab[2] == 'X':
            comp_placement = 58
        elif tab[30] == tab[58] and tab[30] == 'X':
            comp_placement = 2
        elif tab[58] == tab[2] and tab[58] == 'X':
            comp_placement = 30
        elif tab[10] == tab[30] and tab[10] == 'X':
            comp_placement = 50
        elif tab[30] == tab[50] and tab[30] == 'X':
            comp_placement = 10
        elif tab[50] == tab[10] and tab[50] == 'X':
            comp_placement = 30

        # To check if the computer is currently winning
        elif tab[2] == tab[6] and tab[2] == 'O':
            comp_placement = 10
        elif tab[10] == tab[6] and tab[10] == 'O':
            comp_placement = 2
        elif tab[2] == tab[10] and tab[2] == 'O':
            comp_placement = 6
        elif tab[30] == tab[26] and tab[26] == 'O':
            comp_placement = 34
        elif tab[26] == tab[34] and tab[26] == 'O':
            comp_placement = 30
        elif tab[30] == tab[34] and tab[30] == 'O':
            comp_placement = 26
        elif tab[50] == tab[54] and tab[50] == 'O':
            comp_placement = 58
        elif tab[54] == tab[58] and tab[54] == 'O':
            comp_placement = 50
        elif tab[50] == tab[58] and tab[50] == 'O':
            comp_placement = 54
        elif tab[2] == tab[26] and tab[2] == 'O':
            comp_placement = 50
        elif tab[26] == tab[50] and tab[26] == 'O':
            comp_placement = 2
        elif tab[50] == tab[2] and tab[50] == 'O':
            comp_placement = 50
        elif tab[10] == tab[34] and tab[10] == 'O':
            comp_placement = 58
        elif tab[34] == tab[58] and tab[34] == 'O':
            comp_placement = 10
        elif tab[58] == tab[10] and tab[58] == 'O':
            comp_placement = 34
        elif tab[6] == tab[30] and tab[6] == 'O':
            comp_placement = 54
        elif tab[30] == tab[54] and tab[30] == 'O':
            comp_placement = 6
        elif tab[54] == tab[6] and tab[54] == 'O':
            comp_placement = 30
        elif tab[2] == tab[30] and tab[2] == 'O':
            comp_placement = 10
        elif tab[30] == tab[58] and tab[30] == 'O':
            comp_placement = 10
        elif tab[58] == tab[2] and tab[58] == 'O':
            comp_placement = 10
        elif tab[10] == tab[30] and tab[10] == 'O':
            comp_placement = 50
        elif tab[30] == tab[50] and tab[30] == 'O':
            comp_placement = 10
        elif tab[50] == tab[10] and tab[50] == 'O':
            comp_placement = 30
        else:
            comp_p = int(rd.choice(choice))
            comp_placement = index_convertor(comp_p)
        comp_placement = key[int(comp_placement)]
        if index_convertor(comp_placement) not in choice:
            return comp_placement
        else:
            continue


def wint_checker(tab):
    c = 'Computer Won'
    u = 'User Won'

    if tab[2] == tab[6] and tab[6] == tab[10] and tab[2] == tab[10]:
        if tab[2] == 'X':
            return u
        elif tab[2] == 'O':
            return c
    elif tab[30] == tab[26] and tab[26] == tab[34] and tab[30] == tab[34]:
        if tab[26] == 'X':
            return u
        elif tab[26] == 'O':
            return c
    elif tab[50] == tab[54] and tab[54] == tab[58] and tab[50] == tab[58]:
        if tab[50] == 'X':
            return u
        elif tab[50] == 'O':
            return c
    elif tab[2] == tab[26] and tab[26] == tab[50] and tab[2] == tab[50]:
        if tab[2] == 'X':
            return u
        elif tab[2] == 'O':
            return c
    elif tab[6] == tab[30] and tab[30] == tab[54] and tab[6] == tab[54]:
        if tab[6] == 'X':
            return u
        elif tab[6] == 'O':
            return c
    elif tab[10] == tab[34] and tab[34] == tab[58] and tab[10] == tab[58]:
        if tab[10] == 'X':
            return u
        elif tab[10] == 'O':
            return c
    elif tab[10] == tab[30] and tab[30] == tab[50] and tab[10] == tab[50]:
        if tab[10] == 'X':
            return u
        elif tab[10] == 'O':
            return c
    elif tab[2] == tab[30] and tab[30] == tab[58] and tab[2] == tab[58]:
        if tab[2] == 'X':
            return u
        elif tab[2] == 'O':
            return c


def win_checker(tab):
    c = 'Computer Won'
    u = 'User Won'

    if tab[2] != ' ' and (tab[2] == tab[6] and tab[6] == tab[10] and tab[2] == tab[10]):
        if tab[10] == 'X':
            print(u)
            return u
        elif tab[2] == 'O':
            print(c)
            return c
    elif tab[26] != ' ' and (tab[30] == tab[26] and tab[26] == tab[34] and tab[30] == tab[34]):
        if tab[26] == 'X':
            print(u)
            return u
        elif tab[26] == 'O':
            print(c)
            return c
    elif tab[50] != ' ' and (tab[50] == tab[54] and tab[54] == tab[58] and tab[50] == tab[58]):
        if tab[50] == 'X':
            print(u)
            return u
        elif tab[50] == 'O':
            print(c)
            return c
    elif tab[2] != ' ' and (tab[2] == tab[26] and tab[26] == tab[50] and tab[2] == tab[50]):
        if tab[2] == 'X':
            print(u)
            return u
        elif tab[2] == 'O':
            print(c)
            return c
    elif tab[2] != ' ' and (tab[6] == tab[30] and tab[30] == tab[54] and tab[6] == tab[54]):
        if tab[6] == 'X':
            print(u)
            return u
        elif tab[6] == 'O':
            print(c)
            return c
    elif tab[2] != ' ' and (tab[10] == tab[34] and tab[34] == tab[58] and tab[10] == tab[58]):
        if tab[10] == 'X':
            print(u)
            return u
        elif tab[10] == 'O':
            print(c)
            return c
    elif tab[2] != ' ' and (tab[2] == tab[30] and tab[30] == tab[10] and tab[2] == tab[10]):
        if tab[2] == 'X':
            print(u)
            return u
        elif tab[2] == 'O':
            print(c)
            return c
    elif tab[2] != ' ' and (tab[2] == tab[6] and tab[6] == tab[10] and tab[2] == tab[10]):
        if tab[2] == 'X':
            print(u)
            return u
        elif tab[2] == 'O':
            print(c)
            return c
    elif tab[10] == tab[30] and tab[30] == tab[50] and tab[10] == tab[50]:
        if tab[10] == 'X':
            print(u)
            return u
        elif tab[10] == 'O':
            print(c)
            return c
    elif tab[2] == tab[30] and tab[30] == tab[58] and tab[2] == tab[58]:
        if tab[2] == 'X':
            print(u)
            return u
        elif tab[2] == 'O':
            print(c)
            return c


table()

while True:
    inputs = input('Choose the position to place your marker(1-9) or Press Q to quit : ')
    if inputs in choice:
        position = index_convertor(inputs)
        Table = Table[:position] + 'X' + Table[position + 1:]
        win_checker(Table)

        if wint_checker(Table) == 'Computer Won' or wint_checker(Table) == 'User Won':
            table()
            if wint_checker(Table) == 'Computer Won':
                comp_wins += 1
            elif wint_checker(Table) == 'User Won':
                user_wins += 1
            i = input("Do you want to continue? (Yes/No): ").lower()
            if i in 'no':
                print('User Wins =', user_wins)
                print('Computer Wins =', comp_wins)
                break
            elif i in 'yes':
                Table = '\n   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'
                choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                table()
                continue
            else:
                print('Invalid option!')
                break
        else:
            print('')
        choice.remove(inputs)
        if choice:
            comp_chose = comp_pos(Table)
            comp_choice = index_convertor(comp_chose)
            choice.remove(str(comp_chose))
            Table = Table[:comp_choice] + 'O' + Table[comp_choice + 1:]
        elif not choice:
            print('Draw')
        table()
        win_checker(Table)
        if wint_checker(Table) == 'Computer Won' or wint_checker(Table) == 'User Won':
            table()
            break
        else:
            print('')
    elif inputs.lower() in 'q':
        print('User Wins =', user_wins)
        print('Computer Wins =', comp_wins)
        break
    else:
        print('\n Unsupported Number \n')
