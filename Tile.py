#SUDOKU SOLVER with Backtracking Algrotihm
#JOHN MILTON PONCE

# Import and initialize the pygame library
import pygame
pygame.font.init()


'''Represent a single tile in a Sudoku 
   Note that this Sudoku will be (9 x 9) tiles'''
class Tile:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value 
        self.row = row
        self.col = col
        self.width = width
        self.height = height

        #Check if this particular tile is selected
        #If true, then user can modify the value of the tile
        self.selected = False

        #Answer will be drawn in red
        self.answer = True if value is '?' else False


    '''Draw the tile'''
    def draw(self, screen):
        font = pygame.font.SysFont("comicsans", 40)
        
        #Initialize the coordinates to draw the tile
        space = self.width / 9
        x = self.col * space
        y = ((self.height - self.width) * (5/9)) + (self.row * space) #Title Space
        
        text_Color = (0, 100, 100) if self.answer else (0, 0, 0)
        if (not self.value == '?'):
            text = font.render(str(self.value), True, text_Color)
             # blit ~ Update the Sudoku GUI
            screen.blit(text, ((x + space/2 - text.get_width()/2), (y + space/2 - text.get_height()/2)))
        
        #Used when editing the sudoku
        elif (self.value == '?'):
            text = font.render("", True, text_Color)
            screen.blit(text, ((x + space/2 - text.get_width()/2), (y + space/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, space, space), 3)
