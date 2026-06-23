import random
from symtable import Symbol 
from colorama import Style, init, Fore
init(autoreset=True)
wincond= [
    (0,1,2),(3,4,5),(6,7,8)
    ,(0,3,6),(1,4,7),(2,5,8)
    ,(0,4,8),(6,4,2)
]
def board(board):
    print()
    def color(cell):
        if cell=="X":
            return Fore.BLUE+cell+ Style.RESET_ALL
        elif cell =="O":
            return Fore.RED+cell+Style.RESET_ALL
        else:
            return Fore.GREEN+cell+Style.RESET_ALL
    print(''+color(board[0])+'I'+color(board[1])+'I'+color(board[2])+'I')
    print(Fore.CYAN+'---+---+---'+Style.RESET_ALL)
    print(''+color(board[3])+'I'+color(board[4])+'I'+color(board[5])+'I')
    print(Fore.CYAN+'---+---+---'+Style.RESET_ALL)
    print(''+color(board[6])+'I'+color(board[7])+'I'+color(board[8])+'I')
def playerchoice():
    symbol = ''
    while symbol not in ['X','O']:
        symbol = input(Fore.BLUE+"Do you want X or O"+
Style.RESET_ALL).strip().upper()
    if symbol =='X':
        return ('X','O')
    else:
        return ('O','X')
def playermove():
    move = -1
    while move not in range(1,10) or not board[move-1].isdigit():
        try:
            move = int(input("Enter Number between 1-9:"))
            if move not in range(1,10) or not board[move-1].isdigit():
                print("Invalid! Try again ")
        except ValueError:
            print("Enter a value between 1-9!")
    board[move - 1]= symbol            
def aimove(board,aisymbol,playersymbol):
    for i in range(9):
        if board[i].isdigit():
            boardcopy=board.copy()
            boardcopy=aisymbol
            if checkwin(boardcopy,aisymbol):
                board[i]=aisymbol
                return
    for i in range(9):
        if board[i].isdigit():
            boardcopy=board.copy()
            boardcopy=playersymbol
            if checkwin(boardcopy,playersymbol):
                board[i]=playersymbol
                return

