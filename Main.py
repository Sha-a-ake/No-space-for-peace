import pygame, sys, Draw, Enemies, Func, Gen, Misc, Player, Game
import Config as C
from pygame.locals import *
from Const import *
from Images import *
from random import randint

pygame.init()
C.init()

# --- To remove later --- #
AreaX = 20; AreaY = 16
Gen.Create_Map(AreaX, AreaY)
Draw.Map(); 
Draw.Model(C.Humie,C.HumieX,C.HumieY)
Player.Move('right')





# Main game loop
def Loop():
    
    C.Move = True
    while True:
        # Checking for player actions
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Movement
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RIGHT:
                    Player.Move('right')
                        
                elif event.key == pygame.K_LEFT:
                    Player.Move('left')
                      
                elif event.key == pygame.K_UP:
                    Player.Move('up')
                        
                elif event.key == pygame.K_DOWN:
                    Player.Move('down')
                    
                    
                elif event.key == pygame.K_SPACE:
                    Player.Attack() 
                        
                elif event.key == pygame.K_LCTRL:
                    Player.Shoot()

                    
                elif event.key == pygame.K_ESCAPE:
                    menu = Game.Menu('pause')
                    if menu == 0: pass
                    if menu == 1: return(0)   
                    if menu == 2: pygame.quit(); sys.exit();
            
            # Calculating enviroment reaction  
            if C.Move == True:
                #continue
                for Bot in C.Bots:
                    Bot.Turn()
                for Misc in C.Misc:
                    Misc.Move()
                for Misc in C.Misc:
                    if Misc.Alive == False:
                        C.Misc.remove(Misc)


            
            DISPLAY.fill(BLACK) 
            
            # Drawing things
            Draw.Map()
            #Draw.WalkMap()
            
            
            #input()
            Draw.Model(C.Humie,C.HumieX,C.HumieY)
            
            for Bot in C.Bots:
                Bot.Draw()
            Draw.Model(C.Humie,C.HumieX,C.HumieY)
            for Misc in C.Misc:
                Misc.Draw()
            Draw.MsgBox()
            
            C.Move = False # if True, activates move
            
            
        pygame.display.update()
        FpsClock.tick(FPS)
        

# Create an enemy of chosen type
def Spawn(EnemyType, x=randint(0,AreaX-1), y=randint(0,AreaY-1), Id = 'Null'): # Spawn Enemy in x,y
    if EnemyType == 'Droid':
        Enemy = Enemies.droid
        C.Bots.append(Enemy(x,y,Id))            

# Creating a bunch of enemies for testing                
for k in range(1,9):
    Spawn('Droid', k+2,k+2,k)
    C.IdMap[k+2][k+2] = k


# Запуск
while True:
    menu = Game.Menu('main')
    if menu == 0:
        Loop()
    elif menu == 1:
        menu == Game.Menu('set')
        if menu == 0: continue
    elif menu == 2: pygame.quit(); sys.exit();
