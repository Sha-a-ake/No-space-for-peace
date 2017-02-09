import pygame, Misc
from Const import * 
import Config as C

class droid:
    Model = CalmDroidLeft
    Mode = 'Calm'
    Hp = 25
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        
    def Draw(self):
        global DISPLAY
        DISPLAY.blit(self.Model,((self.X+1)*TileSize,(self.Y+1)*TileSize))    
        
    def Attack(self, direction):
        Bullet = Misc.bullet
        C.Misc.append(Bullet(self.X,self.Y,direction,10))    
        
    def Move(self,TargetX,TargetY):
        if self.Mode != 'dead':
            C.Map[self.X][self.Y][3] = True
            if abs(TargetX - self.X) < abs(TargetY - self.Y):
                if TargetX > self.X:
                    self.X += 1
                    self.Model = CalmDroidRight
                elif TargetX < self.X:
                    self.X -= 1
                    self.Model = CalmDroidLeft
                else:
                    if TargetY < self.Y:
                        self.Attack('up')
                        self.Model = CalmDroidUp
                    else:
                        self.Attack('down')
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
                        self.Attack('right')
                        self.Model = CalmDroidRight
                    else:
                        self.Attack('left')
                        self.Model = CalmDroidLeft
            C.Map[self.X][self.Y][3] = False    
        
    def Die(self):
        print('I died for your sins')
        self.Mode = 'dead'
        self.Model = DeadDroidLeft
        C.Map[self.X][self.Y][3] = True
        
    def GetHit(self,x,y,power):
        if self.X == x and self.Y == y:
            print('Getting Hit! Hp =', self.Hp)
            self.Hp -= power
            if self.Hp <= 0:
               self.Die()   
                
                
                
                
                
            
