import pygame, sys, Init
from pygame.locals import *
pygame.init()
DSP = pygame.display.set_mode((600,400))
pygame.display.set_caption('Hello World!')

# Setting up the colors
Black = (0,0,0)
White = (255,255,255)
Red   = (255,0,0)
Green = (0,255,0)
Blue  = (0,0,255)

DSP.fill(White)
pygame.draw.polygon(DSP, Red, ((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.line(DSP,Blue,(60,60),(120,60),4)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
        pygame.display.update()
        
