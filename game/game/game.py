import pygame;

pygame.init() # initialize pygame
pygame.display.set_caption("Pumpkin Boi") # set the title of the window

size = (1500, 900) #set the size of the window
screen = pygame.display.set_mode(size) # not really sure what this does

done = False # boolean to determine if the game has been exited

clock = pygame.time.Clock() # determines how fast the screen updates


# Play the background music
pygame.mixer.music.load("bensound-creepy.mp3") #the name of the music file in here
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# boolean to trigger game over scree
#game_over = False;

#-------------Create Sprites-----------------------------#

# main guy
width = 75
height = 175
x = 0
y = 725
vel = 8

# grunts

# final boss

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
 
        text = font.render("He must die for his transgressions.", True, (255, 255, 255))
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

    background = pygame.image.load("BG.png")

    screen.blit(background,(0,0)) #place the background  image


 
# stuf to jump
isJump = False
jumpCount = 10

#stuff to slide
isSlide = False

#stuff for direction
direction = 1

#--------------Main Program Loop---------------#
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #----------Game Logic----------------------#
    keys = pygame.key.get_pressed() #get key inputs

    # moving and jumping logic
    if keys[pygame.K_LEFT]:
        direction = -1
        x -= vel
    if keys[pygame.K_RIGHT]:
        direction = 1
        x += vel
    if keys[pygame.K_DOWN] and not isSlide:
            x += direction * 2.5 * vel
            isSlide = False

    if not (isJump):
        if keys[pygame.K_UP]:
            y -= vel
        
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * .5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10



    pygame.draw.rect(screen, (255,0,0), (x,y,width, height))
    pygame.display.update()

    screen.blit(background,(0,0)) #place the background  image
    # display game over screen
    #if game_over:
    #    # If game over is true, draw game over
    #    text = font.render("Game Over", True, (255,255,255))
    #    text_rect = text.get_rect()
    #    text_x = screen.get_width() / 2 - text_rect.width / 2
    #    text_y = screen.get_height() / 2 - text_rect.height / 2
    #    screen.blit(text, [text_x, text_y])
 
    #else:
    #    # If game isn't over, draw this stuff.
    #    text = font.render("Click to end game", True, (255,255,255))
    #    text_rect = text.get_rect()
    #    text_x = screen.get_width() / 2 - text_rect.width / 2
    #    text_y = screen.get_height() / 2 - text_rect.height / 2
    #    screen.blit(text, [text_x, text_y])

    pygame.display.flip()

    clock.tick(60);

pygame.quit();