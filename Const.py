import pygame
from Images import *

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

# Start
Humie = HumieUp
Droid = PreparedDroidLeft

# Windows
FpsClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WinX,WinY),0,32)

# Game constants
DroidX = 18; DroidY = 6
