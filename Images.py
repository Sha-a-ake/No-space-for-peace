import pygame
# Room

Floor            = pygame.image.load('Level_Models/Floors/floor.png')
Plate            = pygame.image.load('Level_Models/Floors/plate.png')
Lattice          = pygame.image.load('Level_Models/Floors/floor_lattice.png')


WallVerLeft      = pygame.image.load('Level_Models/Walls/wall_vertical_left.png')
WallVerRight     = pygame.image.load('Level_Models/Walls/wall_vertical_right.png')
WallHorTop       = pygame.image.load('Level_Models/Walls/wall_horizontal_top.png')
WallHorBottom    = pygame.image.load('Level_Models/Walls/wall_horizontal_bottom.png')
WallSpVerLeft    = pygame.image.load('Level_Models/Walls/wall_special_vertical_left.png')
WallSpVerRight   = pygame.image.load('Level_Models/Walls/wall_special_vertical_right.png')
WallSpHorTop     = pygame.image.load('Level_Models/Walls/wall_special_horizontal_top.png')
WallSpHorBottom  = pygame.image.load('Level_Models/Walls/wall_special_horizontal_bottom.png')
WallCornerBL     = pygame.image.load('Level_Models/Walls/corner_bl.png')
WallCornerBR     = pygame.image.load('Level_Models/Walls/corner_br.png')
WallCornerTL     = pygame.image.load('Level_Models/Walls/corner_tl.png')
WallCornerTR     = pygame.image.load('Level_Models/Walls/corner_tr.png')


"""
D == Door
H == Holder

L == Locked
U == Unlocked
G == Glitched

C == Closed
O == Open

N == Switched On
F == Switched Off
"""

# Doors

# Locked Door

DLCFHor = pygame.image.load('Level_Models/Doors/Locked/door_main_locked_closed_off_hor.png')
DLCFVer = pygame.image.load('Level_Models/Doors/Locked/door_main_locked_closed_off_ver.png')
DLCNHor = pygame.image.load('Level_Models/Doors/Locked/door_main_locked_closed_on_hor.png')
DLCNVer = pygame.image.load('Level_Models/Doors/Locked/door_main_locked_closed_on_ver.png')

# Unlocked Door

DUCFHor = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_closed_off_hor.png')
DUCFVer = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_closed_off_ver.png')
DUCNHor = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_closed_on_hor.png')
DUCNVer = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_closed_on_ver.png')
DUOFHor = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_open_off_hor.png')
DUOFVer = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_open_off_ver.png')
DUONHor = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_open_on_hor.png')
DUONVer = pygame.image.load('Level_Models/Doors/Unlocked/door_main_unlocked_open_on_ver.png')

# Glitched Door

DGCFHor = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_closed_off_hor.png')
DGCFVer = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_closed_off_ver.png')
DGCNHor = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_closed_on_hor.png')
DGCNVer = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_closed_on_ver.png')
DGOFHor = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_open_off_hor.png')
DGOFVer = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_open_off_ver.png')
DGONHor = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_open_on_hor.png')
DGONVer = pygame.image.load('Level_Models/Doors/Glitched/door_main_glitched_open_on_ver.png')


# Holders

# Locked Holder

HLCFDown  = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_off_down.png')
HLCFLeft  = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_off_left.png')
HLCFRight = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_off_right.png')
HLCFUp    = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_off_up.png')

HLCNDown  = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_on_down.png')
HLCNLeft  = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_on_left.png')
HLCNRight = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_on_right.png')
HLCNUp    = pygame.image.load('Level_Models/Doors/Locked/door_locked_closed_on_up.png')

# Unlocked Holder

HUCFDown  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_off_down.png')
HUCFLeft  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_off_left.png')
HUCFRight = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_off_right.png')
HUCFUp    = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_off_up.png')

HUCNDown  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_on_down.png')
HUCNLeft  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_on_left.png')
HUCNRight = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_on_right.png')
HUCNUp    = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_closed_on_up.png')

HUOFDown  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_off_down.png')
HUOFLeft  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_off_left.png')
HUOFRight = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_off_right.png')
HUOFUp    = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_off_up.png')

HUONDown  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_on_down.png')
HUONLeft  = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_on_left.png')
HUONRight = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_on_right.png')
HUONUp    = pygame.image.load('Level_Models/Doors/Unlocked/door_unlocked_open_on_up.png')


# Glitched Holder

HGCFDown  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_off_down.png')
HGCFLeft  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_off_left.png')
HGCFRight = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_off_right.png')
HGCFUp    = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_off_up.png')

HGCNDown  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_on_down.png')
HGCNLeft  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_on_left.png')
HGCNRight = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_on_right.png')
HGCNUp    = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_closed_on_up.png')

HGOFDown  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_off_down.png')
HGOFLeft  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_off_left.png')
HGOFRight = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_off_right.png')
HGOFUp    = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_off_up.png')

HGONDown  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_on_down.png')
HGONLeft  = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_on_left.png')
HGONRight = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_on_right.png')
HGONUp    = pygame.image.load('Level_Models/Doors/Glitched/door_glitched_open_on_up.png')


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

DeadDroidLeft       = pygame.image.load('Enemies/Droid/Dead/droid_left.png')
DeadDroidRight      = pygame.image.load('Enemies/Droid/Dead/droid_right.png')
DeadDroidUp         = pygame.image.load('Enemies/Droid/Dead/droid_up.png')
DeadDroidDown       = pygame.image.load('Enemies/Droid/Dead/droid_down.png')

BulletVer       = pygame.image.load('Misc/Bullet/bullet_vertical.png')
BulletHor       = pygame.image.load('Misc/Bullet/bullet_horizontal.png')

