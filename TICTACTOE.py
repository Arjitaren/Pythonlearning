#from IPython.display import clear_output

test_board = ['#', ' ',' ',' ',' ',' ',' ',' ',' ',' ']

#fUNCTION for displaying board
def display(board):
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
#Chosing marker function
def player_input():
    marker = ''
    #Keep asking player 1 to chose X or O

    while marker!='X' and marker!='O':
        marker = input('Player 1 chose X or O :')

    player1 = marker

    if player1=='X':
        player2='O'
    else:
        player2='X'

    return (player1,player2)

#Function for deciding the index to place X or O on board
def position(Player):
    #print('_'*10)
    index=''
    while index not in range(1,10):
        index = int(input(Player + ' Chose the position from 1-9 to play:'))

    return index

#function for changing test_board list  after each turn of player 1
def change_board1(indexpos1):
    #indexpos=''
    test_board[indexpos1] = player1_marker
    return test_board
    """
    i=0
    while i in range (1,10):
        if i%2==0:
            test_board[indexpos] = player2_marker
        else:
    """
#function for changing test_board list  after each turn of player 2
def change_board2(indexpos2):
    test_board[indexpos2] = player2_marker
    return test_board

#function to check if a player has won
def win_check(test_board,player,player_marker):
    #checking win row wise
    j=0
    if (test_board[1]==player_marker and test_board[2]==player_marker and test_board[3]==player_marker) or (test_board[4]==player_marker and test_board[5]==player_marker and test_board[6]==player_marker) or (test_board[7]==player_marker and test_board[8]==player_marker and test_board[9]==player_marker):
        print(player + ' won!!')
        j=1

    #checking win column wise
    elif (test_board[1]==player_marker and test_board[4]==player_marker and test_board[7]==player_marker) or (test_board[2]==player_marker and test_board[5]==player_marker and test_board[8]==player_marker) or (test_board[3]==player_marker and test_board[6]==player_marker and test_board[9]==player_marker):
        print(player + ' won!!')
        j=1
    #checking win diagonally
    elif (test_board[1]==player_marker and test_board[5]==player_marker and test_board[9]==player_marker) or (test_board[3]==player_marker and test_board[5]==player_marker and test_board[7]==player_marker):
        print(player + ' won!!')
        j=1
    return j


display(test_board)

player1_marker , player2_marker = player_input()

for i in range (1,10):
    if i%2!=0:
        index_position = position('Player 1')
        test_board = change_board1(index_position)
        display(test_board)
        k = win_check(test_board,'Player 1',player1_marker)
        if k==1:
            break

    else:
        index_position = position('Player 2')
        test_board = change_board2(index_position)
        display(test_board)
        k = win_check(test_board, 'Player 2', player2_marker)
        if k==1:
            break

