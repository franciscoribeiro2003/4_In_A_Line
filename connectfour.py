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
                col = cpuMove(cpu, table)

        else:
            if currentSymbol == symbols[0]:
                print("\nIt is now the CPU turn.")
                col = cpuMove(cpu, table)

            else:
                print("\nIt is now your turn.")
                print("Make a move by choosing your coordinates to play (1 to 7).")
                col = choice(table)                  

        for row in range(ROWS-1, -1, -1): 
            if table[row][col] == '- ':
                table[row][col] = currentSymbol
                break

        print("Utilidade: " + str(utility(table)))

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
def cpuMove(cpu, table):
    if cpu == 1:
        return minimax(table)
    elif cpu == 2:
        return alphabeta(table)
    else:
        return mcts(table)

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
    #return uLine(table) + uColumn(table) + uDiagonal(table)
    l = uLine(table)
    c = uColumn(table)
    print("uLine: %d | uColumn: %d\n" %(l, c))
    return uLine(table) + uColumn(table)

def uColumn(table):
    points = 0
    for c in range(COLS):
        if table[0][c] == '- ' and table[1][c] == '- ' and table[2][c] == '- ' and table[3][c] == '- ' and table[4][c] == '- ' and table[5][c] == '- ': continue

        for r in range(ROWS-1, 4, -1):
            first = table[r][c]
            second = table[r - 1][c]
            third = table[r - 2][c]
            forth = table[r - 3][c]
            
            #Points for X
            if first == 'X ':
                if second == '- ':
                    if third == '- ' and forth == '- ': points += 1
                    elif third == 'X ' and forth == '- ': points += 10
                    elif third == 'X ' and forth == 'X ': points += 50
                    else: continue

                elif second == 'X ':
                    if third == '- ' and forth == '- ': points += 10
                    elif third == 'X ' and forth == '- ': points += 50
                    elif third == 'X ' and forth == 'X ': points = 512
                    else: continue        

            #Points for O
            elif first == 'O ':
                if second == '- ':
                    if third == '- ' and forth == '- ': points -= 1
                    elif third == 'O ' and forth == '- ': points -= 10
                    elif third == 'O ' and forth == 'O ': points -= 50
                    else: continue

                elif second == 'O ':
                    if third == '- ' and forth == '- ': points -= 10
                    elif third == 'O ' and forth == '- ': points -= 50
                    elif third == 'O ' and forth == 'O ': points = -512
                    else: continue

            else:
                #The - X sequence
                if second == 'X ':
                    if third == '- ' and forth == '- ': points += 1
                    elif third == 'X ' and forth == '- ': points += 10
                    elif third == 'X ' and forth == 'X ': points += 50
                    else: continue
                
                #The - O sequence
                elif second == 'O ':
                    if third == '- ' and forth == '- ': points -= 1
                    elif third == 'O ' and forth == '- ': points -= 10
                    elif third == 'O ' and forth == 'O ': points -= 50
                    else: continue

                #The - - sequence
                else:
                    if (third == 'X ' and forth == '- ') or (third == '- ' and forth == 'X '): points += 1
                    elif third == 'X ' and forth == 'X ': points += 10
                    elif (third == 'O ' and forth == '- ') or (third == '- ' and forth == 'O '): points -= 1
                    elif third == 'O ' and forth == 'O ': points -= 10
                    else: continue

    return points

def uLine(table):
    points = 0
    for l in range(ROWS-1, -1, -1):
        line = table[l]

        if line == ['- ','- ','- ','- ','- ','- ','- ']: return points

        for i in range(4):
            first = line[i]
            second = line[i + 1]
            third = line[i + 2]
            forth = line[i + 3]

            #Points for X
            if first == 'X ':
                #The X - sequence
                if second == '- ':
                    if third == '- ' and forth == '- ': points += 1
                    elif third == 'X ' and forth == '- ': points += 10
                    elif third == 'X ' and forth == 'X ': points += 50
                    else: continue
                
                #The X X sequence
                elif second == 'X ':
                    if third == '- ' and forth == '- ': points += 10
                    elif third == 'X ' and forth == '- ': points += 50
                    elif third == 'X ' and forth == 'X ': points = 512
                    else: continue

            #Points for O
            elif first == 'O ':
                #The O - sequence
                if second == '- ':
                    if third == '- ' and forth == '- ': points -= 1
                    elif third == 'O ' and forth == '- ': points -= 10
                    elif third == 'O ' and forth == 'O ': points -= 50
                    else: continue

                #The O O sequence
                elif second == 'O ':
                    if third == '- ' and forth == '- ': points -= 10
                    elif third == 'O ' and forth == '- ': points -= 50
                    elif third == 'O ' and forth == 'O ': points = -512
                    else: continue
            
            #Check if there is a symbol after -
            else:
                #The - X sequence
                if second == 'X ':
                    if third == '- ' and forth == '- ': points += 1
                    elif third == 'X ' and forth == '- ': points += 10
                    elif third == 'X ' and forth == 'X ': points += 50
                    else: continue
                
                #The - O sequence
                elif second == 'O ':
                    if third == '- ' and forth == '- ': points -= 1
                    elif third == 'O ' and forth == '- ': points -= 10
                    elif third == 'O ' and forth == 'O ': points -= 50
                    else: continue

                #The - - sequence
                else:
                    if (third == 'X ' and forth == '- ') or (third == '- ' and forth == 'X '): points += 1
                    elif third == 'X ' and forth == 'X ': points += 10
                    elif (third == 'O ' and forth == '- ') or (third == '- ' and forth == 'O '): points -= 1
                    elif third == 'O ' and forth == 'O ': points -= 10
                    else: continue

    return points

#Minimax Algorithm
def minimax(table):
    return random.randint(0,6)

#Alpha Beta Algorithm
def alphabeta(table):
    return random.randint(0,6)

#MCTS Algorithm
def mcts(table):
    return random.randint(0,6)

game(table)
