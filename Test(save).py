import Node
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
	x1 = getBoardCopy(x)
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
print(posibility_lines([1,7,6,2,5]))