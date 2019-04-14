import pygame
import random
pygame.init()

#define color
GREY = (70, 84, 78)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
snowColor = (169, 169, 169)

#display screen
sWidth = 1100
sHeight = 630
screen = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption("Our Game")

#walking Pumpkin Boi character list
walkRight = [pygame.image.load('RWalk1.png'), pygame.image.load('RWalk2.png'),
             pygame.image.load('RWalk3.png'), pygame.image.load('RWalk4.png'),
             pygame.image.load('RWalk5.png'), pygame.image.load('RWalk6.png'),
             pygame.image.load('RWalk7.png'), pygame.image.load('RWalk8.png'),
             pygame.image.load('RWalk9.png'), pygame.image.load('RWalk10.png')]
walkLeft = [pygame.image.load('LWalk1.png'), pygame.image.load('LWalk2.png'),
             pygame.image.load('LWalk3.png'), pygame.image.load('LWalk4.png'),
             pygame.image.load('LWalk5.png'), pygame.image.load('LWalk6.png'),
             pygame.image.load('LWalk7.png'), pygame.image.load('LWalk8.png'),
             pygame.image.load('LWalk9.png'), pygame.image.load('LWalk10.png')]
background = pygame.image.load('BG.png')
character = pygame.image.load('Idle (1).png')

clock = pygame.time.Clock()

score = 0 #to start scorekeeping

#=============================================================

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x, self.y, self.width, self.height)
        #elements for hitbox: (top left x, top left y, width, height)

    def draw(self, screen):
#10 images, same image for 3 frames. Use upper bound of 30 (30/3 = 10 images)
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if not(self.standing):
            if self.left: #if we are facing left
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y)) #divide by 3
                self.walkCount += 1

            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y)) #if character is standing still
            else:
                screen.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #copied and pasted from __init__ because we must constantly redefine the hitbox
        #pygame.draw.rect(screen, RED, self.hitbox, 2) #to draw hitbox around player
#====================================================================================
class projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win): #draws bullet
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

#=============================================

class enemy():
#walking Enemy character
    walkRight = [pygame.image.load('idle_R000.png'), pygame.image.load('idle_R001.png'),
                 pygame.image.load('idle_R002.png'), pygame.image.load('idle_R003.png'),
                 pygame.image.load('idle_R004.png'), pygame.image.load('idle_R005.png')]
    walkLeft = [pygame.image.load('idle_L000.png'), pygame.image.load('idle_L001.png'),
                 pygame.image.load('idle_L002.png'), pygame.image.load('idle_L003.png'),
                 pygame.image.load('idle_L004.png'), pygame.image.load('idle_L005.png')]

    def __init__(self, x, y, width, height, end): #initialize enemy
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end] #start and end of enemy path
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.health = 10
        self.visible = True

    def draw(self, screen):
        self.move()
        if self.visible:
            if self.walkCount +1 >= 18: #6 enemy images, 3 frames. 3 x 6 = 18
                self.walkCount = 0

            if self.vel > 0: #display walkRight images if moving right
                screen.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

        pygame.draw.rect(screen, RED, (self.hitbox[0], self. hitbox[1] - 20, 50, 10))
        pygame.draw.rect(screen, GREEN, (self.hitbox[0], self.hitbox[1] - 20, 50 -(5*(10-self.health)), 10))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 5) #draws hitbox around enemy

    def move(self):
        if self.vel > 0: #if moving right
            if self.x < self.path[1] + self.vel: #if haven't reached the furthest right on our path
                self.x += self.vel
            else: #change direction and move back the other way
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else: #if moving left
            if self.x > self.path[0] - self.vel: #if haven't reached furthest left point
                self.x += self.vel
            else: #change direction
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0  

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

#=====================================================================================

def redrawGameWindow():
    screen.blit(background, (0,0)) #draws background image at (0,0)
    text = font.render('Score: ' + str(score), 1, WHITE)
    screen.blit(text, (sWidth//1.15, sHeight//20))
    pBoi.draw(screen)
    ghost.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

#=============main loop=========

font = pygame.font.SysFont('comicsans', 30, True)
pBoi = player(100, 410, 64, 84) #position of character and pixel size
ghost = enemy(800, 410, 80, 82, (sWidth//1.2)) #x,y, pixel, pixel, end x-coord
shootLoop = 0
bullets = [] #a list that will store all of the bullet objects

run = True

while run:
    clock.tick(30) #delays the game by the given amount of milliseconds (0.1 secs)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop >3:
        shootLoop = 0

    for event in pygame.event.get(): #loops through a list of any keyboard or mouse event
        if event.type == pygame.QUIT:
            run = False #ends game loop

    for bullet in bullets:
        if bullet.y - bullet.radius < ghost.hitbox[1] + ghost.hitbox[3] and bullet.y + bullet.radius > ghost.hitbox[1]: #checks x-coords
                if bullet.x + bullet.radius > ghost.hitbox[0] and bullet.x - bullet.radius < ghost.hitbox[0] + ghost.hitbox[2]: #checks y-coords
                        ghost.hit() #calls enemy hit method
                        score += 1  #incrememnts score
                        bullets.pop(bullets.index(bullet)) #removes bullet from bullet list
        
        if bullet.x < sWidth and bullet.x > 0:
            bullet.x += bullet.vel #moves bullet by its velocity
        else:
            bullets.pop(bullets.index(bullet)) #removes bullet if off screen

    #moving the characters up, down, left, and right
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0: #shoots bullet
        if pBoi.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5: #makes sure we can't exceed 5 bullets on screen at once
            bullets.append(projectile(round(pBoi.x + pBoi.width//2), #creates a bullet starting at the middle of the character
                round(pBoi.y + pBoi.height//2), 6, RED, facing))     #look of bullet
            shootLoop = 1
            
    if keys[pygame.K_LEFT] and pBoi.x > pBoi.vel: #x > vel makes character not move off screen
        pBoi.x -= pBoi.vel
        pBoi.left = True
        pBoi.right = False
        pBoi.standing = False
        
    elif keys[pygame.K_RIGHT]and pBoi.x < sWidth - pBoi.width - pBoi.vel:
        pBoi.x += pBoi.vel
        pBoi.right = True
        pBoi.left = False
        pBoi.standing = False

    else:
        pBoi.standing = True
        pBoi.walkCount = 0
                
    #jumping
    if not(pBoi.isJump): #checks user is not jumping    
        if keys[pygame.K_UP]:
            pBoi.isJump = True
            pBoi.left = False
            pBoi.right = False
            pBoi.walkCount = 0
    else:
        if pBoi.jumpCount >= -10:
            pBoi.y -= (pBoi.jumpCount * abs(pBoi.jumpCount)) * 0.5
            pBoi.jumpCount -= 1
        else:
            pBoi.isJump = False
            pBoi.jumpCount = 10

    redrawGameWindow()
    
pygame.quit()
