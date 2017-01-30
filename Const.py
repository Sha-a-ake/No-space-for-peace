import pygame

TileSize = 24
FPS = 120

# Resolution
WinX = 640
WinY = 480

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

# Images
Tile = pygame.image.load('Level_Models/floor.png')
Wall = pygame.image.load('Level_Models/wall.png')
HumieLeft = pygame.image.load('Humie/humie_left.png')
HumieRight = pygame.image.load('Humie/humie_right.png')
HumieUp = pygame.image.load('Humie/humie_up.png')
HumieDown = pygame.image.load('Humie/humie_down.png')
Humie = HumieUp

# Windows
FpsClock = pygame.time.Clock()
DISP = pygame.display.set_mode((WinX,WinY),0,32)

# Game constants
HumieX = 4; HumieY = 4
