#SUDOKU SOLVER with Backtracking Algrotihm
#JOHN MILTON PONCE


'''Use Backtracking Algorithm
    Return True if soduku is solvable, along with the number of steps it took to solve'''
def solve_backtrack(board, numSteps, backTrackSteps):
    if numSteps == 0: 
        if not check_Init_Board(board):
            print_board(board)
            return (False, numSteps, backTrackSteps)

    #Find empty spot within the board
    pos = find_empty(board)
    if not pos:
        return (True, numSteps, backTrackSteps)
    
    row, col = pos 
    #Try every value in that empty spot, from 1 ~ 9
    for i in range(1,10):
        numSteps += 1
        if valid(board, i, pos):
            #Set board value to 'i'
            board[row][col] = i
            
            #Normal Backtracking
            solved, numSteps, backTrackSteps = solve_backtrack(board, numSteps, backTrackSteps)
            
            if solved: return (True, numSteps, backTrackSteps)
            board[row][col] = '?' #If cannot solve, backtrack and reset last element to empty('?')    
            backTrackSteps += 1

    return (False, numSteps, backTrackSteps)


'''Check if number can be placed into the position without violating any rules'''
def valid(board, num, pos):
    #Position is a tuple of (row, col)
    row, col = pos

    #Check row
    for i in range (len(board[0])):
        if (board[row][i] == num and col != i):
            return False

    #Check column
    for r in range (len(board)):
        if (board[r][col] == num and row != r):
            return False

    #Check Box (3 x 3 cube)
    box_X = (col // 3) * 3
    box_Y = (row // 3) * 3

    for x in range(box_Y, box_Y + 3):
        for y in range(box_X, box_X + 3):
            if (board[x][y] == num and (x,y) != pos):
                return False
    return True


'''Find the next empty spot in the sudoku puzzle and return its coordinates'''
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == "?"):
                return (i, j) #(row, col)
    return None


'''Check if starting board is solvable'''    
def check_Init_Board(board):
    for x in range(9):
        for y in range(9):
            val =  board[x][y]
            if val != '?' and not valid(board, val, (x, y)):
                return False
            elif val != '?':
                board[x][y] = int(board[x][y]) #Transforom string to int number
    return True


'''Print the board'''
def print_board(board):
    print()
    for i in range(len(board)):
        if (i % 3 == 0):
            print("- - - - - - - - - - - - - - -")

        for j in range(len(board[i])):
            if (j % 3 == 0):
                print(" | ", end = "")

            if (j == 8):
                print(f"{board[i][j]} | ")
            else: 
                print(f"{board[i][j]} ", end = "")
        
        if (i == 8):
            print("- - - - - - - - - - - - - - -\n")

#Use this as a test board
board = [
    ['1', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '2', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '3', '?', '?', '?', '?', '?', '?'],
    
    ['?', '?', '?', '4', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '5', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '6', '?', '?', '?'],

    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?']
]

#TESTING PURPOSES
# print_board(board)
# solved, steps, backTrackSteps = solve_backtrack(board, 0, 0)
# if solved:
#     print("Sudoku is solvable.")
#     print(f"Number of steps: {steps}")
#     print(f"Number of backtracks: {backTrackSteps}")
#     print_board(board)
# else:
#     print("Sudoku is not solvable.")
