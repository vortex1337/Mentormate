import os
from random import randint
def clear():
    os.system( 'clear' )
def print_board(board):
    print "    |     |    \n  {} |  {}  | {}  \n    |     |    \n--------------\n    |     |    \n  {} |  {}  | {}  \n    |     |    \n--------------\n    |     |    \n  {} |  {}  | {}  \n    |     |    ".format(*board)
def next_turn(board, marker):
    s = raw_input("{} turn (choose 1-9): ".format(marker))
    while s.isalpha() or (int(s)>9 or int(s)<0) or arr[d[s]] != ' ':
        s = raw_input("{} turn (choose 1-9): ".format(marker))
    clear()
    arr[d[s]] = marker
    print_board(arr)
def check_equal_list(lst):
   return lst[1:] == lst[:-1] and ' ' not in lst
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
def make_matr(arr):
    matrix = []
    j=0
    for i in range(3):
        matrix.append(arr[j:j+3])
        j+=3
    return matrix
def who_wins(arr):
    global win_check
    win_check = False
    matrix = make_matr(arr)
    transpose_matrix=transpose(matrix)
    d1,d2=[' ',' ',' '],[' ',' ',' ']
    for i in range(3):
        if check_equal_list(matrix[i]):
            win_check = True
            if player1 in matrix[i]:
                print ("{} wins.".format(player1))
            else:
                print ("{} wins.".format(player2))
        elif check_equal_list(transpose_matrix[i]):
            win_check = True
            if player1 in transpose_matrix[i]:
                print ("{} wins.".format(player1))
            else:
                print ("{} wins.".format(player2))
        d1[i] = matrix[i][i]
        d2[i] = matrix[i][2-i]

    if check_equal_list(d1):
        win_check = True
        if player1 in d1:
            print ("{} wins.".format(player1))
        else:
            print ("{} wins.".format(player2))
    elif check_equal_list(d2):
        win_check = True
        if player1 in d2:
            print ("{} wins.".format(player1))
        else:
            print ("{} wins.".format(player2))

def replay():
    s = raw_input("Replay? y/n: ")
    if s!='y':
        if s!='n':
            clear()
            replay()
    if s == 'y':
        clear()
        new_game()
        play()
        replay()
def full_board_check(arr):
    if ' ' not in arr:
        print "The game was even"
        return True
    return False
def play():
    while True:
        if chance == 1:
            next_turn(arr, player1)
            if full_board_check(arr):
                break
            who_wins(arr)
            if win_check:
                break
            next_turn(arr, player2)
            if full_board_check(arr):
                break
            who_wins(arr)
            if win_check:
                break
        else:
            next_turn(arr, player2)
            if full_board_check(arr):
                break
            who_wins(arr)
            if win_check:
                break
            next_turn(arr, player1)
            if full_board_check(arr):
                break
            who_wins(arr)
            if win_check:
                break
def new_game():
    global arr,player1,d,player2
    d = {'7':0, '8':1, '9':2, '4':3, '5':4, '6':5, '1':6, '2':7, '3':8}
    arr = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('Do you want to be X or O')
    print_board(arr)
    player1 = raw_input()
    if player1 != 'X':
        if player1 != 'O':
            clear()
            new_game()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    clear()
    print_board(arr)
chance = randint(1,2)
new_game()
play()
replay()
