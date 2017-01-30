import pygame, sys
from pygame.locals import *

FPS = 30
FpsClock = pygame.time.Clock()

pygame.init()
DISP = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')

# Setting up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

MAP = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

px = 4; py = 4;

Tile = pygame.image.load('floor.png')

def draw(o,s):
    x = o; y = s
    for Line in MAP:
        x = o
        y += 16
        for X in Line:
            x += 16
            if X == 0: DISP.blit(Tile, (x,y))

draw(0,0)
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
            draw(xx,yy)
            
            
    pygame.display.update()
    FpsClock.tick(FPS)        
