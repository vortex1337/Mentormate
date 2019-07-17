import os
d = {'7':0, '8':1, '9':2, '4':3, '5':4, '6':5, '1':6, '2':7, '3':8}
arr = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print('Do you want to be X or O')
player1 = raw_input()
if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'
def clear():
    os.system( 'clear' )
def print_board(board):
    print "    |     |    \n  {} |  {}  | {}  \n    |     |    \n--------------\n    |     |    \n  {} |  {}  | {}  \n    |     |    \n--------------\n    |     |    \n  {} |  {}  | {}  \n    |     |    ".format(*board)
def next_turn(board, marker):
    s = str(input())
    clear()
    arr[d[s]] = marker
    print_board(arr)
def check_equal_list(lst):
   return lst[1:] == lst[:-1] and ' ' not in lst
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
def who_wins(arr):
    matrix = []
    j=0
    for i in range(3):
        matrix.append(arr[j:j+3])
        j+=3
    transpose_matrix=transpose(matrix)
    d1,d2=[],[]
    for i in range(3):
        if check_equal_list(matrix[i]) or check_equal_list(transpose_matrix[i]):
            if player1 in matrix[i]:
                print("Player 1 ({}) wins.".format(player1))
            else:
                print("Player 2 ({}) wins.".format(player2))
        d1.append(matrix[i][i])
        d2.append(transpose_matrix[i][i])
    if check_equal_list(d1) or check_equal_list(d2):
        if player1 in matrix[i]:
            print("Player 1 ({}) wins.".format(player1))
        else:
            print("Player 2 ({}) wins.".format(player2))
def full_board_check(arr):
    if ' ' not in arr:
        print "The game was even"
        return True
    return False
print_board(arr)
while True:
    next_turn(arr, player1)
    if full_board_check(arr):
        break
    if who_wins(arr) != None:
        break
    next_turn(arr, player2)
    if who_wins(arr) != None:
        break
    if full_board_check(arr):
        break
