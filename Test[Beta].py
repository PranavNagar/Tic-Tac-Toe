import Node,time
def getBoardCopy(b):
    # Make a duplicate of the board. When testing moves we don't want to 
    # change the actual board
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard
def get_last(a):
	if a == []:
		return int
	else:
		return type(a[-1])
def pos(x):
	if not get_last(x)==int:
		return [x]
	x1 = getBoardCopy(x)
	pos_line = []
	for i in range(9):
		p = win(x1+[i],"x")
		if p != "Posistion" and i not in x1:
			pos_line += [x1+[i]+[p]]
		elif i not in x1:
			pos_line += [x1+[i]]
	return pos_line

def f1(posibility1):
	lines = []
	for i in pos(posibility1):
		posic = [i]
		for _ in range(8-len(posibility1)):
			posic2 = posic
			posic = []
			for j in posic2:
				posic += pos(j)
		lines += posic
	return lines

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
	b = [" ",]*9
	for x in range(len(posibility)):
		if type(posibility[x]) == int:
			b[posibility[x]] = ["O","X"][x%2]
		else:
			return posibility[x]
	if checkWin(b,"X"):
		return "True"
	elif checkWin(b,"O"):
		return "False"
	elif " " not in b:
		return "Draw"
	else:
		return "Posistion"
@Node.timer
def main(posibility = [0,1,6,7]):
	player_move = (len(posibility))%2
	posibility_list = f1(posibility)
	#print(len(posibility_list))
	tree = Node.treeify(posibility_list)
	bottom = Node.bottomView(tree)
	false_list = [x for x in bottom if x.data == "False"]
	true_list = [x for x in bottom if x.data == "True"]
	draw_list = [x for x in bottom if x.data == "Draw"]
	print(len(false_list),len(true_list),len(draw_list))
	start_time = time.time()
	for x in false_list:
		temp = x
		for _ in range(temp.get_level()):
			alive_child = temp.child_alive()
			#print(f"[{temp.data}],[{temp.parent.data}],[{temp.parent.childData}],[{alive_child}]")
			#print((temp.get_level()%2 == player_move),len(alive_child)>=1)
			#temp.print_parentage()
			if (temp.get_level()%2 == player_move) and len(alive_child)>=1:
				break
			else:
				Node.kill_node(temp)
				temp = temp.parent
				continue
	print("hello:--- %s seconds ---" % (time.time() - start_time))
	bottom = Node.bottomView(tree)
	false_list = [x for x in bottom if (x.data == "False" and x.state)]
	true_list = [x for x in bottom if (x.data == "True" and x.state)]
	draw_list = [x for x in bottom if (x.data == "Draw" and x.state)]
	print(len(false_list),len(true_list),len(draw_list))
	for x in true_list:
		if x.state:
			Node.kill_sibling(x.parent)
	bottom = Node.bottomView(tree)
	true_list = [x for x in bottom if (x.data == "True" and x.state)]
	draw_list = [x for x in bottom if (x.data == "Draw" and x.state)]
	print(len(draw_list),len(true_list))
	#tree.print_tree(show_dead=False)
	y = tree
	for x in posibility:
		y = y.child[y.childData.index(x)]
	print(y.data)
	move_dict = {}
	for x in y.child_alive():
		view = Node.bottomView(x)
		move_dict[x] = [x.data for x in view].count('True')/([x.data for x in view].count('Draw')+[x.data for x in view].count('True'))
	if move_dict == {}:
		return "Lost"
	return sorted(move_dict.items(), key=lambda kv:(kv[1], kv[0].data))[0][0].data
print(main())
#main()
