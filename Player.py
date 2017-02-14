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
            
    def Attack():
        C.Move = True
        if C.Humie == HumieLeft:
            for Bot in C.Bots:
                Bot.GetHit(C.HumieX-1,C.HumieY,30)
        if C.Humie == HumieRight:
            for Bot in C.Bots:
                Bot.GetHit(C.HumieX+1,C.HumieY,30)
        if C.Humie == HumieUp:
            for Bot in C.Bots:
                Bot.GetHit(C.HumieX,C.HumieY-1,30)
        if C.Humie == HumieDown:
            for Bot in C.Bots:
                Bot.GetHit(C.HumieX,C.HumieY+1,30)    
    def hi():
        print('hi')   
