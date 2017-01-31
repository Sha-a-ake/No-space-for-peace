import pygame
from Const import * 

class droid:
    Model = DeadDroidLeft
    Mode = 'Dead'
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
                self.Model = DeadDroidRight
            elif TargetX < self.X:
                self.X -= 1
                self.Model = DeadDroidLeft
            else:
                if TargetY < self.Y:
                    self.Mode = 'AttackUp'
                    self.Model = DeadDroidUp
                else:
                    self.Mode = 'AttackDown'
                    self.Model = DeadDroidDown
            
        else :
            if TargetY > self.Y:
                self.Y += 1
                self.Model = DeadDroidDown
            elif TargetY < self.Y:
                self.Y -= 1
                self.Model = DeadDroidUp
            else:
                if TargetX > self.X:
                    self.Mode = 'AttackRight'
                    self.Model = DeadDroidRight
                else:
                    self.Mode = 'AttackLeft'
                    self.Model = DeadDroidLeft
                
                
                
                
                
            
