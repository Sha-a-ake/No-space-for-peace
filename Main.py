import pygame, sys
from pygame.locals import *

FPS = 30
FpsClock = pygame.time.Clock()

pygame.init()
DSP = pygame.display.set_mode((600,400),0,32)
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')

# Setting up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

CatImg = pygame.image.load('cat.jpg')
catx = 10
caty = 10
direction = 'right'

DSP.fill(WHITE)

while True:
    if direction == 'right':
        catx += 5
        if catx == 500:
            direction = 'left'
    elif direction == 'left':
        catx-= 5
        if catx == 10:
            direction = 'right'
    
    DSP.blit(CatImg,(catx,caty))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    FpsClock.tick(FPS)        
