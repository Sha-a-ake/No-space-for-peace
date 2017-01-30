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
Tile        = pygame.image.load('Level_Models/floor.png')
WallVer     = pygame.image.load('Level_Models/wall_vertical.png')
WallHor     = pygame.image.load('Level_Models/wall_horizontal.png')
WallSpVer   = pygame.image.load('Level_Models/wall_special_vertical.png')
WallSpHor   = pygame.image.load('Level_Models/wall_special_horizontal.png')
HumieLeft   = pygame.image.load('Humie/humie_left.png')
HumieRight  = pygame.image.load('Humie/humie_right.png')
HumieUp     = pygame.image.load('Humie/humie_up.png')
HumieDown   = pygame.image.load('Humie/humie_down.png')
DroidLeft   = pygame.image.load('Enemies/Droid/droid_left.png')
DroidRight  = pygame.image.load('Enemies/Droid/droid_right.png')
DroidUp     = pygame.image.load('Enemies/Droid/droid_up.png')
DroidDown   = pygame.image.load('Enemies/Droid/droid_down.png')
BulletVer   = pygame.image.load('Misc/Bullet/bullet_vertical.png')
BulletHor   = pygame.image.load('Misc/Bullet/bullet_horizontal.png')

#Start
Humie = HumieUp
Droid = DroidLeft

# Windows
FpsClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WinX,WinY),0,32)

# Game constants
HumieX = 1; HumieY = 1
DroidX = 18; DroidY = 6
