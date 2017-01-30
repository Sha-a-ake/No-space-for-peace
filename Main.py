import pygame, sys, Gen
from pygame.locals import *
from Constants import *


def draw():
    x = 10; y = 10
    for Line in MAP:
        x = 0
        y += TileSize
        for X in Line:
            x += TileSize
            if X[0] == 1: DISP.blit(Tile, (x,y))



FpsClock = pygame.time.Clock()



pygame.init()
DISP = pygame.display.set_mode((WinX,WinY),0,32)
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')



MAP = Gen.Create_Map(20,2)

xx = 0; yy = 0
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xx += 16
            if event.key == pygame.K_LEFT:
                xx -= 16
            if event.key == pygame.K_UP:
                yy -= 16
            if event.key == pygame.K_DOWN:
                yy += 16
                       
            DISP.fill(BLACK) 
            draw()
            
            
    pygame.display.update()
    FpsClock.tick(FPS)        

