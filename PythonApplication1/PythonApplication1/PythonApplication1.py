import pygame
import random

""" Main Program """
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
snowColor = (169,169,169)
 
# Global constants
global idleCount
global walkCount
global right 
global left
global idle 
global jump

global X2
global background
X2 = 0

background = pygame.transform.scale(pygame.image.load("3_game_background.png"), (SCREEN_WIDTH*2, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()

        self.right = False
        self.left = False
        self.idle = True
        self.jump = False
 
        # This could also be an image loaded from the disk.
        self.idling = [pygame.transform.scale(pygame.image.load("Idle (1).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (1).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (2).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (3).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (4).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (5).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (6).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (7).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (8).png"), (100, 190)),
            pygame.transform.scale(pygame.image.load("Idle (9).png"), (100, 190))]
        self.runRight = [pygame.transform.scale(pygame.image.load("Run (1).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (2).png"), (100, 200)),
            pygame.transform.scale(pygame.image.load("Run (3).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (4).png"), (100, 200)),
            pygame.transform.scale(pygame.image.load("Run (5).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (6).png"), (100, 200)),
            pygame.transform.scale(pygame.image.load("Run (7).png"), (100, 200)), 
            pygame.transform.scale(pygame.image.load("Run (8).png"), (100, 200))]
        self.runLeft = [pygame.transform.scale(pygame.image.load("lRun (1).png"), (100, 200)),
                        pygame.transform.scale(pygame.image.load("lRun (2).png"), (100, 200)),
                        pygame.transform.scale(pygame.image.load("lRun (3).png"), (100, 200)), 
                        pygame.transform.scale(pygame.image.load("lRun (4).png"), (100, 200)),
                        pygame.transform.scale(pygame.image.load("lRun (5).png"), (100, 200)), 
                        pygame.transform.scale(pygame.image.load("lRun (6).png"), (100, 200)),
                        pygame.transform.scale(pygame.image.load("lRun (7).png"), (100, 200)), 
                        pygame.transform.scale(pygame.image.load("lRun (8).png"), (100, 200))]
        self.jumpy = [pygame.transform.scale(pygame.image.load("Jump (1).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("Jump (2).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("Jump (3).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("Jump (4).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("Jump (5).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("Jump (6).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("Jump (7).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("Jump (8).png"), (100, 200)),
           pygame.transform.scale(pygame.image.load("Jump (9).png"), (100, 200)), 
           pygame.transform.scale(pygame.image.load("Jump (10).png"), (100, 200))]
        self.die = [pygame.transform.scale(pygame.image.load("Dead (1).png"), (100,200)), 
           pygame.transform.scale(pygame.image.load("Dead (2).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (3).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (4).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (5).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (6).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (7).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (8).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (9).png"), (100,200)),
           pygame.transform.scale(pygame.image.load("Dead (10).png"), (100,200))]
        self.slide = [pygame.transform.scale(pygame.image.load("Slide (1).png"), (100,200)), 
             pygame.transform.scale(pygame.image.load("Slide (2).png"), (100,200)),
             pygame.transform.scale(pygame.image.load("Slide (3).png"), (100,200)),
             pygame.transform.scale(pygame.image.load("Slide (4).png"), (100,200)),
             pygame.transform.scale(pygame.image.load("Slide (5).png"), (100,200)),
             pygame.transform.scale(pygame.image.load("Slide (6).png"), (100,200))]
        
        self.index = 0
        self.image = self.idling[self.index]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
      
    def update(self):
        """ Move the player. """
        self.index += 1
        
        try:
            if self.right:
                if self.index >= len(self.runRight):
                    self.index = 0
                self.image = self.runRight[self.index]
            elif self.left:
                if self.index > len(self.runLeft):
                    self.index = 0
                self.image = self.runLeft[self.index]
            elif self.jump:
                if self.index >= len(self.jumpy):
                    self.index = 0
                self.image = self.jumpy[self.index]
            else:
                if self.index >= len(self.idling):
                    self.index = 0
                self.image = self.idling[self.index]
        except:
            self.update()

        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def doJump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        # Sound Effect when jumping, in jump definition of player class
        self.jump = True
        jump_sound = pygame.mixer.Sound("Jump_Sound.wav")
        pygame.mixer.Sound.play(jump_sound)

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -12
 
    # Player-controlled movement:--------------------------------------------------------------------------------------------------------------------------------
    def go_left(self, X2):
        """ Called when the user hits the left arrow. """
        self.left = True
        self.right = False
        self.jump = False
        self.idle = False
        self.change_x = -6
        X2 -=12

    def go_right(self, X2):
        """ Called when the user hits the right arrow. """
        self.left = False
        self.right = True
        self.jump = False
        self.idle = False
        self.change_x = 6
        X2 +=12
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.left = False
        self.right = False
        self.jump = False
        self.idle = True
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load("Tile (1).png"), (100, 200))
 
        self.rect = self.image.get_rect()

class Dead_Bodies(pygame.sprite.Sprite):

    def __init__(self,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image = pygame.transform.scale(pygame.image.load("Dead (10).png"),(100,100))
        self.rect = self.image.get_rect()

class Dead_Bodies2(pygame.sprite.Sprite):

    def __init__(self,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image = pygame.transform.scale(pygame.image.load("Slide (10).png"),(100,100))
        self.rect = self.image.get_rect()
 
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.bodies_list = pygame.sprite.Group()
        self.bods_list2 = pygame.sprite.Group()
        self.player = player
 
        # How far this world has been scrolled left/right
        self.world_shift = 0

    def load_music(self, song):    
        pygame.mixer.music.load(song) #the name of the music file in here
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.bodies_list.update()
        self.bods_list2.update()
 
    def draw(self, screen, X2, curr_background = background): #---------------------------------------------------------------------------------------------------------------------------------------------------
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLUE)

        X2 += 1
        screen.blit(curr_background,(X2,0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.bodies_list.draw(screen)
        self.bods_list2.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for bodies in self.bodies_list:
            bodies.rect.x += shift_x

 # Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
        background = pygame.transform.scale(pygame.image.load("3_game_background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background, (0,0))
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -1000

        song = "Purple Planet Music - Tense - Stalking the Prey (1_20) 92bpm.mp3"
        self.load_music(song)
 
        # Array with width, height, x, and y of platform
        level = [[1000, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]

        #array of dead bodies
        arr_bods = [[100,100,200,450],
                    [100,100, 300, 450],
                    [100,100, 100, 450],
                    [100, 100,400, 450]
                    ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for b in arr_bods:
            ent = Dead_Bodies(b[0], b[1])
            ent.rect.x = b[2]
            ent.rect.y = b[3]
            self.bodies_list.add(ent)


 # Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 450, 570],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 280]]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

                # Array with type of platform, and x, y location of the platform.
        bods_list2 =  [[100,100,200,450],
                    [100,100, 300, 450],
                    [100,100, 100, 450],
                    [100, 100,400, 450]
                    ]

        for b in bods_list2:
            ent = Dead_Bodies2(b[0], b[1])
            ent.rect.x = b[2]
            ent.rect.y = b[3]
            self.bodies_list.add(ent)





 
# Create platforms for the level
class Level_03(Level):
     def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -1000
        self.X2 = 0

 
        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 

# Create platforms for the level
class Level_04(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

 
        self.level_limit = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 450, 570],
                 [210, 30, 650, 420],
                 [210, 30, 700, 520],
                 [210, 30, 1120, 580],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


# Create platforms for the level
class Level_05(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

 
        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1200, 500],
                 [210, 70, 1320, 580],
                 ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)  
#--------------Display instruction page------------------#

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1

while display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 5:
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


    # Limit to 60 frames per second
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    DislpayInstructions = False
def main():
    pygame.display.set_caption("Side-scrolling Platformer")

    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
    level_list.append(Level_05(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

 
    # -------- Main Program Loop -----------
    walkCount = 0
    idleCount = 0
    jumpCount = 10

    right = True
    left = False
    idle = True
    jump = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
           player.go_left(X2)
        elif keys[pygame.K_RIGHT]:
           player.go_right(X2)
        else:
            player.stop()

        if not player.jump:
            if keys[pygame.K_SPACE]:
                player.doJump()
                player.walkCount = 0
        else:
            if player.jumpCount >= -10:
                if player.jumpCount <0:
                    player.doJump()
            else:
                player.jump = False
                player.jumpCount = 10
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                idle = True
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.idle = True
                player.stop()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()

 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen, X2)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.update()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()