from Images import HumieUp

def init():
    global TileMap
    global WalkMap
    global IdMap
    TileMap = []
    WalkMap = []
    IdMap = []
    global Bots
    Bots = []
    global Misc
    Misc = []
    global Humie
    global HumieX
    global HumieY
    global Move
    Humie = HumieUp
    HumieX = 1
    HumieY = 1
    Move = False
