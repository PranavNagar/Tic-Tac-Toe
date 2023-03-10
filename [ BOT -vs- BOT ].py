import os,Test2,Board,math,STD
os.system("")
ESC = {"HEADER": "\033[95m",
"BLUE": "\033[94m",
"YELLOW": "\033[93m",
"GREEN": "\033[92m",
"RED": "\033[91m",
"ENDC": "\033[0m",
}

def Progress_Bar(Total,Current):
    percent = math.ceil((Current+1)*100/Total)
    String = f"[\033[94m{chr(9632)*math.floor(percent/10):<10}\033[92m] {percent:>3}%"
    print(f"\033[17D"+String,end = "",flush = True)


owin = xwin = draws = 0

LOOP_NO = 100

print(f"{ESC['YELLOW']}Progress:"+" "*17+f"{ESC['GREEN']}",end= "",flush = True)
for seed1 in range(LOOP_NO):

    Progress_Bar(LOOP_NO,seed1)

    store_move = []
    board = [' '] * 9
    seed = seed1 % 2

    if seed == 0:
        BOT_Marker = '0'
    else:
        BOT_Marker = 'X'

    InGame = True
    while InGame:
        if BOT_Marker == '0':
            move = STD.getComputerMove3(board)
        else:
            move = Test2.main(store_move)

        board[move] = BOT_Marker
        store_move += [move]

        if STD.checkWin(board, BOT_Marker):
            InGame = False
            if BOT_Marker == '0':
                owin+=1

                print(store_move)
                Board.main(store_move)

                continue
            else:

                xwin+=1
                continue


        if len(store_move) == 9:
            InGame = False
            draws +=1
            store_move = []
            continue
        
        if BOT_Marker == '0':
            BOT_Marker = 'X'
        else:
            BOT_Marker = '0'
print(f"{ESC['ENDC']}\n",owin,xwin,draws)