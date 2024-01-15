#SUDOKU SOLVER with Backtracking Algrotihm
#JOHN MILTON PONCE

import numpy as np

'''Use Backtracking Algorithm
    Return True if soduku is solvable, along with the number of steps it took to solve'''
def solve_backtrack_FC(board, numSteps, backTrackSteps):
    if numSteps == 0: 
        # print('Transforming...')
        board = transform_Board(board)
        if not check_Init_Board(board): 
            print("Check Init")
            return (False, numSteps, backTrackSteps, board)

        print_board(board)
        # print(board)
        # print(f"\n\nAFTER:\n {board}")


    #Find empty spot within the board
    pos = find_empty(board)
    if not pos:
        return (True, numSteps, backTrackSteps, board)

    row, col = pos 
    pos_Values = np.where(board[row, col] == 1)[0]
    #Try every possible value in that empty spot
    for index in pos_Values:
        numSteps += 1
        temp = board.copy()
        if valid(board, index, pos): 
            # print(f"\n~ CORRECT: NUM: {index+1}, POS: {pos}: BOARD: {board[row, col]}")
            board[row, col, :] = 0
            board[row, col, index] = -1 
            
            #Normal Backtracking
            solved, numSteps, backTrackSteps, board = solve_backtrack_FC(board, numSteps, backTrackSteps)

            if solved: return (True, numSteps, backTrackSteps, board)
        
        board = temp #If cannot solve, backtrack and reset last element to empty('?') 
        backTrackSteps += 1
        
        # print(f'\n~ BACKTRACK: ~ NUM: {index+1}, BOARD: {board[row, col]}, POS: {pos}\n')
        

    return (False, numSteps, backTrackSteps, board)


'''Check if number can be placed into the position without violating any rules'''
'''Check if number can be placed into the position without violating any rules'''
def valid(board, index, pos):
    row, col = pos

    #Check row
    for i in range(9):
        val = board[row, i, index]

        if checkCount(board, (row, i), -1) and val == -1 and i != col:
            # print((f'~ WRONG: INDEX: {index}, BOARD: {board[row,i]}, POS: {row, i} ~ row2\n'))
            return False

        elif i != col:
            forward_Checking(board, index, (row,i))
            
    #Check column
    for r in range (9):
        val = board[r, col, index]
        
        if checkCount(board, (r, col), -1) and val == -1 and r != row:
            # print((f'~ WRONG: INDEX: {index}, BOARD: {board[r,col]}, POS: {r, col} ~ col2\n'))
            return False

        elif r != row:
            forward_Checking(board, index, (r,col))

    #Check Box (3 x 3 cube)
    box_X = (col // 3) * 3
    box_Y = (row // 3) * 3

    for x in range(box_Y, box_Y + 3):
        for y in range(box_X, box_X + 3):
            if x == row or y == col: continue  #Remove any checks where forward checking has already been applied in row or col
            val = board[x, y, index]

            if checkCount(board, (x,y), -1) and val == -1 and (x,y) != pos:
                # print((f'~ WRONG: INDEX: {index}, BOARD: {board[x,y]}, POS: {x, y} ~ box2\n'))
                return False

            elif (x,y) != pos:
                forward_Checking(board, index, (x,y))

    return True


def forward_Checking(board, index, pos):
    row, col = pos
    board[row, col, index] = 0


'''Find the next empty spot in the sudoku puzzle and return its coordinates'''
def find_empty(board):
    for x in range(9):
        for y in range(9):
            if not checkCount(board, (x,y), -1):
                return (x, y) #(row, col)
    return None


'''Checks how many possible values does the current location has
    returns True if more than one, otherwise False'''
def checkCount(board, pos, num):
    row, col = pos
    count = np.sum(board[row, col, :] == num)
    return count > 0


'''Tranform board into a 3D numpy array'''
def transform_Board(sudoku):
    board = np.ones((9, 9, 9), dtype=int)  # Initialize a 3D array with all possibilities set to 1
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] != '?':
                # If a value is given in the Sudoku puzzle, set the corresponding possibility array to all zeros
                board[x, y, :] = 0
                board[x, y, int(sudoku[x][y]) - 1] = -1 #Set index
    return board


'''Check if starting board is solvable'''    
def check_Init_Board(board):
    for x in range(9):
        for y in range(9):
            if checkCount(board, (x, y), -1):
                arr = board[x, y].copy()
                index = np.where(arr == -1)
                index = index[0][0]
                if not valid(board, index, (x,y)): 
                    return False
    return True


'''Print the board'''
def print_board(board):
    print()
    for i in range(9):
        if i % 3 == 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0:
                print(" | ", end="")

            if checkCount(board, (i,j), -1):
                try:
                    print(f"{np.where(board[i, j] == -1)[0][0] + 1} ", end="")
                except:
                    print("? ", end="")

            else:
                print("? ", end="")

            if j == 8:
                print("| ")
        
        if i == 8:
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
# solved, steps, backTrackSteps, board = solve_backtrack_FC(board, 0, 0)
# if solved:
#     print("\nSudoku is solvable.")
#     print(f"Number of steps: {steps}")
#     print(f"Number of backtracks: {backTrackSteps}")
#     print_board(board)
# else:
#     print("\nSudoku is not solvable.")
