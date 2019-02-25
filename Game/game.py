'''
Garfield game
Control Garfield by moving him side to side on the screen,
avoiding angry looking Jon Arbuckles. There are also tasty
looking lasagas falling in the same method of the angry Jons.
Moving from top to bottom, if you were to collide with a Jon,
then it would be game over for you. However if you were to 
collide with a tasty lasaga, it would grant you a lasaga point.
The goal is to get as many lasaga points as possible before
an angry Jon Arbuckle takes your lasaga away.
'''
'''
I cannot figure out how to make the lasagna points go up when garfield collides with the image
'''

import pygame
import time
import random

# Initiates pygame
pygame.init()

# Sets size of game display window
display_width = 1000
display_height = 800

# Colors used in creating the game
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
bright_green = (0,200,0)
bright_red = (200,0,0)
orange = (239,127,14)

# Sets width of beautiful garfield to 70px
gar_width = 100

# Sets gamedisplay/name/time for the running game
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Garfeilds Lasaga")
clock = pygame.time.Clock()

# Images inserted into the game
garImg = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/lasaga.jpg')
jonImg = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/jon.png')
background = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/mondays.jpg')
menuImg = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/gameintro.jpg')
las1Img = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/lasagna1.jpg')
las2Img = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/lasagna2.jpg')
las3Img = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/lasagna3.png')
odieImg = pygame.image.load('C:/Users/edwar/Desktop/py_apps/GoldBadgeChallenges/Python-104-GoldBadgeChallenges-master/Game/Images/odie.png')


# Sets size parameters for different images and objects
backgroundRect = background.get_rect()
size = (display_width, display_height) = background.get_size()
screen = pygame.display.set_mode(size)
jonRect = gameDisplay.blit(jonImg, (100,100))
garRect = gameDisplay.blit(garImg, (70,1))
lasagna1Rect = gameDisplay.blit(las1Img, (80,1))
lasagna2Rect = gameDisplay.blit(las2Img, (70,1))
lasagna3Rect = gameDisplay.blit(las3Img, (70,1))
odieRect = gameDisplay.blit(odieImg, (50, 1))

def odie(x,y):
    gameDisplay.blit(odieImg, (x,y))

def lasagna1(x,y):
    gameDisplay.blit(las1Img, (x,y))

def lasagna2(x,y):
    gameDisplay.blit(las2Img, (x,y))

def lasagna3(x,y):
    gameDisplay.blit(las3Img, (x,y))

# Maintains the count and displays the score of Lasaga Points in the bottom right
def lasagna_eaten(count):
    font = pygame.font.SysFont(None, 35)
    text = font.render("    Lasaga Points:"+str(count), True, black)
    gameDisplay.blit(text,((700),750))

def jon(x,y):
    gameDisplay.blit(jonImg, (x,y))

# Maintains the count of dodge and displays the number of Jon's dodged in the top left
def jons_dodged(count):
    font = pygame.font.SysFont(None, 35)
    text = font.render("    Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
  
def monday():
    gameDisplay.blit(mondayImg, (display_width,display_height))

def gar(x,y):
    gameDisplay.blit(garImg, (x,y))

# Sets all text objects used to be in black text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Defines how the initial message will be displayed 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(4)
    game_loop()

def crash():
    
    gameDisplay.fill(orange)
    largeText = pygame.font.SysFont("comicsansms",95)
    TextSurf, TextRect = text_objects("Jon Has Slain You", largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        start_button("Consume",350,450,100,50,green,bright_green,game_loop)
        quit_button("Quit",550,450,100,50,red,bright_red,quit)

        pygame.display.update()
        clock.tick(15)

# Button that when pressed starts the game
def start_button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

# Button that when pressed closses the application
def quit_button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
    return True

# Starts the introduction screen of the game
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(orange)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Garfields Lasaga", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        start_button("Consume",350,450,100,50,green,bright_green,game_loop)
        quit_button("Sleep",550,450,100,50,red,bright_red,"quit")

        pygame.display.update()
        clock.tick(15)
    
def game_loop():

    #Places Garfield onto the screen in the position based on the display window's size
    x = (display_width *0.45)
    y = (display_height * 0.85)
    
    #Initial values for the movement of Garfield
    #y_change = 0       # <--- If uncommented with the y axis movement commands, allows garfield to move in 8 directions
    x_change = 0

    count = 0

    # Basic information for Odie element
    odie_startx = random.randrange(0, display_width)
    odie_starty = -900
    odie_speed = 8
    odie_width = 50
    odie_height = 1
    odieCount = 1

    # Base information of the start of Lasagna One
    lasagna1_startx = random.randrange(0, display_width)
    lasagna1_starty = -750
    lasagna1_speed = 5
    lasagna1_width = 60
    lasagna1_height = 1
    lasagna1Count = 1

    # Base information of the start of Lasagna Two
    lasagna2_startx = random.randrange(0, display_width)
    lasagna2_starty = -800
    lasagna2_speed = 4
    lasagna2_width = 60
    lasagna2_height = 1
    lasagna2Count = 1

    # Base information of the start of Lasagna Three
    lasagna3_startx = random.randrange(0, display_width)
    lasagna3_starty = -900
    lasagna3_speed = 3
    lasagna3_width = 60
    lasagna3_height = 1
    lasagna3Count = 1


    jon_startx = random.randrange(0, display_width)
    jon_starty = -600
    jon_speed = 7
    jon_width = 210
    jon_height = 173
    jonCount = 1
    dodged = 0

    gameExit = False
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        #y += y_change
        x += x_change 
        
        screen.blit(background, backgroundRect)

        lasagna1(lasagna1_startx,lasagna1_starty)
        lasagna1_starty += lasagna1_speed
        
        lasagna2(lasagna2_startx,lasagna2_starty)
        lasagna2_starty += lasagna2_speed

        lasagna3(lasagna3_startx,lasagna3_starty)
        lasagna3_starty += lasagna3_speed

        odie(odie_startx,odie_starty)
        odie_starty += odie_speed

        jon(jon_startx,jon_starty)
        jon_starty += jon_speed

        gar(x,y)
        jons_dodged(dodged)
        lasagna_eaten(count)

        # If garfield goes out of the boundaries of the screen, he will be slain.
        if x > display_width - gar_width or x < 0 - gar_width:
            crash()
        if y > display_height - gar_width or y < 0 - gar_width:
            crash()
        
        # Sets starting position, and speed of Jon and the Lasagna
        if jon_starty > display_height:
            jon_starty = 0 - jon_height
            jon_startx = random.randrange(0,display_width)
            dodged += 1
            jon_speed += .45
            
        if lasagna1_starty > display_height:
            lasagna1_starty = 0 - lasagna1_height
            lasagna1_startx = random.randrange(0,display_width)
            lasagna1_speed += .25


        if lasagna2_starty > display_height:
            lasagna2_starty = 0 + lasagna2_height
            lasagna2_startx = random.randrange(0,display_width)
            lasagna2_speed += .5

        if lasagna3_starty > display_height:
            lasagna3_starty = 0 - lasagna3_height
            lasagna3_startx = random.randrange(0,display_width)
            lasagna3_speed += 1

        if odie_starty > display_height:
            odie_starty = 0 - odie_height
            odie_startx = random.randrange(0,display_width)
            odie_speed += .1
        
        # Determines if a Jon has been hit, causing garfield to be slain by Jon
        if y < jon_starty+jon_height:
            print('y crossover')

            if x > jon_startx and x < jon_startx + jon_width or x+gar_width > jon_startx and x + gar_width < jon_startx+jon_width:
                print('x crossover')
                crash()

        # Determines if the one point lasagna has been hit, giving garfield one lasagna point
        if y < lasagna1_starty+lasagna1_height:
            print('y crossover')

            if x > lasagna1_startx and x < lasagna1_startx + lasagna1_width or x+gar_width > lasagna1_startx and x + gar_width < lasagna1_startx+lasagna1_width:
                print('x crossover')
                count += 1
                lasagna_eaten(count)
        # Determines if the two point lasagna has been hit, giving garfield two lasagna points.
        if y < lasagna2_starty+lasagna2_height:
            #print('y crossover')

            if x > lasagna2_startx and x < lasagna2_startx + lasagna2_width or x+gar_width > lasagna2_startx and x + gar_width < lasagna2_startx+lasagna2_width:
                #print('x crossover')
                count += 2
                lasagna_eaten(count)

        # Determines if the three point lasagna has been hit, giving garfield three lasagna points
        if y < lasagna3_starty+lasagna3_height:
            #print('y crossover')

            if x > lasagna3_startx and x < lasagna3_startx + lasagna3_width or x+gar_width > lasagna3_startx and x + gar_width < lasagna3_startx+lasagna3_width:
                #print('x crossover')
                count += 3
                lasagna_eaten(count)

        if y < odie_starty+odie_height:
            #print('y crossover')

            if x > odie_startx and x < odie_startx + odie_width or x+gar_width > odie_startx and x + gar_width < odie_startx+odie_width:
                #print('x crossover')
                count -= 1
                lasagna_eaten(count)

        pygame.display.update()
        clock.tick(60)

# What starts the game
game_intro()
game_loop()
pygame.quit()
quit()