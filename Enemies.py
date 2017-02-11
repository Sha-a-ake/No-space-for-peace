import pygame, Misc, Game, Func
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
        if self.Mode != 'dead' and abs(self.X-TargetX) > 1 and abs(self.Y-TargetY) > 1:
            if abs(TargetX - self.X) < abs(TargetY - self.Y):
                if TargetX > self.X:
                    self.Model = CalmDroidRight
                elif TargetX < self.X:
                    self.Model = CalmDroidLeft
                else:
                    if TargetY < self.Y:
                        self.Model = CalmDroidUp
                    else:
                        self.Model = CalmDroidDown
            else :
                if TargetY > self.Y:
                    self.Model = CalmDroidDown
                elif TargetY < self.Y:
                    self.Model = CalmDroidUp
                else:
                    if TargetX > self.X:
                        self.Model = CalmDroidRight
                    else:
                        self.Model = CalmDroidLeft
                
            try:
                cords = Func.FindPath(C.Map,self.X,self.Y,TargetX,TargetY)
                for i in range(len(C.Bots)):
                    C.Map[C.Bots[i].X][C.Bots[i].Y][2] = True
                self.X = cords[0]
                self.Y = cords[1]
                for i in range(len(C.Bots)):
                    if C.Bots[i].Mode != 'dead':
                        C.Map[C.Bots[i].X][C.Bots[i].Y][2] = False
            except: pass

        
        
    def Die(self):
        print('I died for your sins')
        Game.Msg('I died for your sins')
        self.Mode = 'dead'
        self.Model = DeadDroidLeft
        C.Map[self.X][self.Y][3] = True
        
    def GetHit(self,x,y,power):
        if self.X == x and self.Y == y:
            print('Getting Hit! Hp =', self.Hp)
            text = 'Getting Hit! Hp =' + str(self.Hp)
            Game.Msg(text)
            self.Hp -= power
            if self.Hp <= 0:
               self.Die()   
                
                
                
                
                
            
