import os,STD,Test2,Board,Cur_pos
os.system("")

def move_cur (y, x):
	print("\033[%d;%dH" % (y, x),end="")


x, y = Cur_pos.cursorPos()

move_cur(y+8,0)
print('Engine or Code? (1/2)')
if input() == '1':
    Engine = True
else:
    Engine = False
move_cur(y+9,0)
print(" "*30,flush = True,end="")

while True:
    InGame = True
    board = [' '] * 9
    move_order_list = []
    move_cur(y+8,0)
    print('first or second? (1/2)')
    print(" "*30,flush = True,end="")
    move_cur(y+9,0)
    if input() == '1':
        playerMarker = '0'
    else:
        playerMarker = 'X'

    move_cur(y+8,30)
    print('[             ]')
    while InGame:
        move_cur(y+8,0)
        print('Player go: (1-9)             ')

        if playerMarker == '0':
            move_cur(y+9,0)
            move = int(input()[0])-1
            move_cur(y+9,0)
            print(" "*30)

            if board[move] != ' ':
                move_cur(y+8,30)
                print('[Invalid move!]')
                continue
            else :
                move_cur(y+8,30)
                print('[             ]')
        else:

            move = Test2.main(move_order_list) if Engine else STD.getComputerMove3(board)

        board[move] = playerMarker
        move_order_list.append(move)

        move_cur(y+0,0)
        Board.main(move_order_list)
    
        if STD.checkWin(board, playerMarker):
            InGame = False
            if playerMarker == '0':
                move_cur(y+8,30)
                print('[Zeroes  won !]')
            else:
                move_cur(y+8,30)
                print('[Crosses won !]')
            continue
    
        if STD.checkDraw(board):
            InGame = False
            move_cur(y+8,30)
            print('[       Draw !]')
            continue
        

        if playerMarker == '0':
            playerMarker = 'X'
        else:
            playerMarker = '0'
