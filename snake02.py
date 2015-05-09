

## glich: if you press two adjacent directions in quick succession you can go back on yourself
## area for improvemnt increase speed after eats
## glich: food can spawn inside the snake


import pygame, sys, random
from pygame.locals import*

def genRanBox():
    global ranXpos 
    global ranYpos
    ranXpos = random.randrange(1,50)*10
    ranYpos = random.randrange(1,40)*10

def moveLEADbox(boxLEAD,numboxes,Train):

    if boxLEAD[2] == 'right':
        boxLEAD[0] += 10
    elif boxLEAD[2] == 'left':
            boxLEAD[0] -= 10
    elif boxLEAD[2] == 'up':
            boxLEAD[1] -= 10
    elif boxLEAD[2] == 'down':
            boxLEAD[1] += 10

    if boxLEAD[0] == 0 or boxLEAD[0] == 500 or boxLEAD[1] == 0 or boxLEAD[1] == 400:
        print "out of bounds"
        return True
    if numboxes > 1:
        for j in range(1,len(Train)):
            if boxLEAD[0] == Train[j-1][0] and boxLEAD[1] == Train[j-1][1]:
                print boxLEAD, Train[j]
                print "self eaten"
                return True
    

    return False
    
pygame.init()

#set up window
FPS = 24
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Snake!')

#define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255,0,0)

#Game rules
GameOver = False

def PlayGame(GameOver):
    genRanBox()
    boxLEAD = [250,150,'right']
    Train = [boxLEAD[0],boxLEAD[1]]
    numboxes = 0
    ranBox = [[ranXpos, ranYpos],[0,0]]
    while GameOver == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    #controls using arrow keys
            if event.type == KEYDOWN and event.key == K_UP and boxLEAD[2] != 'down':
                    boxLEAD[2] = 'up'
            elif event.type == KEYDOWN and event.key == K_DOWN and boxLEAD[2] != 'up':
                    boxLEAD[2] = 'down'
            elif event.type == KEYDOWN and event.key == K_LEFT and boxLEAD[2] != 'right':
                    boxLEAD[2] = 'left'     
            elif event.type == KEYDOWN and event.key == K_RIGHT and boxLEAD[2] != 'left':
                    boxLEAD[2] = 'right'
        

    #delete the previous box

        
        Train.insert(0,([boxLEAD[0],boxLEAD[1]]))
        Train.pop()
        GameOver = moveLEADbox(boxLEAD,numboxes,Train)
        
        
    # offscreen = otherside of the screen

            
    #constant motion of the box
        
        
        if boxLEAD[0] >= ranBox[0][0] -9 and boxLEAD[0] <= ranBox[0][0] +9 and boxLEAD[1] >= ranBox[0][1] -9 and boxLEAD[1] <= ranBox[0][1] + 9:
            genRanBox()
            ranBox[1]= ranBox[0]
            ranBox[0] = [ranXpos, ranYpos]
            numboxes +=1
            Train.insert(0,[boxLEAD[0],boxLEAD[1]])

        pygame.draw.rect(DISPLAYSURF, BLACK, (Train[numboxes][0],Train[numboxes][1],10,10))
        pygame.draw.rect(DISPLAYSURF, GREEN, (boxLEAD[0],boxLEAD[1],10,10))
        pygame.draw.rect(DISPLAYSURF, GREEN, (ranBox[0][0],ranBox[0][1],10,10))

        pygame.display.update()
        fpsClock.tick(FPS)
        print Train
        print " "
    return numboxes

print "You collected " + str(PlayGame(GameOver)) +" boxes"


print "Game Over"

DISPLAYSURF.fill(RED)
pygame.display.update()
