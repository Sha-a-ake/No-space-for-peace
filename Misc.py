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
        if self.x == C.HumieX and self.y == C.HumieY and self.PlayerOwned == False:
            print('Hit!')
        elif self.PlayerOwned and C.IdMap[self.x][self.y]:
            C.Bots[C.IdMap[self.x][self.y] - 1].GetHit(10) 
            self.Alive = False
        
          
    def Move(self):
        self.Impact()
        if   self.direction == 'up' and C.WalkMap[self.x][self.y-1] != 2:
            self.y -= 1
        elif self.direction == 'down' and C.WalkMap[self.x][self.y+1] != 2:
            self.y += 1
        elif self.direction == 'right' and C.WalkMap[self.x+1][self.y] != 2:
            self.x += 1
        elif self.direction == 'left' and C.WalkMap[self.x-1][self.y] != 2:
            self.x -= 1
        else:
            self.Alive = False
        self.Impact()

    def Draw(self):
        DISPLAY.blit(self.Model,((self.x+1)*TileSize, (self.y+1)*TileSize))
        
        
