import pygame, sys
from pygame.locals import *

pygame.init()
DSP = pygame.display.set_mode((600,400))
pygame.display.set_caption('Hello World!')


# Setting up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

pygame.draw.polygon(DSP, GREEN, ((146, 0), (291, 106),(236,277),(56, 277),(0,106)))
pygame.draw.line(DSP, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DSP, BLUE, (120, 60), (60, 120))
pygame.draw.line(DSP, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DSP, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DSP, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DSP, RED, (200, 150, 100, 50))

pix = pygame.PixelArray(DSP)
pix[480][380] = BLACK
pix[482][382] = BLACK
pix[484][384] = BLACK
pix[486][386] = BLACK
pix[488][388] = BLACK
del pix

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
        pygame.display.update()
        
