import Node,time,itertools

def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
            (b[3] == m and b[4] == m and b[5] == m) or  # H mid
            (b[6] == m and b[7] == m and b[8] == m) or  # H bot
            (b[0] == m and b[3] == m and b[6] == m) or  # V left
            (b[1] == m and b[4] == m and b[7] == m) or  # V centre
            (b[2] == m and b[5] == m and b[8] == m) or  # V right
            (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
            (b[2] == m and b[4] == m and b[6] == m))  # RL diag

def win(posibility,m):
	## If posibility is less than 5 no way game has ended
	if len(posibility)<5:
		return 3

	mnot = 1 if m==0 else 0

	## Make a board for checking
	b = [" ",]*9
	for x in range(len(posibility)):
		b[posibility[x]] = [0,1][x%2]
	
	## Return the current state of the game
	if checkWin(b,m):
		return 1
	elif checkWin(b,mnot):
		return 0
	elif len(posibility) == 9:
		return 2
	else:
		return 3

def posibility_lines(GAME):
	## Get The Player 's turn
	m = (len(GAME)+0) % 2 # 1,0 Decide Lose/Win;

	## Get a list of all possible ways the game can play out
	PAY_LOAD = tuple(itertools.permutations([i for i in range(9) if i not in GAME]))

	## Refine the possibilities and lable them
	POS = set()
	for i in PAY_LOAD:
		## Create a temperory new GAME tupel
		TEMP_GAME = GAME

		for j in i:
			TEMP_GAME += (j,)

			## Check if won or draw
			WIN_VAR = win(TEMP_GAME,m)

			## If game still playing
			if WIN_VAR == 3:
				continue
			
			## If game ended
			else:
				TEMP_GAME += (str(WIN_VAR),)
				break
		## Add to set
		POS.add(TEMP_GAME)

	## Return the set of all possibilities
	return POS

#@Node.timer
def main(GAME = [],TIMER = False):
	if GAME == [] :
		return 1
	if len(GAME) == 1 :
		return {0:4,1:7,2:4,3:5,4:0,5:3,6:4,7:1,8:4}[GAME[0]]
	if len(GAME) == 8:
		return [x for x in range(9) if x not in GAME][0]


	GAME = tuple(GAME)
	start_time = {}

	"Void[0]"

	start_time[0] = time.time()
	player_move = len(GAME)%2
	posibility_list = posibility_lines(GAME)
	##print(len(posibility_list))
	start_time[0] -= time.time()

	"/Void[0]"

	"Void[1]"

	start_time[1] = time.time()
	tree = Node.treeify(posibility_list)
	bottom = Node.bottomView(tree)
	false_list = [x for x in bottom if x.data == "0"]
	start_time[1] -= time.time()

	"/Void[1]"

	"Void[2]"

	start_time[2] = time.time()
	for x in false_list:
		if not x.state:
			continue
		temp = x
		for _ in range(temp.get_level()):
			alive_child = temp.parent.child_alive()
			if ((temp.parent.get_level())%2 == player_move) and len(alive_child)>1:
				Node.kill_node(temp)
				break
			else:
				temp = temp.parent
				continue
	start_time[2] -= time.time()
	bottom = Node.bottomView(tree)

	"/Void[2]"

	"Void[3]"

	start_time[3] = time.time()
	true_list = [x for x in bottom if (x.data == "1" and x.state)]

	for x in true_list:
		if x.state:
			Node.kill_sibling(x.parent)
	start_time[3] -= time.time()

	"/Void[3]"

	"Void[4]"

	start_time[4] = time.time()
	y = tree
	for x in GAME:
		y = y.child[y.childData.index(x)]
	move_dict = {}
	for x in y.child_alive():
		view = Node.bottomView(x)
		TEMP = [x.data for x in view]
		try:
			move_dict[x] = TEMP.count("1")/(TEMP.count("2") + TEMP.count("1"))
		except ZeroDivisionError:
			print(GAME)
			exit()

	if move_dict == {}:
		return "Lost"
	start_time[4] -= time.time()

	"/Void[4]"

	if TIMER:
		for keys in start_time:
			print(f"[{keys}]:--- %s seconds ---" % (-1*start_time[keys]))

	return sorted(move_dict.items(), key=lambda kv:(kv[1], kv[0].data))[0][0].data


if __name__ == "__main__":
	print("{",end ="")
	for x in range(9):
		print(f"{x}:{main([x])},",end = "")#,TIMER=True))
	print("}",end ="")