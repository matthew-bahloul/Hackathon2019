import pygame;

pygame.init() # initialize pygame
pygame.display.set_caption("Pumpkin Boi") # set the title of the window

size = (650, 500) #set the size of the window
screen = pygame.display.set_mode(size) # not really sure what this does

done = False # boolean to determine if the game has been exited

clock = pygame.time.Clock() # determines how fast the screen updates


# Play the background music
pygame.mixer.music.load("bensound-creepy.mp3") #the name of the music file in here
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

#--------------Display instruction page------------------#

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1


while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 6:
                display_instructions = False
 
    # Set the screen background
    screen.fill((0,0,0))
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("Intro", True, (255,255,255))
        screen.blit(text, [10, 10])
 
        text = font.render("The big bad boss boy ate your pumpkin seed.", True, (255,255,255))
        screen.blit(text, [10, 40])
 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Intro", True, (255, 255, 255))
        screen.blit(text, [10, 10])
 
        text = font.render("He will die for his transgressions.", True, (255, 255, 255))
        screen.blit(text, [10, 40])

    if instruction_page == 3:
        # Draw instructions, page 3
        text = font.render("Controls (1)", True, (255, 255, 255))
        screen.blit(text, [10, 10])
 
        text = font.render("[left arrow] [right arrow]: move left and right", True, (255, 255, 255))
        screen.blit(text, [10, 40])

    if instruction_page == 4:
        # Draw instructions, page 4
        text = font.render("Controls (2)", True, (255, 255, 255))
        screen.blit(text, [10, 10])
 
        text = font.render("[space] : jump", True, (255, 255, 255))
        screen.blit(text, [10, 40])

    if instruction_page == 5:
        # Draw instructions, page 5
        text = font.render("Controls (3)", True, (255, 255, 255))
        screen.blit(text, [10, 10])
 
        text = font.render("[down arrow] : slide", True, (255, 255, 255))
        screen.blit(text, [10, 40])

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


#--------------Main Program Loop---------------#

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #----------Game Logic----------------------#



    screen.fill((255,255,255))

    pygame.display.flip()

    clock.tick(60);

pygame.quit();