import pygame
from Const import * 

class droid:
    Model = PreparedDroidLeft
    Mode = 'Prepared'
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
                self.Model = PreparedDroidRight
            elif TargetX < self.X:
                self.X -= 1
                self.Model = PreparedDroidLeft
            else:
                if TargetY < self.Y:
                    self.Mode = 'AttackUp'
                    self.Model = PreparedDroidUp
                else:
                    self.Mode = 'AttackDown'
                    self.Model = PreparedDroidDown
            
        else :
            if TargetY > self.Y:
                self.Y += 1
                self.Model = PreparedDroidDown
            elif TargetY < self.Y:
                self.Y -= 1
                self.Model = PreparedDroidUp
            else:
                if TargetX > self.X:
                    self.Mode = 'AttackRight'
                    self.Model = PreparedDroidRight
                else:
                    self.Mode = 'AttackLeft'
                    self.Model = PreparedDroidLeft
                
                
                
                
                
            
