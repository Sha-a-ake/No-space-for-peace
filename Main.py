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

def Spawn(EnemyType, x=randint(0,AreaX-1), y=randint(0,AreaY-1)): # Spawn Enemy in x,y
    if EnemyType == 'Droid':
        Enemy = Enemies.droid
        while True:
            if C.Map[x][y][2]:
                C.Bots.append(Enemy(x,y))
                C.Map[x][y][2] = False
                break
            else:
                x = randint(0,AreaX-1)
                y = randint(0,AreaY-1)            
        
for k in range(10):
    Spawn('Droid')

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
                if C.Map[HumieX+1][HumieY][2] == True:
                    HumieX += 1
                    
            if event.key == pygame.K_LEFT:
                Humie = HumieLeft
                if C.Map[HumieX-1][HumieY][2] == True:
                    HumieX -= 1
                    
            if event.key == pygame.K_UP:
                Humie = HumieUp
                if C.Map[HumieX][HumieY-1][2] == True:
                    HumieY -= 1
                    
            if event.key == pygame.K_DOWN:
                Humie = HumieDown
                if C.Map[HumieX][HumieY+1][2] == True:
                    HumieY += 1         
                    
        # Calculating enviroment reaction  
                          
        for Bot in C.Bots:
            Bot.Move(HumieX, HumieY)
            
        
        DISPLAY.fill(BLACK) 
        
        #Drawing things
        C.Map[6][6] = [1,1,True,False,False]
        DISPLAY.blit(Lattice,(7*24,7*24))
            
        C.Map[7][8] = [1,1,False,False,False]
        DISPLAY.blit(HGONDown,(8*24,9*24))
        C.Map[7][9] = [1,1,True,False,False]
        DISPLAY.blit(DGONVer,(8*24,10*24))
        C.Map[7][10] = [1,1,True,False,False]
        DISPLAY.blit(DGONVer,(8*24,11*24))
        C.Map[7][11] = [1,1,True,False,False]
        DISPLAY.blit(DGONVer,(8*24,12*24))
        C.Map[7][12] = [1,1,False,False,False]
        DISPLAY.blit(HGONUp,(8*24,13*24))
        
         
        C.Map[8][8] = [1,1,False,False,False]
        DISPLAY.blit(HGCNDown,(9*24,9*24))
        C.Map[8][9] = [1,1,False,False,False]
        DISPLAY.blit(DGCNVer,(9*24,10*24))
        C.Map[8][10] = [1,1,False,False,False]
        DISPLAY.blit(DGCNVer,(9*24,11*24))
        C.Map[8][11] = [1,1,False,False,False]
        DISPLAY.blit(DGCNVer,(9*24,12*24))
        C.Map[8][12] = [1,1,False,False,False]
        DISPLAY.blit(HGCNUp,(9*24,13*24))
       
        
        Draw.Map() 
        Draw.Model(Humie,HumieX,HumieY)
        
        for Bot in C.Bots:
            Bot.Draw()
    
    pygame.display.update()
    FpsClock.tick(FPS) 
    
