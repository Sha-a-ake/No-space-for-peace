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

# Room
Tile             = pygame.image.load('Level_Models/floor.png')
WallVerLeft      = pygame.image.load('Level_Models/wall_vertical_left.png')
WallVerRight     = pygame.image.load('Level_Models/wall_vertical_right.png')
WallHorTop       = pygame.image.load('Level_Models/wall_horizontal_top.png')
WallHorBottom    = pygame.image.load('Level_Models/wall_horizontal_bottom.png')
WallSpVerLeft    = pygame.image.load('Level_Models/wall_special_vertical_left.png')
WallSpVerRight   = pygame.image.load('Level_Models/wall_special_vertical_right.png')
WallSpHorTop     = pygame.image.load('Level_Models/wall_special_horizontal_top.png')
WallSpHorBottom  = pygame.image.load('Level_Models/wall_special_horizontal_bottom.png')
WallCornerBL     = pygame.image.load('Level_Models/corner_bl.png')
WallCornerBR     = pygame.image.load('Level_Models/corner_br.png')
WallCornerTL     = pygame.image.load('Level_Models/corner_tl.png')
WallCornerTR     = pygame.image.load('Level_Models/corner_tr.png')

# Characters
HumieLeft       = pygame.image.load('Humie/humie_left.png')
HumieRight      = pygame.image.load('Humie/humie_right.png')
HumieUp         = pygame.image.load('Humie/humie_up.png')
HumieDown       = pygame.image.load('Humie/humie_down.png')

CalmDroidLeft       = pygame.image.load('Enemies/Droid/Calm/droid_left.png')
CalmDroidRight      = pygame.image.load('Enemies/Droid/Calm/droid_right.png')
CalmDroidUp         = pygame.image.load('Enemies/Droid/Calm/droid_up.png')
CalmDroidDown       = pygame.image.load('Enemies/Droid/Calm/droid_down.png')

AngryDroidLeft       = pygame.image.load('Enemies/Droid/Angry/droid_left.png')
AngryDroidRight      = pygame.image.load('Enemies/Droid/Angry/droid_right.png')
AngryDroidUp         = pygame.image.load('Enemies/Droid/Angry/droid_up.png')
AngryDroidDown       = pygame.image.load('Enemies/Droid/Angry/droid_down.png')

PreparedDroidLeft       = pygame.image.load('Enemies/Droid/Prepared/droid_left.png')
PreparedDroidRight      = pygame.image.load('Enemies/Droid/Prepared/droid_right.png')
PreparedDroidUp         = pygame.image.load('Enemies/Droid/Prepared/droid_up.png')
PreparedDroidDown       = pygame.image.load('Enemies/Droid/Prepared/droid_down.png')

BulletVer       = pygame.image.load('Misc/Bullet/bullet_vertical.png')
BulletHor       = pygame.image.load('Misc/Bullet/bullet_horizontal.png')

# Start
Humie = HumieUp
Droid = PreparedDroidLeft

# Windows
FpsClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WinX,WinY),0,32)

# Game constants
HumieX = 1; HumieY = 1
DroidX = 18; DroidY = 6
