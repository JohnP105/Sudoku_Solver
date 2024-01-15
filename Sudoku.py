#SUDOKU SOLVER with Backtracking Algrotihm
#JOHN MILTON PONCE

from Tile import*
from backtrack import solve_backtrack
from forward_Checking import solve_backtrack_FC, np

class Sudoku:
    def __init__(self, board, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.solve = None

        #Will be used as a temporary board to solve the soduku
        #2D List containing numerical values of the Sudoku
        self.model = None

        #Variables to store info when editing a particular tile 
        self.select_cord = None

        #2D List of Tile Class
        self.tiles = []
        for r in range(rows):
            row = []
            for c in range(cols):
                val = '?'
                if board[r][c] != '?':
                    val = int(board[r][c])
                row.append(Tile(val, r, c, width, height))
            self.tiles.append(row)
                
        #Number of values tried until program is solve
        self.numSteps = 0

        #Number of backtracks
        self.backtrack = 0


    '''RESET values'''
    def reset_Sudoku(self):
        for x in range(self.rows):
            for y in range(self.cols):
             self.tiles[x][y].value = '?'  
        self.reset_Selected_Values()


    '''Solve Sudoku using NORMAL Backtracking Algorithm
        or Backtracking Algorithm w/ Forward Checking'''
    def solve_Sudoku(self, method):
        temp_Val = []
        for x in range(self.rows):
            row_values = []
            for y in range(self.cols):
                row_values.append(self.tiles[x][y].value)
                self.tiles[x][y].answer = True if self.tiles[x][y].value == '?' else False
            temp_Val.append(row_values)

        self.reset_Selected_Values()
        
        #NORMAL Backtracking Algorithm
        if method.upper() == 'NORMAL':
            self.solve, self.numSteps, self.backtrack = solve_backtrack(temp_Val, 0, 0)

        #Backtracking Algorithm w/ Forward Checking
        else:
            self.solve, self.numSteps, self.backtrack, temp_Val = solve_backtrack_FC(temp_Val, 0, 0)
            
        if not self.solve: return

         #Update Tiles value
        for x in range(self.rows):
            for y in range(self.cols):
                if method.upper() == 'NORMAL':
                    self.tiles[x][y].value = temp_Val[x][y]
                else: 
                    arr = temp_Val[x, y]
                    index = np.where(arr == -1)
                    self.tiles[x][y].value = index[0][0] + 1

        
    '''Reset all selected values back to FALSE'''
    def reset_Selected_Values(self):
        for x in range(self.rows):
             for y in range(self.cols):
                self.tiles[x][y].selected = False


    '''Draw the Sudoku'''
    def draw(self, screen):
        #Draw grid lines
        space = self.width / 9
        y = (self.height - self.width) * (5/9)  #Title Space
        for x in range(self.rows+1):
            if (x % 3 == 0):
                line_thickness = 4
            else:
                line_thickness = 1
            
            pygame.draw.line(screen, (0,0,0), (0, y + x * space), (self.width, y + x * space), line_thickness) 
            pygame.draw.line(screen, (0,0,0), (x * space, y), (x * space, self.height - (self.height - self.width - y)), line_thickness) 

        #Draw Tiles
        for x in range(self.rows):
            for y in range(self.cols):
                self.tiles[x][y].draw(screen)


    '''Select the tile based on row, col value'''
    def select(self, row, col):
        self.reset_Selected_Values()
        
        #Set new selected value
        self.tiles[row][col].selected = True    
        self.select_cord = (row, col)    


    '''Return the index of the board based on param: pos value'''
    def click(self, pos):
        x, y = pos
        if (x < self.width and y < self.height):
            space = self.width / 9
            row = y // space
            col = x // space
            return (int(row), int(col))
        return None


    '''Temporary edit the Sudoku puzzle'''
    def value_draw(self, val):
        if self.select_cord is None:
            return
        row, col = self.select_cord
        self.tiles[row][col].value = val
        self.tiles[row][col].answer = True if val is '?' else False

