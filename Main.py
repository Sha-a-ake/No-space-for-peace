import pygame, sys, Gen, Func
from pygame.locals import *
from Const import *

def Draw():
    x = 24; y = 24
    for Line in MAP:
        x = 0
        y += TileSize
        for X in Line:
            x += TileSize
            if X[0] == 1: DISP.blit(Tile, (x,y))
            elif X[0] == 2: DISP.blit(Wall, (x,y))
                
def DrawSquare(X1,Y1,X2,Y2):
    x = X1*24; y = Y1*24
    for Line in range(abs(X2-X1+1)):
        x = X1*24
        y += TileSize
        for X in range(abs(Y2-Y1+1)):
            x += TileSize
            DISP.blit(Tile, (x,y))
    
def DrawHumie():
    DISP.blit(Humie,(HumieX*24,HumieY*24))

pygame.init()
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')

MAP = Gen.Create_Map(16,12)
#Draw(); 

DrawHumie()

Sq = Func.MakeSquaresInCircle(25,10)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                HumieX += 1
                Humie = HumieRight
            if event.key == pygame.K_LEFT:
                HumieX -= 1
                Humie = HumieLeft
            if event.key == pygame.K_UP:
                HumieY -= 1
                Humie = HumieUp
            if event.key == pygame.K_DOWN:
                HumieY += 1
                Humie = HumieDown
                
            DISP.fill(BLACK) 
            for Room in Sq:
                DrawSquare(abs(Room[0]),abs(Room[1]),abs(Room[2]),abs(Room[3]))       
            
            #Draw(); 
            DrawHumie()
            
            
            
    pygame.display.update()
    FpsClock.tick(FPS)        
