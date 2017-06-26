import Config as C
from Images import *
import Misc

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
            
def Attack():
    C.Move = True
    if C.Humie == HumieLeft:    Id = C.IdMap[C.HumieX -1][C.HumieY]              
    elif C.Humie == HumieRight: Id = C.IdMap[C.HumieX +1][C.HumieY]                
    elif C.Humie == HumieUp:    Id = C.IdMap[C.HumieX][C.HumieY -1]
    elif C.Humie == HumieDown:  Id = C.IdMap[C.HumieX][C.HumieY +1] 
    if Id:
        C.Bots[Id-1].GetHit(250)
   
def Shoot():
    C.Move = True
    if C.Humie == HumieLeft:    direction = 'left'              
    elif C.Humie == HumieRight: direction = 'right'                
    elif C.Humie == HumieUp:    direction = 'up'
    elif C.Humie == HumieDown:  direction = 'down'
    Bullet = Misc.bullet
    C.Misc.append(Bullet(C.HumieX,C.HumieY,direction,10,True))
