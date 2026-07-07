import random
from colorama import Style, init, Fore

init(autoreset=True)

wincond = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(6,4,2)
]

def displayboard(board):
    print()

    def color(cell):
        if cell == "X":
            return Fore.BLUE + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.RED + cell + Style.RESET_ALL
        else:
            return Fore.GREEN + cell + Style.RESET_ALL

    print(" " + color(board[0]) + " | " + color(board[1]) + " | " + color(board[2]))
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(" " + color(board[3]) + " | " + color(board[4]) + " | " + color(board[5]))
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(" " + color(board[6]) + " | " + color(board[7]) + " | " + color(board[8]))
    print()

def playerchoice():
    symbol = ""

    while symbol not in ["X", "O"]:
        symbol = input(Fore.BLUE + "Do you want X or O? " + Style.RESET_ALL).strip().upper()

    if symbol == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def playermove(board, symbol):
    move = -1

    while move not in range(1,10) or not board[move-1].isdigit():
        try:
            move = int(input("Enter a number between 1-9: "))

            if move not in range(1,10):
                print("Invalid! Choose 1-9.")

            elif not board[move-1].isdigit():
                print("That spot is already taken.")

        except ValueError:
            print("Please enter a valid number.")

    board[move-1] = symbol

def aimove(board, aisymbol):
    available = []

    for i in range(9):
        if board[i].isdigit():
            available.append(i)

    move = random.choice(available)
    board[move] = aisymbol

def checkwin(board, symbol):
    for condition in wincond:
        if (board[condition[0]] == symbol and
            board[condition[1]] == symbol and
            board[condition[2]] == symbol):
            return True
    return False

def checkdraw(board):
    for cell in board:
        if cell.isdigit():
            return False
    return True

# ---------------- MAIN GAME ----------------

while True:

    board = ['1','2','3','4','5','6','7','8','9']

    playersymbol, aisymbol = playerchoice()

    turn = random.choice(["Player", "AI"])

    print(Fore.YELLOW + f"\n{turn} goes first!\n")

    while True:

        displayboard(board)

        if turn == "Player":

            playermove(board, playersymbol)

            if checkwin(board, playersymbol):
                displayboard(board)
                print(Fore.GREEN + "Congratulations! You Win!")
                break

            turn = "AI"

        else:

            print(Fore.MAGENTA + "AI is making a move...\n")
            aimove(board, aisymbol)

            if checkwin(board, aisymbol):
                displayboard(board)
                print(Fore.RED + "AI Wins!")
                break

            turn = "Player"

        if checkdraw(board):
            displayboard(board)
            print(Fore.YELLOW + "It's a Draw!")
            break

    again = input("\nPlay again? (Y/N): ").strip().upper()

    if again != "Y":
        print(Fore.CYAN + "Thanks for playing!")
        break