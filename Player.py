import Config as C
from Images import *

def Move(direction):
    C.Move = True
    
    C.WalkMap[C.HumieX][C.HumieY] = 0
    
    if direction == 'right':
        C.Humie = HumieRight
        if C.WalkMap[C.HumieX+1][C.HumieY] == False:
            C.HumieX += 1        
    elif direction == 'left':
        C.Humie = HumieLeft
        if C.WalkMap[C.HumieX-1][C.HumieY] == False:
            C.HumieX -= 1        
    elif direction == 'up':
        C.Humie = HumieUp
        if C.WalkMap[C.HumieX][C.HumieY-1] == False:
            C.HumieY -= 1
    elif direction == 'down':
        C.Humie = HumieDown
        if C.WalkMap[C.HumieX][C.HumieY+1] == False:
            C.HumieY += 1

    C.WalkMap[C.HumieX][C.HumieY] = 3
            
def Attack(direction):
    print(C.IdMap[C.HumieX][C.HumieY])
    C.Move = True
    if direction == 'up':       Id = C.IdMap[C.HumieX][C.HumieY -1]
    elif direction == 'down':   Id = C.IdMap[C.HumieX][C.HumieY +1] 
    elif direction == 'right':  Id = C.IdMap[C.HumieX +1][C.HumieY]
    elif direction == 'left':   Id = C.IdMap[C.HumieX -1][C.HumieY]
    
    if Id:
        C.Bots[Id-1].GetHit(10)
    
