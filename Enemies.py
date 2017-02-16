import pygame, Misc, Game, Func
from Const import * 
import Config as C
from math import sqrt

class droid:
    Model = CalmDroidLeft
    Mode = 'Calm'
    Hp = 125
 
    Far = 5 # Константы
    Close = 2
    
    IsFar = IsClose = LineUp = None
    
    def __init__(self,X,Y,Id):
        self.X = X
        self.Y = Y
        self.Id = Id

    def Evaluate(self):
        Radius = sqrt((self.X-C.HumieX)**2 + (self.Y-C.HumieY)**2)
        if Radius >= self.Far: self.IsFar = True
        elif Radius <= self.Close: self.IsClose = True
        else: self.IsFar = False; self.IsClose = False

        if self.X == C.HumieX:
            if self.Y < C.HumieY: self.LineUp = 2
            else: self.LineUp = 8
        elif self.Y == C.HumieY:
            if self.X < C.HumieX: self.LineUp = 6
            else: self.LineUp = 4
        else: self.LineUp = 0
        

        
    #-----  Basic functions ----- #  
    
    def Draw(self):
        global DISPLAY
        DISPLAY.blit(self.Model,((self.X+1)*TileSize,(self.Y+1)*TileSize))    
        
    def Attack(self, direction):
        Bullet = Misc.bullet
        C.Misc.append(Bullet(self.X,self.Y,direction,10))
        
    def Move(self,direction,length = 1, attack = False):
        C.WalkMap[self.X][self.Y] = 0
        C.IdMap[self.X][self.Y] = 0
        
        if direction == 'up':
            if attack: self.Attack('up')
            self.Model = CalmDroidUp  
            for i in range(length):
                if C.WalkMap[self.X][self.Y-1] == 0:
                    self.Y -= 1
                    
        elif direction == 'down':
            if attack: self.Attack('down')
            self.Model = CalmDroidDown
            for i in range(length):
                if C.WalkMap[self.X][self.Y+1] == 0:
                    self.Y += 1
                                        
        elif direction == 'left':
            if attack: self.Attack('left')
            self.Model = CalmDroidLeft
            for i in range(length):
                if C.WalkMap[self.X-1][self.Y] == 0:   
                    self.X -= 1
                                        
        elif direction == 'right':
            if attack: self.Attack('right')
            self.Model = CalmDroidRight
            for i in range(length):
                if C.WalkMap[self.X+1][self.Y] == 0:
                    self.X += 1
                    
        C.WalkMap[self.X][self.Y] = 1
        C.IdMap[self.X][self.Y] = self.Id          
                    
    def Die(self):
        Game.Msg('I died for your sins')
        self.Mode = 'dead'
        self.Model = DeadDroidLeft
        C.WalkMap[self.X][self.Y] = 0
        C.IdMap[self.X][self.Y] = 0
        
    def GetHit(self,power):
        text = 'Getting Hit! Hp =' + str(self.Hp)
        Game.Msg(text)
        self.Hp -= power
        if self.Hp <= 0:
           self.Die() 
               
    # ----- Complex actions ----- #
          
    def MoveInLine(self,TargetX,TargetY):
         # Если расстояние до цели по иксу меньше чем по игреку
        if abs(TargetX - self.X) < abs(TargetY - self.Y):
            # Если цель правее / левее
            if TargetX > self.X:
                self.Move('right')
            elif TargetX < self.X:
                self.Move('left')
            # Если цель на одной линии 
            
            else:
                # цель выше/ниже
                if TargetY < self.Y:
                    self.Move('up',0,True)
                else:
                    self.Move('down',0,True)
            
        else:
            # Если цель выше/ниже
            if TargetY > self.Y:
                self.Move('down')
            elif TargetY < self.Y:
                self.Move('up')
            # цель на одной линии
            
            else:
                # Цель правее/левее
                if TargetX > self.X:
                    self.Move('right',0,True)
                else:
                    self.Move('left',0,True)
                        

    def MoveTo(self,x,y):
        direction = Func.FindPath(C.WalkMap,self.X,self.Y,x,y)
        self.Move(direction)
        
           
    def Turn(self):
        if self.Mode != 'dead':
            self.Evaluate()
##            self.MoveInLine(C.HumieX,C.HumieY)
            if self.IsFar != True:
                self.MoveTo(C.HumieX,C.HumieY)
            self.Evaluate()
      
                
                
                
                
                
            
