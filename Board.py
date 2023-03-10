import os,random,time

import os
os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

##print(COLOR["GREEN"], "Testing Green!!", COLOR["ENDC"])

double_line = "║═╔╗╚╝╩╠╦╣╬"
single_line = "│─┌┐└┘┴├┬┤┼"

def move (y, x):
	print("\033[%d;%dH" % (y, x),end="")

def displayBoard(b):
        print(COLOR["GREEN"],end="")
        print("╔═══╦═══╦═══╗")
        print("║ "+b[0]+" ║ "+b[1]+" ║ "+b[2]+" ║")
        print("╠═══╬═══╬═══╣")
        print("║ "+b[3]+" ║ "+b[4]+" ║ "+b[5]+" ║")
        print("╠═══╬═══╬═══╣")
        print("║ "+b[6]+" ║ "+b[7]+" ║ "+b[8]+" ║")
        print("╚═══╩═══╩═══╝")
        print(COLOR["ENDC"],end="")
def displayBoard2(b):
        print(COLOR["BLUE"],end="")
        print("╔═══╦═══╦═══╗")
        print("║ "+b[0]+" ║ "+b[1]+" ║ "+b[2]+" ║")
        print("╠═══╬═══╬═══╣")
        print("║ "+b[3]+" ║ "+b[4]+" ║ "+b[5]+" ║")
        print("╠═══╬═══╬═══╣")
        print("║ "+b[6]+" ║ "+b[7]+" ║ "+b[8]+" ║")
        print("╚═══╩═══╩═══╝")
        print(COLOR["ENDC"],end="")

def main1(GAME = []):
        b = [" ",]*9
        for x in range(len(GAME)):
        	move(0,0)
        	if type(GAME[x]) == int:
        		b[GAME[x]] = ["X","O"][x%2]
        		displayBoard2(b)
        	time.sleep(0.1)
        print()
def main(GAME = []):
        b = [" ",]*9
        for x in range(len(GAME)):
        	if type(GAME[x]) == int:
        		b[GAME[x]] = ["X","O"][x%2]
        displayBoard2(b)
if __name__ == "__main__":
        GAME = [7, 1, 4, 6, 3, 5, 0, 2, 8]
        main(GAME)
