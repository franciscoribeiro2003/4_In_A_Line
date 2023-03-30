import random
import math

table = [['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- '],
         ['- ','- ','- ','- ','- ','- ','- ']]

ROWS = 6
COLS = 7
symbols = ['X ', 'O ']

#Play the Game
def game(table):
    print("Welcome to Connect Four! The player with the X piece start first.")
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
            print("Please, pick X or O")

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
                col = cpuMove(cpu, table, symbols[1])

        else:
            if currentSymbol == symbols[0]:
                print("\nIt is now the CPU turn.")
                col = cpuMove(cpu, table, currentSymbol)

            else:
                print("\nIt is now your turn.")
                print("Make a move by choosing your coordinates to play (1 to 7).")
                col = choice(table)
        
        m = move(table, currentSymbol, col)
        if m != -1: table[m][col] = currentSymbol

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
def cpuMove(cpu, table, symbol):
    if cpu == 1:
        values = minimax(table, 4, symbol, -1)
        return values[1]
    elif cpu == 2:
        return alphabeta(table)
    else:
        return mcts(table)

#Makes the move and returns its utility value
def move(t, symbol, col):
    row = -1

    for r in range(ROWS-1, -1, -1): 
        if t[r][col] == '- ':
            row = r
            break

    return row

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

#Points of a certain movement
def utility(table):
    if check(table, 'X '): return 512
    elif check(table, 'O '): return -512
    return uLine(table) + uColumn(table) + uDiagonal(table)

#Utility points from the lines
def uLine(table):
    points = 0

    for i in range(ROWS):
        for j in range(4):
            xCount = 0
            oCount = 0

            for k in range(j, j + 4):
                if table[i][k] == 'X ': xCount += 1
                elif table[i][k] == 'O ': oCount += 1

            if xCount > 0 and oCount == 0:
                if xCount == 1: points += 1
                elif xCount == 2: points += 10
                elif xCount == 3: points += 50

            elif xCount == 0 and oCount > 0:
                if oCount == 1: points -= 1
                elif oCount == 2: points -= 10
                elif oCount == 3: points -= 50

            else: continue

    return points

#Utility points from the column
def uColumn(table):
    points = 0

    for i in range(COLS):
        for j in range(3):
            xCount = 0
            oCount = 0

            for k in range(j, j + 4):
                if table[k][i] == 'X ': xCount += 1
                elif table[k][i] == 'O ': oCount += 1

            if xCount > 0 and oCount == 0:
                if xCount == 1: points += 1
                elif xCount == 2: points += 10
                elif xCount == 3: points += 50

            elif xCount == 0 and oCount > 0:
                if oCount == 1: points -= 1
                elif oCount == 2: points -= 10
                elif oCount == 3: points -= 50

            else: continue

    return points

#Utility points from the diagonals
def uDiagonal(table):
    points = 0

    for i in range(3):
        for j in range(4):
            xCount = 0
            oCount = 0

            for k in range(4):
                if table[i + k][j + k] == 'X ': xCount += 1
                elif table[i + k][j + k] == 'O ': oCount += 1

            if xCount > 0 and oCount == 0:
                if xCount == 1: points += 1
                elif xCount == 2: points += 10
                elif xCount == 3: points += 50

            elif xCount == 0 and oCount > 0:
                if oCount == 1: points -= 1
                elif oCount == 2: points -= 10
                elif oCount == 3: points -= 50

            else: continue

    return points

#Minimax Algorithm
def minimax(table, depth, symbol, col):
    if depth == 0 or check(table, 'X ') or check(table, 'O '):
        return (utility(table), col)
    
    if symbol == 'X ':
        maxEval = -math.inf
        bestMove = col

        for i in range(7):
            cloneTable = [row[:] for row in table]
            m = move(cloneTable, symbol, i)

            if m != -1:
                cloneTable[m][i] == symbol
                values = minimax(cloneTable, depth - 1, 'O ', i)
                eval = values[0]

                if eval > maxEval:
                    maxEval = eval
                    bestMove = i
            else: continue
        
        return (maxEval, bestMove)
    
    else:
        minEval = math.inf
        bestMove = col

        for i in range(7):
            cloneTable = [row[:] for row in table]
            m = move(cloneTable, symbol, i)

            if m != -1:
                cloneTable[m][i] = symbol
                values = minimax(cloneTable, depth - 1, 'X ', i)
                eval = values[0]

                if eval < minEval:
                    minEval = eval
                    bestMove = i

            else: continue

        return (minEval, bestMove)


#Alpha Beta Algorithm
def alphabeta(table):
    return random.randint(0,6)

#MCTS Algorithm
def mcts(table):
    return random.randint(0,6)

game(table)
