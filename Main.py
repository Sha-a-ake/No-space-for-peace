import pygame, sys, Gen, Func, random, Enemies, Draw
from pygame.locals import *
from Const import *
            
pygame.init()
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')

MAP = Gen.Create_Map(20,16)
Draw.Map(MAP); 

Draw.Model(Humie,HumieX,HumieY)
D1 = Enemies.droid(16,7) 
D2 = Enemies.droid(15,3)
D3 = Enemies.droid(17,10)

t = 1
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Humie = HumieRight
                if MAP[HumieX+1][HumieY][2] == True:
                    HumieX += 1
                    
            if event.key == pygame.K_LEFT:
                Humie = HumieLeft
                if MAP[HumieX-1][HumieY][2] == True:
                    HumieX -= 1
                    
            if event.key == pygame.K_UP:
                Humie = HumieUp
                if MAP[HumieX][HumieY-1][2] == True:
                    HumieY -= 1
                    
            if event.key == pygame.K_DOWN:
                Humie = HumieDown
                if MAP[HumieX][HumieY+1][2] == True:
                    HumieY += 1
                        
            DISPLAY.fill(BLACK) 
            D1.Move(HumieX,HumieY);D2.Move(HumieX,HumieY);D3.Move(HumieX,HumieY)
            
            Draw.Map(MAP) 
            Draw.Model(Humie,HumieX,HumieY)
            D1.Draw(); D2.Draw(); D3.Draw()
            MAP[7][8] = [1,1,False,False,False]
            DISPLAY.blit(WallSpVerLeft,(8*24,9*24))
            print(HumieX,HumieY)
            
            
            
    pygame.display.update()
    FpsClock.tick(FPS)        
