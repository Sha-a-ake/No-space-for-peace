import pygame, sys, Draw, Enemies, Func, Gen
import Config as C
from pygame.locals import *
from Const import *
from Images import *

pygame.init()
C.init()

# --- To remove later --- #
Gen.Create_Map(20,16)
Draw.Map(); 
Draw.Model(Humie,HumieX,HumieY)
D1 = Enemies.droid(16,7) 
D2 = Enemies.droid(15,3)
D3 = Enemies.droid(17,10)

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
        D1.Move(HumieX,HumieY);D2.Move(HumieX,HumieY);D3.Move(HumieX,HumieY)
        
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
        #C.Map[7][12] = [1,1,False,False,False]
        #DISPLAY.blit(HGONUp,(8*24,13*24))
        
         
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
        D1.Draw(); D2.Draw(); D3.Draw()
    
    pygame.display.update()
    FpsClock.tick(FPS) 
    
