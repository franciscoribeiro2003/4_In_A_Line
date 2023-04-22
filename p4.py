import random
import time
import math
from copy import deepcopy
import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
size = (800, 700)
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("Connect Four")

# Set the font for the text
font = pygame.font.Font(None, 36)

ROWS = 6
COLS = 7
SYMBOLS = ['X', 'O']

# Initialize the game board
board = [['-'] * COLS for _ in range(ROWS)]

# Prints the game board
def print_board():
    for i in range(6):
        for j in range(7):
            print(board[i][j], end=' ')
        print()
    print('1 2 3 4 5 6 7\n')
    print()


# Prompts the user to choose X or O
def choose_symbol():
    while True:
        symbol = input("Choose X(RED, start first) or O(BLACK): ")
        if symbol in SYMBOLS:
            return symbol
        
def empate():
    if all('-' not in row for row in board):
        print_board()
        print("It's a tie!")
        return True
    return False

def not_symbol(symbol):
    if symbol == SYMBOLS[0]:
        return SYMBOLS[1]
    else:
        return SYMBOLS[0]
        
# Prompts the user to choose the difficulty level
def choose_difficulty():
    print("Choose the algorithm you want to play against:")
    print("1: Minimax | 2: Alpha Beta | 3: MCTS")
    while True:
        try:
            return int(input())
        except ValueError:
            print("Please type a number.")


# Gets a legal move from the user
def get_move():
    while True:
        try:
            col = int(input("Make a move by choosing your column (1 to 7): ")) - 1
            if col < 0 or col >= COLS or board[0][col] != '-':
                raise ValueError
            return col
        except ValueError:
            print("That's an illegal move, try again.")




# Makes a move on the board and returns the row where the piece landed
def make_move(symbol, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == '-':
            board[row][col] = symbol
            return True
    return False



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


    
# Calculate the utility of the table
def utility(table):
    if check(table, 'X'):
        return 1000
    elif check(table, 'O'):
        return -1000
    else:
        return uTable(table)
    
# Utility points from the table
def uTable(table):
    points = 0
    
    # Count X and O values in each row, column, and diagonal
    rows = table
    cols = [[table[j][i] for j in range(ROWS)] for i in range(COLS)]
    diags = [[table[i+k][j+k] for k in range(4)] for i in range(ROWS-3) for j in range(COLS-3)] + [[table[i+k][j-k+3] for k in range(4)] for i in range(ROWS-3) for j in range(COLS-3)]
    
    # Calculate utility points for each row, column, and diagonal
    for line in rows + cols + diags:
        x_count = line.count('X')
        o_count = line.count('O')
        
        if x_count > 0 and o_count == 0:
            if x_count == 1: points += 1
            elif x_count == 2: points += 10
            elif x_count == 3: points += 50
        elif x_count == 0 and o_count > 0:
            if o_count == 1: points -= 1
            elif o_count == 2: points -= 10
            elif o_count == 3: points -= 50
    
    return points


# Undo the move
def undo_move(thisboard,col, row):
    thisboard[row][col] = '-'

def move_selected(thisboard,symbol, col):
    for row in range(ROWS-1, -1, -1):
        if thisboard[row][col] == '-':
            thisboard[row][col] = symbol
            return row
    return None


def legal_moves(table):
    #retorna uma lista de inteiros com as colunas que podem ser jogadas
    lista = []
    for col in range(COLS):
        if table[0][col] == '-':
            lista += [col]
    return lista

def game_over(thisboard, symbol):
    return check(thisboard, symbol) or len(legal_moves(thisboard)) == 0


# Gets a legal move from the CPU using the selected algorithm
def get_cpu_move(difficulty,NotSymbol):
    if difficulty == 1:
        return minimax(board, 4, NotSymbol)[1]
    elif difficulty == 2:
        return alphabeta(board, 6, NotSymbol, -math.inf, math.inf)[1]
    else:
        return mcts(board, NotSymbol)

# Minimax Algorithm
def minimax(thisboard, depth, symbol):
    best_move=-1
    if depth==0 or game_over(thisboard, symbol):
        return utility(thisboard), None
    
    if symbol == 'X':
        maxEval = -math.inf
        #for each child
        for col in (legal_moves(thisboard)):
            row = move_selected(thisboard,symbol, col)
            eval = minimax(thisboard, depth-1, not_symbol(symbol))[0]
            undo_move(thisboard, col, row)
            if eval>maxEval:
                maxEval = eval
                best_move=col
        return maxEval,best_move
    
    else:
        minEval = math.inf
        #for each child
        for col in (legal_moves(thisboard)):
            row = move_selected(thisboard,symbol, col)
            eval = minimax(thisboard, depth-1, not_symbol(symbol))[0]
            undo_move(thisboard, col, row)
            if eval<minEval:
                minEval = eval
                best_move=col
        return minEval, best_move

#Alpha Beta Algorithm
def alphabeta(thisboard, depth,symbol , alpha, beta):
    best_move=None
    if depth==0 or game_over(thisboard, symbol):
        return utility(thisboard), None
    
    if symbol == 'X':
        maxEval = -math.inf
        #for each child
        for col in (legal_moves(thisboard)):
            row = move_selected(thisboard,symbol, col)
            eval = alphabeta(thisboard, depth-1, not_symbol(symbol), alpha, beta)[0]
            undo_move(thisboard, col, row)
            if eval>maxEval:
                maxEval = eval
                best_move=col
            alpha= max(alpha, maxEval)
            if beta<=alpha: break
        return maxEval,best_move

    else:
        minEval = math.inf
        #for each child
        for col in (legal_moves(thisboard)):
            row = move_selected(thisboard,symbol, col)
            eval = alphabeta(thisboard, depth-1, not_symbol(symbol), alpha, beta)[0]
            undo_move(thisboard, col, row)
            if eval<minEval:
                minEval = eval
                best_move=col
            beta= min(beta, minEval)
            if beta<=alpha: break
        return minEval, best_move
    

#MCTS Algorithm (Trocar pela classe)
def mcts(table, symbol):   
    class Node:
        def __init__(self, move, parent):
            self.move = move
            self.parent = parent
            self.N = 0
            self.Q = 0
            self.children = {}

        def add_children(self, children: dict) -> None:
            for child in children:
                self.children[child.move] = child

        #função Upper Confidence Bound (UCB)
        def UCB(self):
            if self.N == 0:
                return 0 if math.sqrt(2) == 0 else float('inf')
            return self.Q / self.N + math.sqrt(2) * math.sqrt(math.log(self.parent.N) / self.N)


    class MCTS:
        def __init__(self, state, symbol):
            self.root_state = deepcopy(state)
            self.symbol = symbol
            self.root = Node(None, None)
            self.run_time = 0
            self.node_count = 0
            self.num_rollouts = 0

        def select_node(self) -> tuple:
            node = self.root
            state = deepcopy(self.root_state)

            while len(node.children) != 0:
                children = node.children.values()
                max_value = max(children, key=lambda n: n.UCB()).UCB()
                max_nodes = [n for n in children if n.UCB() == max_value]

                #choices = legal_moves(state)
                node = random.choice(max_nodes)
                move_selected(state, symbol ,node.move)

                if node.N == 0:
                    return node, state

            if self.expand(node, state):
                node = random.choice(list(node.children.values()))
                move_selected(state, self.symbol, node.move)

            return node, state

        def expand(self, parent: Node, state) -> bool:
            if check(state, self.symbol):
                return False

            children = [Node(move, parent) for move in legal_moves(state)]
            parent.add_children(children)

            return True

        def roll_out(self, state):
            while not check(state, self.symbol):
                move_selected(state, self.symbol ,random.choice(legal_moves(state)))

            return check(state, symbol)

        def back_propagate(self, node: Node, outcome) -> None:

            # For the current player, not the next player
            reward = 0 if outcome else 1

            while node is not None:
                node.N += 1
                node.Q += reward
                node = node.parent
                if empate():
                    reward = 0
                else:
                    reward = 1 - reward

        def search(self, time_limit: int):
            start_time = time.process_time()

            num_rollouts = 0
            while time.process_time() - start_time < time_limit:
                node, state = self.select_node()
                outcome = self.roll_out(state)
                self.back_propagate(node, outcome)
                num_rollouts += 1

            run_time = time.process_time() - start_time
            self.run_time = run_time
            self.num_rollouts = num_rollouts

        def best_move(self):
            if check(self.root_state, self.symbol):
                return -1

            max_value = max(self.root.children.values(), key=lambda n: n.N).N
            max_nodes = [n for n in self.root.children.values() if n.N == max_value]
            best_child = random.choice(max_nodes)

            return best_child.move

        def move(self, move):
            if move in self.root.children:
                self.root_state.move(move)
                self.root = self.root.children[move]
                return

            self.root_state.move(move)
            self.root = Node(None, None)

        def statistics(self) -> tuple:
            return self.num_rollouts, self.run_time
    
    mcts = MCTS(table, symbol)
    mcts.search(4)
    move = mcts.best_move()
    return move #ERRO


# Define a function to draw the game board
def draw_board(board, player_turn):
    # Clear the screen
    screen.fill(WHITE)

    # Draw the game board
    for row in range(6):
        for col in range(7):
            pygame.draw.rect(screen, BLACK, [col*100+50, row*100+50, 100, 100], 2)
            if board[row][col] == 'X':
                pygame.draw.circle(screen, RED, [col*100+100, row*100+100], 45)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, [col*100+100, row*100+100], 45)

    # Draw the player's turn text
    player_text = font.render("Player " + player_turn + "'s turn", True, BLACK)
    screen.blit(player_text, [50, 10])

    # Update the display
    pygame.display.update()

#game loop
def main():
    print("Welcome to Connect 4!")
    print("Good luck!")
    print()
    
    symbol = choose_symbol()
    atual = 'X'
    difficulty = choose_difficulty()
    print()
    
    while True:
        print_board()
        draw_board(board, symbol)
        
        if (atual=='X' and atual==symbol):
            col = get_move()
            row = make_move(symbol, col)
            if check(board, atual):
                print_board()
                print("You won!")
                print_board()
                break
            elif empate(): break


        elif (atual=='X' and atual!=symbol):
            col = get_cpu_move(difficulty, atual)
            #print(col)
            row = make_move(atual, col)
            if check(board, atual):
                print_board()
                print("CPU won!")
                print_board()
                break
            elif empate(): break


        elif (atual=='O' and atual!=symbol):
            col = get_cpu_move(difficulty, atual)
            #print(col)
            row = make_move(atual, col)
            if check(board, atual):
                print_board()
                print("CPU won!")
                print_board()
                break
            elif empate(): break


        elif (atual=='O' and atual==symbol):
            col = get_move()
            row = make_move(symbol, col)
            if check(board, atual):
                print_board()
                print("You won!")
                print_board()
                break
            elif empate(): break
        
        atual=not_symbol(atual)
        

if __name__ == "__main__":
    main()