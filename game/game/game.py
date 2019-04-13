import pygame;

pygame.init() # initialize pygame
pygame.display.set_caption("Pumpkin Boi") # set the title of the window

size = (650, 500) #set the size of the window
screen = pygame.display.set_mode(size) # not really sure what this does

done = False # boolean to determine if the game has been exited

clock = pygame.time.Clock() # determines how fast the screen updates


# Play the background music
#pygame.mixer.music.load(None) #the name of the music file in here
#pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
#pygame.mixer.music.play()

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
            if instruction_page == 3:
                display_instructions = False
 
    # Set the screen background
    screen.fill((0,0,0))
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("Instructions", True, (255,255,255))
        screen.blit(text, [10, 10])
 
        text = font.render("The big bad boss boi ate your pumpkin seeds.", True, (255,255,255))
        screen.blit(text, [10, 40])
 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Instructions", True, (255, 255, 255))
        screen.blit(text, [10, 10])
 
        text = font.render("He must die for his transgressions.", True, (255, 255, 255))
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