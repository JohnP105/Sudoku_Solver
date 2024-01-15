#SUDOKU SOLVER with Backtracking Algrotihm
#JOHN MILTON PONCE

from Sudoku import*

board = [
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],

    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?', '?']
]


def main():
    #Set up the Pygame window
    pygame.init()
    width, height = 600, 720
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont("comicsans", 35)
    solve_font = pygame.font.SysFont("comicsans", 30)

    #Title Space
    titleSpace = (height - width) * (5/9) 

    #Set Title/caption
    caption = "John Milton Ponce"
    pygame.display.set_caption(caption)

    #Reset Image
    reset_img = pygame.image.load('pixelArt/Reset.png')
    reset_img.convert()   
    imgW, imgH = 50, 50
    reset_img = pygame.transform.scale(reset_img, (imgW, imgH)) #Scale it down

    reset = reset_img.get_rect()
    reset.center = (width - imgW/2 - 5), (imgH/2 + titleSpace/10)

    #Home Image
    home_img = pygame.image.load('pixelArt/Home.png')
    home_img.convert()   
    home_img = pygame.transform.scale(home_img, (imgW, imgH)) #Scale it down

    home = home_img.get_rect()
    home.center = (imgW/2 + 5), (imgH/2 + titleSpace/10)

    #Set up the Sudoku
    sudoku = Sudoku(board, 9, 9, width, height)
    unsolvable = False
    display_Steps = False
    home_Screen = True
    algorithm = None
            
    running = True
    while running:

        #EVENTS
        for event in pygame.event.get():
            #QUIT
            if event.type == pygame.QUIT:
                running = False

            #Mouse Events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Get mouse coordinates
                mouseX, mouseY = pygame.mouse.get_pos()
                
                #Home Events
                if home_Screen:
                    y = titleSpace + (height - titleSpace)/2

                    if mouseY > titleSpace and mouseY < y:
                        home_Screen = False
                        algorithm = 'Normal'
                        print('Normal BackTracking')

                    elif mouseY > y and mouseY < height:
                        home_Screen = False
                        algorithm = 'Forward Checking' 
                        print('Forward Checking' )                       

                #Check if the click is within the Sudoku
                if 0 <= mouseX <= width and 0 <= mouseY <= height:
                    # print(mouseX, mouseY)

                    #Check Retry Button
                    if reset.collidepoint(event.pos):
                        print("Reset")
                        sudoku.reset_Sudoku()
                        unsolvable = False
                        display_Steps = False

                    #Click Home Button
                    elif home.collidepoint(event.pos):
                        print("Home")
                        sudoku.reset_Sudoku()
                        unsolvable = False
                        display_Steps = False
                        home_Screen = True
                        
                    #Click Solve Button
                    elif (mouseY > (titleSpace + width)):
                        print("Solve")
                        sudoku.solve_Sudoku(algorithm)
                        print(f"Number of values TRIED: {sudoku.numSteps}")
                        print(f"Backtracking Steps: {sudoku.backtrack}")
                        if not sudoku.solve:
                            unsolvable = True
                            print("Unsolvable")
                            break
                        display_Steps = True
                        break

                    else:       
                        #Convert mouse coordinates to grid coordinates
                        row, col = sudoku.click((mouseX, mouseY - titleSpace))

                        #Check if click is within the Sudoku
                        if (row is not None) and (col is not None):
                            # Update the selected cell in sudoku
                            sudoku.select(row, col)

            #Keyboard Events
            elif event.type == pygame.KEYDOWN and not home_Screen:
                if event.key == pygame.K_1: sudoku.value_draw(1)
                elif event.key == pygame.K_2: sudoku.value_draw(2)
                elif event.key == pygame.K_3: sudoku.value_draw(3)
                elif event.key == pygame.K_4: sudoku.value_draw(4)
                elif event.key == pygame.K_5: sudoku.value_draw(5)
                elif event.key == pygame.K_6: sudoku.value_draw(6)
                elif event.key == pygame.K_7: sudoku.value_draw(7)
                elif event.key == pygame.K_8: sudoku.value_draw(8)
                elif event.key == pygame.K_9: sudoku.value_draw(9)

                #Delete Key
                elif event.key == pygame.K_BACKSPACE: sudoku.value_draw('?')

        #Main Screen
        screen.fill((255, 255, 255))

        #Home Screen
        if home_Screen:
            #Title Screen
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, titleSpace), 0) 
            pygame.draw.rect(screen, (0,0,0), (0, 0, width, titleSpace), 4) #Border
            text = font.render("Pick an Algorithm!!!", True, (2, 2, 2))

            x = (width/2 - text.get_width()/2)
            y = (titleSpace/2 - text.get_height()/2)
            screen.blit(text, ((x), y))
            
            y = (titleSpace + ((height - titleSpace) / 2))
            pygame.draw.rect(screen, (220,20,60), (0, titleSpace, width, (height-titleSpace)), 0) #Background
            pygame.draw.rect(screen, (255, 255, 255), (0, titleSpace, width, (height-titleSpace)), 4) #Border
            pygame.draw.line(screen, (255, 255, 255), (0, y), (width, y), 4) #Line-border

            #Option1 ~ Normal Backtracking
            option1 = font.render("Normal Backtracking", True, (2, 2, 2))
            x = (width / 2 - option1.get_width() / 2)
            y = (titleSpace + (height - titleSpace)/4) - option1.get_height()/2
            screen.blit(option1, (x, y))

            #Option2 ~ Backtracking w/ FC
            option2 = font.render("Backtracking w/ FC", True, (2, 2, 2))
            x = (width / 2 - option1.get_width() / 2)
            y = (titleSpace + (height - titleSpace) * 3 / 4) - option1.get_height()/2
            screen.blit(option2, (x, y))

            pygame.display.flip()
            continue
        
        #Title Screen
        pygame.draw.rect(screen, (220,20,60), (0, 0, width, titleSpace), 0) #Background
        pygame.draw.rect(screen, (220,20,60), (0, 0, width, titleSpace), 4) #Border
        if display_Steps:
            text = solve_font.render(f"BACKTRACKING STEPS: {sudoku.backtrack}", True, (0, 255, 0))
            screen.blit(text, ((width/2 - text.get_width()/2), (titleSpace/2 - text.get_height()/2)))
        else:
            text = font.render("SUDOKU SOLVER", True, (2, 2, 2))
            screen.blit(text, ((width/2 - text.get_width()/2), (titleSpace/2 - text.get_height()/2)))


        #Reset Button
        screen.blit(reset_img, reset)
        #Home Button
        screen.blit(home_img, home)

        #Unsolvable Screen
        if unsolvable:
            pygame.draw.rect(screen, (0,0,0), (0, titleSpace, width, height-titleSpace), 4) #Border
            text = font.render("UNSOLVABLE!", True, (2, 2, 2))    
            screen.blit(text, ((width/2 - text.get_width()/2), (height/2 - text.get_height()/2)))
            screen.blit(reset_img, reset)
            screen.blit(home_img, home)
            pygame.display.flip()
            continue

        #Sudoku Screen
        sudoku.draw(screen)

        #Solve_Button Screen
        y = titleSpace + width
        pygame.draw.rect(screen, (220,20,60), (0, y+4, width, (height - width - titleSpace)-4), 0) #Background
        pygame.draw.rect(screen, (220,20,60), (0, y+4, width, (height - width - titleSpace)-4), 4) #Border

        if display_Steps:
            text = solve_font.render(f"NUMBER of VALUES TRIED: {sudoku.numSteps}", True, (0, 255, 0))
            screen.blit(text, ((width/2 - text.get_width()/2), (height - titleSpace) + text.get_height()*2/5))
        else:
            text = font.render("CLICK HERE TO SOLVE!!!", True, (2, 2, 2))
            screen.blit(text, ((width/2 - text.get_width()/2), y))

        #Update Window
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
