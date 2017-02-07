# --- Does not work yet --- #

import pygame
from Const import *
import Config as C

class bullet:
    Alive = True
    
    def __init__(self,x,y,direction,power):
        self.x = x
        self.y = y
        self.direction = direction
        self.power = power
        if direction == 'right' or direction == 'left': self.Model = BulletHor
        if direction == 'up' or direction == 'down': self.Model = BulletVer
    
    def Impact(self):
        if   C.Map[self.x][self.y][2] == False: self.Alive = False
        #elif C.Map[self.x][self.y][3] == False:
        
        
            
    def Move(self):
        if   self.direction == 'up':
             self.y -= 1
        elif self.direction == 'down':
             self.y += 1
        elif self.direction == 'right':
             self.x += 1
        else:
             self.x -= 1
        print('Cords',self.x,self.y)
        self.Impact()
            
    def Draw(self):
        DISPLAY.blit(self.Model,((self.x+1)*24,(self.y+1)*24))
        
        
        
