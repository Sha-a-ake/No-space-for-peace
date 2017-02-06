import pygame, sys, Draw, Enemies, Func, Gen
import Config as C
from pygame.locals import *
from Const import *
from Images import *
from random import randint

pygame.init()
C.init()

# --- To remove later --- #
AreaX = 20; AreaY = 16
Gen.Create_Map(AreaX, AreaY)
Draw.Map(); 
Draw.Model(Humie,HumieX,HumieY)

# Create an enemy of chosen type
def Spawn(EnemyType, x=randint(0,AreaX-1), y=randint(0,AreaY-1)): # Spawn Enemy in x,y
    if EnemyType == 'Droid':
        Enemy = Enemies.droid
        while True:
            if C.Map[x][y][2]:
                C.Bots.append(Enemy(x,y))
                break
            else:
                x = randint(0,AreaX-1)
                y = randint(0,AreaY-1)            

# Creating a bunch oh enemies for testing                
for k in range(10):
    Spawn('Droid', k+2,k+2)

# Main game loop
while True:
    # Checking for player actions
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Humie = HumieRight
                if C.Map[HumieX+1][HumieY][2] == True and C.Map[HumieX+1][HumieY][3] == True:
                    HumieX += 1
                    
            if event.key == pygame.K_LEFT:
                Humie = HumieLeft
                if C.Map[HumieX-1][HumieY][2] == True and C.Map[HumieX-1][HumieY][3] == True:
                    HumieX -= 1
                    
            if event.key == pygame.K_UP:
                Humie = HumieUp
                if C.Map[HumieX][HumieY-1][2] == True and C.Map[HumieX][HumieY-1][3] == True:
                    HumieY -= 1
                    
            if event.key == pygame.K_DOWN:
                Humie = HumieDown
                if C.Map[HumieX][HumieY+1][2] == True and C.Map[HumieX][HumieY+1][3] == True:
                    HumieY += 1 
            if event.key == pygame.K_SPACE:

                if True:
                    for Bot in C.Bots:
                        Bot.GetHit(HumieX-1,HumieY,10)
                if True:
                    for Bot in C.Bots:
                        Bot.GetHit(HumieX+1,HumieY,10)
                if True == HumieUp:
                    for Bot in C.Bots:
                        Bot.GetHit(HumieX,HumieY-1,10)
                if True :
                    for Bot in C.Bots:
                        Bot.GetHit(HumieX,HumieY+1,10)        
                    
        # Calculating enviroment reaction  
                          
        for Bot in C.Bots:
            Bot.Move(HumieX, HumieY)
        
        DISPLAY.fill(BLACK) 
        
        # Drawing things
        Draw.Map() 
        #Draw.WalkMap()
        for Bot in C.Bots:
            Bot.Draw()
        Draw.Model(Humie,HumieX,HumieY)
        
        print(HumieX,HumieY)
        
        
    
    pygame.display.update()
    FpsClock.tick(FPS) 
    
