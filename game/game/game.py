import pygame
import random

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

#-------------Draw Stuff--------------------------------#
def redrawScreen():
    global walkCount
    screen.blit(background,(0,0)) #place the background  image

    if walkCount > 9:
        walkCount = 0

    if isJump:
        screen.blit(jump[walkCount//3], (x,y))
    elif left:
        screen.blit(runLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(runRight[walkCount//3], (x,y))
        walkCount += 1
    
    else:
        screen.blit(char, (x,y))

    pygame.display.update()

#--------------snow stuff-----------------------------------------#
#falling snow obstacle that'll kill our character
SnowObstacle = []
snowColor = (169, 169, 169)

for q in range (5):
    x = random.randrange(0, 1110)
    y = random.randrange(0, 590)
    SnowObstacle.append([x,y])

def snowFall():
    #snow obstacle
    for i in SnowObstacle:
        i[1]+=1
        pygame.draw.circle(screen, snowColor, i, 60)

        if i[1] > 590:
            i[1]= random.randrange(-50, -5)
            i[0] = random.randrange(1110)

#-------------Create Sprites-----------------------------#

# main guy
idle = [pygame.transform.scale(pygame.image.load("Idle (1).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Idle (2).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Idle (3).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Idle (4).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Idle (5).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Idle (6).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Idle (7).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Idle (8).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Idle (9).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Idle (10).png"), (100, 200))]
runRight = [pygame.transform.scale(pygame.image.load("Run (1).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (2).png"), (100, 200)),
            pygame.transform.scale(pygame.image.load("Run (3).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (4).png"), (100, 200)),
            pygame.transform.scale(pygame.image.load("Run (5).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (6).png"), (100, 200)),
            pygame.transform.scale(pygame.image.load("Run (7).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (8).png"), (100, 200))]
runLeft = [pygame.transform.scale(pygame.image.load("lRun (1).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("lRun (2).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("lRun (3).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("lRun (4).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("lRun (5).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("lRun (6).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("lRun (7).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("lRun (8).png"), (100, 200))]
jump = [pygame.transform.scale(pygame.image.load("Jump (1).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Jump (2).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Jump (3).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Jump (4).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Jump (5).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Jump (6).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Jump (7).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Jump (8).png"), (100, 200)),
        pygame.transform.scale(pygame.image.load("Jump (9).png"), (100, 200)), 
        pygame.transform.scale(pygame.image.load("Jump (10).png"), (100, 200))]
die = [pygame.transform.scale(pygame.image.load("Dead (1).png"), (100,200)), 
       pygame.transform.scale(pygame.image.load("Dead (2).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (3).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (4).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (5).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (6).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (7).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (8).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (9).png"), (100,200)),
       pygame.transform.scale(pygame.image.load("Dead (10).png"), (100,200))]
slide = [pygame.transform.scale(pygame.image.load("Slide (1).png"), (100,200)), 
         pygame.transform.scale(pygame.image.load("Slide (2).png"), (100,200)),
         pygame.transform.scale(pygame.image.load("Slide (3).png"), (100,200)),
         pygame.transform.scale(pygame.image.load("Slide (4).png"), (100,200)),
         pygame.transform.scale(pygame.image.load("Slide (5).png"), (100,200)),
         pygame.transform.scale(pygame.image.load("Slide (6).png"), (100,200))]

char = pygame.transform.scale(pygame.image.load("Idle (1).png"), (100, 200))

width = 10
height = 10
x = 0
y = 725
vel = 8
left = False
right = False
walkCount = 0

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
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
    if keys[pygame.K_RIGHT]:
        x += vel
        left = False
        right = True
    #if keys[pygame.K_DOWN]:
    #        x += direction * 2.5 * vel
    else:
        right = False
        left = False
        walkCount = 0

    if not (isJump):
       if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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
    redrawScreen()

    snowFall()

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

    clock.tick(30);

pygame.quit();