import os,random,time
def displayBoard(b):
	#os.system("cls")
	print('     +     +')
	print('  ' + b[0] + '  |  ' + b[1] + '  |  ' + b[2])
	print('     +     +')
	print('-----------------')
	print('     +     +')
	print('  ' + b[3] + '  |  ' + b[4] + '  |  ' + b[5])
	print('     +     +')
	print('-----------------')
	print('     +     +')
	print('  ' + b[6] + '  |  ' + b[7] + '  |  ' + b[8])
	print('     +     +')
b = [" ",]*9
game = [1,7,6,2,5,0]
for x in range(len(game)):
	if type(game[x]) == int:
		b[game[x]] = ["X","O"][x%2]
		displayBoard(b)
	print("<----------------->")
	time.sleep(1)