import random
import time
board = list(range(1,10))

def show():
    print(board[6],'|',board[7],'|',board[8])
    print('-----------')
    print(board[3],'|',board[4],'|',board[5])
    print('-----------')
    print(board[0],'|',board[1],'|',board[2])
def win(char):
    if (board[0] == char and board[1] == char and board[2] == char) or (board[3] == char and board[4] == char and board[5] == char) or \
        (board[6] == char and board[7] == char and board[8] == char) or (board[6] == char and board[3] == char and board[0] == char) or \
        (board[7] == char and board[4] == char and board[1] == char) or (board[8] == char and board[5] == char and board[2] == char) or \
        (board[6] == char and board[4] == char and board[2] == char) or (board[0] == char and board[4] == char and board[8] == char):
        return True
def comp_play():
    global choice2
    choice2 = random.randint(0, 9)
    if board[choice2 - 1] != 'x' and board[choice2 - 1] != 'o':
        board[choice2 - 1] = 'o'


while True:
    #os.system('clear')
    show()
    choice = int(input('Choose a position'))
    if board[choice - 1] != 'x' and board[choice - 1] != 'o':
        board[choice - 1] = 'x'
    else:
        print('Sorry! That space is already taken')
        time.sleep(1)
    if win('x') == True:
        show()
        print('Player X has won')
        break
    '''full = True
    for i in range(0,9):
        for j in board:
            if board[j] != 'x' or board != 'o':
                full = False
                break
    if full:
        print("That's a Tie!!")'''


    choice2 = random.randint(0,9)
    if board[choice2 - 1] != 'x' and board[choice2 - 1] != 'o':
        board[choice2 - 1] = 'o'
    else:
        time.sleep(1)
        comp_play()
    if win('o') == True:
        show()
        print('Player O has won')
        break
    '''full = True
    for i in range(0, 9):
        for j in board:
            if board[j] != 'x' or board != 'o':
                full = False
                break
    if full:
        print("That's a Tie!!")'''

time.sleep(5)