import pygame
from Const import * 
import Config as C

class droid:
    Model = CalmDroidLeft
    Mode = 'Calm'
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        
    def Draw(self):
        global DISPLAY
        DISPLAY.blit(self.Model,((self.X+1)*24,(self.Y+1)*24))    
        
    def Move(self,TargetX,TargetY):
        C.Map[self.X][self.Y][2] = True
        if abs(TargetX - self.X) < abs(TargetY - self.Y):
            if TargetX > self.X:
                self.X += 1
                self.Model = CalmDroidRight
            elif TargetX < self.X:
                self.X -= 1
                self.Model = CalmDroidLeft
            else:
                if TargetY < self.Y:
                    self.Mode = 'AttackUp'
                    self.Model = CalmDroidUp
                else:
                    self.Mode = 'AttackDown'
                    self.Model = CalmDroidDown
            
        else :
            if TargetY > self.Y:
                self.Y += 1
                self.Model = CalmDroidDown
            elif TargetY < self.Y:
                self.Y -= 1
                self.Model = CalmDroidUp
            else:
                if TargetX > self.X:
                    self.Mode = 'AttackRight'
                    self.Model = CalmDroidRight
                else:
                    self.Mode = 'AttackLeft'
                    self.Model = CalmDroidLeft
        C.Map[self.X][self.Y][2] = False        
                
                
                
                
                
            
