# --- Does not work yet --- #

import pygame
from Const import *
import Config as C

class bullet:
    Model = BulletHor
    
    def __init__(self,x,y,direction,power):
        self.x = x
        self.y = y
        self.direction = direction
        self.power = power
        
    def Move(self):
        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'right':
            self.x += 1
        else:
            self.x -= 1
            
    def Draw(self):
        DISPLAY.blit(self.Model,((self.x+1)*24,(self.y+1)*24))
        
        
        
