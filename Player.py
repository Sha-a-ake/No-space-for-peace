import Config as C
from Images import *

def Move(direction):
    C.Move = True
    
    C.Map[C.HumieX][C.HumieY][3] = True
    
    if direction == 'right':
        C.Humie = HumieRight
        if C.Map[C.HumieX+1][C.HumieY][2] == True and C.Map[C.HumieX+1][C.HumieY][3] == True:
            C.HumieX += 1        
    elif direction == 'left':
        C.Humie = HumieLeft
        if C.Map[C.HumieX-1][C.HumieY][2] == True and C.Map[C.HumieX-1][C.HumieY][3] == True:
            C.HumieX -= 1        
    elif direction == 'up':
        C.Humie = HumieUp
        if C.Map[C.HumieX][C.HumieY-1][2] == True and C.Map[C.HumieX][C.HumieY-1][3] == True:
            C.HumieY -= 1
    elif direction == 'down':
        C.Humie = HumieDown
        if C.Map[C.HumieX][C.HumieY+1][2] == True and C.Map[C.HumieX][C.HumieY+1][3] == True:
            C.HumieY += 1

    C.Map[C.HumieX][C.HumieY][3] = False
            
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
