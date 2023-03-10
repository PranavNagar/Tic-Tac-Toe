import Node,time
def getBoardCopy(b):
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
            (b[3] == m and b[4] == m and b[5] == m) or  # H mid
            (b[6] == m and b[7] == m and b[8] == m) or  # H bot
            (b[0] == m and b[3] == m and b[6] == m) or  # V left
            (b[1] == m and b[4] == m and b[7] == m) or  # V centre
            (b[2] == m and b[5] == m and b[8] == m) or  # V right
            (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
            (b[2] == m and b[4] == m and b[6] == m))  # RL diag

def get_last(a):
	if a == []:
		return int
	else:
		return type(a[-1])

def pos(x,m):
	if not get_last(x)==int:
		return [x]
	x1 = x.copy()
	pos_line = []
	for i in range(9):
		p = win(x1+[i],m)
		if p != "Posistion" and i not in x1:
			pos_line += [x1+[i]+[p]]
		elif i not in x1:
			pos_line += [x1+[i]]
	return pos_line

def posibility_lines(posibility1):
	m = ["X","O"][(len(posibility1)+1)%2]
	lines = []
	for i in pos(posibility1,m):
		posic = [i]
		for _ in range(8-len(posibility1)):
			posic2 = posic
			posic = []
			for j in posic2:
				posic += pos(j,m)
		lines += posic
	return lines

def posibility_lines2(posibility1):
	m = ["X","O"][(len(posibility1)+1)%2]
	lines = []
	for i in pos(posibility1,m):
		posic = [i]
		for _ in range(8-len(posibility1)):
			posic2 = posic
			posic = []
			for j in posic2:
				posic += pos(j,m)
		lines += posic
	return lines

def win(posibility,m):
	if type(posibility[-1]) == str:
		return posibility[-1]
	mnot = "X" if m=="O" else "O"
	b = [" ",]*9
	for x in range(len(posibility)):
		if type(posibility[x]) == int:
			b[posibility[x]] = ["O","X"][x%2]
		else:
			return posibility[x]
	if checkWin(b,m):
		return "True"
	elif checkWin(b,mnot):
		return "False"
	elif " " not in b:
		return "Draw"
	else:
		return "Posistion"

#@Node.timer
def main(posibility = [],timer = False):
	if posibility == []:
		return 1
	start_time = {}

	"Void[0]"

	start_time[0] = time.time()
	player_move = (len(posibility))%2
	posibility_list = posibility_lines(posibility)
	#print(len(posibility_list))
	start_time[0] -= time.time()

	"/Void[0]"

	"Void[1]"

	start_time[1] = time.time()
	tree = Node.treeify(posibility_list)
	bottom = Node.bottomView(tree)
	false_list = [x for x in bottom if x.data == "False"]
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
	true_list = [x for x in bottom if (x.data == "True" and x.state)]

	for x in true_list:
		if x.state:
			Node.kill_sibling(x.parent)
	start_time[3] -= time.time()

	"/Void[3]"

	"Void[4]"

	start_time[4] = time.time()
	y = tree
	for x in posibility:
		y = y.child[y.childData.index(x)]
	move_dict = {}
	for x in y.child_alive():
		view = Node.bottomView(x)
		move_dict[x] = [x.data for x in view].count('True')/([x.data for x in view].count('Draw')+[x.data for x in view].count('True'))
	if move_dict == {}:
		return "Lost"
	start_time[4] -= time.time()

	"/Void[4]"

	if timer:
		for keys in start_time:
			print(f"[{keys}]:--- %s seconds ---" % (-1*start_time[keys]))

	return sorted(move_dict.items(), key=lambda kv:(kv[1], kv[0].data))[0][0].data
if __name__ == "__main__":
	print(main(posibility=[],timer=True))