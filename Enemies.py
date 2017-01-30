import pygame
from Const import * 

class droid:
    Model = DroidLeft
    Mode = 'Calm'
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        
    def Draw(self):
        global DISPLAY
        DISPLAY.blit(self.Model,((self.X+1)*24,(self.Y+1)*24))    
        
    def Move(self,TargetX,TargetY):
        if abs(TargetX - self.X) < abs(TargetY - self.Y):
            if TargetX > self.X:
                self.X += 1
                self.Model = DroidRight
            elif TargetX < self.X:
                self.X -= 1
                self.Model = DroidLeft
            else:
                if TargetY < self.Y:
                    self.Mode = 'AttackUp'
                    self.Model = DroidUp
                else:
                    self.Mode = 'AttackDown'
                    self.Model = DroidDown
            
        else :
            if TargetY > self.Y:
                self.Y += 1
                self.Model = DroidDown
            elif TargetY < self.Y:
                self.Y -= 1
                self.Model = DroidUp
            else:
                if TargetX > self.X:
                    self.Mode = 'AttackRight'
                    self.Model = DroidRight
                else:
                    self.Mode = 'AttackLeft'
                    self.Model = DroidLeft
                
                
                
                
                
            
