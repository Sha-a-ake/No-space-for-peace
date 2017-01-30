import pygame
from Const import * 

class droid:
    Model = 
    Mode = 'Calm'
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        
    def Draw(self):
        global DISPLAY
        DISPLAY.blit(Model,((x+1)*24,(y+1)*24))    
        
    def Move(self,TargetX,TargetY):
        if abs(TargetX - self.X) > abs(TargetY - self.Y):
            if TargetX > self.X:
                self.X += 1
            elif TargetX < self.X:
                self.X -= 1
            else:
                if TargetY < Y:
                    self.Mode = 'AttackUp'
                    self.Model = DroidUp
                else:
                    self.Mode = 'AttackDown'
                    self.Model = DroidDown
            
        else :
            if TargetY > self.Y:
                self.Y += 1
            elif TargetY < self.Y:: 
                self.Y -= 1
            else:
                if TargetX > X:
                    self.Mode = 'AttackRight'
                    self.Model = DroidRight
                else:
                    self.Mode = 'AttackLeft'
                    self.Model = DroidLeft
                
                
                
                
                
            
