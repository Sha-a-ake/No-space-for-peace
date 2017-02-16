# --- Does not work yet --- #

import pygame
from Const import *
import Config as C

class bullet:
    Alive = True
    
    def __init__(self,x,y,direction,power,PlayerOwned = False):
        self.x = x
        self.y = y
        self.direction = direction
        self.power = power
        self.PlayerOwned = PlayerOwned
        if direction == 'right' or direction == 'left': self.Model = BulletHor
        if direction == 'up' or direction == 'down': self.Model = BulletVer
    
    def Impact(self):
        if   C.WalkMap[self.x][self.y] == 2: self.Alive = False
        elif self.x == C.HumieX and self.y == C.HumieY and self.PlayerOwned == False:
            print('Hit!')
        elif self.PlayerOwned and C.IdMap[self.x][self.y]:
            C.Bots[C.IdMap[self.x][self.y] - 1].GetHit(10) 
            self.Alive = False
        
          
    def Move(self):
        if self.Alive == True:
            self.Impact()
            if   self.direction == 'up':
                self.y -= 1
            elif self.direction == 'down':
                self.y += 1
            elif self.direction == 'right':
                self.x += 1
            elif self.direction == 'left':
                self.x -= 1
            self.Impact()

    def Draw(self):
        DISPLAY.blit(self.Model,((self.x+1)*TileSize, (self.y+1)*TileSize))
        
        
