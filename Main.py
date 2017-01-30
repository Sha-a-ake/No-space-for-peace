import pygame, sys, Gen, Func, random, Enemies
from pygame.locals import *
from Const import *

def Draw():
    x = 0;
    for Line in MAP:
        y = 0
        x += TileSize
        for X in Line:
            y += TileSize
            if X[0] == 0: DISPLAY.blit(Tile, (x,y))
            elif X[0] == 1: DISPLAY.blit(WallHor, (x,y))
            elif X[0] == 2: DISPLAY.blit(WallVer, (x,y))
            elif X[0] == 3: DISPLAY.blit(WallSpHor, (x,y))
            elif X[0] == 4: DISPLAY.blit(WallSpVer, (x,y))
                
def DrawSquare(X1,Y1,X2,Y2):
    x = X1*24; y = Y1*24
    for Line in range(abs(X2-X1+1)):
        x = X1*24
        y += TileSize
        for X in range(abs(Y2-Y1+1)):
            x += TileSize
            DISP.blit(Tile, (x,y))
    
def DrawHumie():
    DISPLAY.blit(Humie,((HumieX+1)*24,(HumieY+1)*24))


pygame.init()
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')

MAP = Gen.Create_Map(20,16)
#Draw(); 

DrawHumie()
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
            
            Draw() 
            DrawHumie()
            D1.Draw(); D2.Draw(); D3.Draw()
            MAP[7][8] = [1,1,False,False,False]
            DISPLAY.blit(WallSpVer,(8*24,9*24))
            print(HumieX,HumieY)
            
            
            
    pygame.display.update()
    FpsClock.tick(FPS)        
