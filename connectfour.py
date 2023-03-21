import random

table = [['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- ']]

ROWS = 6
COLS = 7

#Play the Game
def game(table):
    print("Welcome to Connect Four! The player with the X piece start first.")
    symbols = ['X ', 'O ']
    currentSymbol = symbols[0] #Player one
    first = False #Decides if human plays first or not

    #Player chooses the piece he wants to play
    while True:
        player = input("Choose X or O: ")
        if player == 'X':
            first = True
            break
        elif player == 'O':
            break
        else:
            print("Please, pick or X or O")

    #Player chooses with difficulty he wants to play
    print("Choose the algorithm you want to play against:\n")
    print("1: Minimax | 2: Alpha Beta | 3: MCTS")
    while True:
        try:
            cpu = int(input())
            break
        except ValueError:
            print("Please type a number.")
            print()

        if cpu < 1 or cpu > 3:
            print("Please type a number beetwen 1 and 3")
            print()

    while True:
        printTable()
        print("1  2  3  4  5  6  7")

        if first:
            if currentSymbol == symbols[0]:
                print("\nIt is now your turn.")
                print("Make a move by choosing your coordinates to play (1 to 7).")
                col = choice(table)
            
            else:
                print("\nIt is now the CPU turn.")
                col = cpuMove()

        else:
            if currentSymbol == symbols[0]:
                print("\nIt is now the CPU turn.")
                col = cpuMove()

            else:
                print("\nIt is now your turn.")
                print("Make a move by choosing your coordinates to play (1 to 7).")
                col = choice(table)                  

        for row in range(ROWS-1, -1, -1): 
            if table[row][col] == '- ':
                table[row][col] = currentSymbol
                break

        #Verifying if there's a winner
        if check(table, currentSymbol):
            printTable()
            print("Player {} has won!".format(currentSymbol))
            break

        if all('- ' not in row for row in table): #Verifying draw
            print("That's a draw!")
            break

        currentSymbol = symbols[(symbols.index(currentSymbol) + 1) % 2] #Change player

#Print Table
def printTable():
    print()
    for i in range(6):
        for j in range(7):
            print(table[i][j], end=' ')
        print()
    print()

#Player picking column
def choice(table):
    while True:
        try:
            col = int(input()) - 1 #Player chooses movement
        except ValueError:
            print("Please type a number.")
            print()

        if col < 0 or col >= COLS: #Checking the limits
            print("That's an illegal move, try again.")
            continue

        elif table[0][col] != '- ': #Checking if it's occupied
            print("That's an illegal move, try again.")
            continue

        return col
    
#CPU picking column (USAR UMA FUNCAO QUE CALCULE MINIMAX, ALPHA BETA, MCTS)
def cpuMove():
    return random.randint(0,6)

#Checking if there's four in line
def check(table, symbol):
    # Check lines
    for row in range(ROWS):
        for col in range(COLS - 3):
            if table[row][col] == table[row][col+1] == table[row][col+2] == table[row][col+3] == symbol:
                return True

    # Check columns
    for col in range(COLS):
        for row in range(ROWS - 3):
            if table[row][col] == table[row+1][col] == table[row+2][col] == table[row+3][col] == symbol:
                return True

    # Check diagonals (top-left to bottom-right)
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            if table[row][col] == table[row+1][col+1] == table[row+2][col+2] == table[row+3][col+3] == symbol:
                return True

    # Check diagonals (bottom-left to top-right)
    for col in range(COLS - 3):
        for row in range(3, ROWS):
            if table[row][col] == table[row-1][col+1] == table[row-2][col+2] == table[row-3][col+3] == symbol:
                return True

    return False

game(table)