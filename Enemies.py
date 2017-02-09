import pygame, Misc
from Const import * 
import Config as C

class droid:
    Model = CalmDroidLeft
    Mode = 'Calm'
    Hp = 25
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def Draw(self):
        global DISPLAY
        DISPLAY.blit(self.Model,((self.x+1)*TileSize,(self.y+1)*TileSize))    
        
    def Attack(self, direction):
        Bullet = Misc.bullet
        C.Misc.append(Bullet(self.x,self.y,direction,10))    
        
    def Move(self,TargetX,TargetY):
        if self.Mode != 'dead':
            C.Map[self.x][self.y][3] = True
            if abs(TargetX - self.x) < abs(TargetY - self.y):
                if TargetX > self.x:
                    self.x += 1
                    self.Model = CalmDroidRight
                elif TargetX < self.x:
                    self.x -= 1
                    self.Model = CalmDroidLeft
                else:
                    if TargetY < self.y:
                        self.Attack('up')
                        self.Model = CalmDroidUp
                    else:
                        self.Attack('down')
                        self.Model = CalmDroidDown
            
            else :
                if TargetY > self.y:
                    self.y += 1
                    self.Model = CalmDroidDown
                elif TargetY < self.y:
                    self.y -= 1
                    self.Model = CalmDroidUp
                else:
                    if TargetX > self.x:
                        self.Attack('right')
                        self.Model = CalmDroidRight
                    else:
                        self.Attack('left')
                        self.Model = CalmDroidLeft
            C.Map[self.x][self.y][3] = False    
        
    def Die(self):
        print('I died for your sins')
        self.Mode = 'dead'
        self.Model = DeadDroidLeft
        C.Map[self.x][self.y][3] = True
        
    def GetHit(self,x,y,power):
        if self.x == x and self.y == y:
            print('Getting Hit! Hp =', self.Hp)
            self.Hp -= power
            if self.Hp <= 0:
               self.Die()   
                
                
                
                
                
            
