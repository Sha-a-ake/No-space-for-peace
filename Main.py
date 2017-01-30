import pygame, sys, Gen
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

def Draw_Humie():
    DISP.blit(Humie,(HumieX*24,HumieY*24))

pygame.init()
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')

MAP = Gen.Create_Map(16,12)
Draw(); Draw_Humie()

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
            Draw(); Draw_Humie()
            
            
    pygame.display.update()
    FpsClock.tick(FPS)        
