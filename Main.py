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



def Menu(arg):
    choice = 0
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    
    if arg == 'main':
        while True:
            
            text0 = fontObj.render('Новая Игра', True, WHITE)
            text1 = fontObj.render('Настройки', True, WHITE)
            text2 = fontObj.render('Выход', True, WHITE)
            text = [text0,text1,text2]
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        if choice == 0: return(0)
                        if choice == 1: return(1)
                        if choice == 2: return(2)
                    if event.key == pygame.K_DOWN:
                        if choice < 2: choice += 1
                        else: choice = 0
                    if event.key == pygame.K_UP:
                        if choice > 0: choice -= 1
                        else: choice = 2

            if choice == 0: text0 = fontObj.render('Новая Игра', True, BLUE)
            if choice == 1: text1 = fontObj.render('Настройки', True, BLUE)
            if choice == 2: text2 = fontObj.render('Выход', True, BLUE)
       
            DISPLAY.fill(BLACK)
            DISPLAY.blit(text0,(220,120))
            DISPLAY.blit(text1,(220,220))
            DISPLAY.blit(text2,(220,320))
            pygame.display.update()
            FpsClock.tick(FPS)
    if arg == 'pause':
        while True:
            
            text0 = fontObj.render('Продолжить', True, WHITE)
            text1 = fontObj.render('Главное Меню', True, WHITE)
            text2 = fontObj.render('Выход', True, WHITE)
            text = [text0,text1,text2]
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        if choice == 0: return(0)
                        if choice == 1: return(1)
                        if choice == 2: return(2)
                    if event.key == pygame.K_DOWN:
                        if choice < 2: choice += 1
                        else: choice = 0
                    if event.key == pygame.K_UP:
                        if choice > 0: choice -= 1
                        else: choice = 2
                    if event.key == pygame.K_ESCAPE: return(0)

            if choice == 0: text0 = fontObj.render('Продолжить', True, BLUE)
            if choice == 1: text1 = fontObj.render('Главное Меню', True, BLUE)
            if choice == 2: text2 = fontObj.render('Выход', True, BLUE)
       
            
            DISPLAY.blit(text0,(220,120))
            DISPLAY.blit(text1,(220,220))
            DISPLAY.blit(text2,(220,320))
            pygame.display.update()
            FpsClock.tick(FPS)

    if arg == 'set':
        while True:
            
            text0 = fontObj.render('Назад', True, BLUE)
            text = [text0]
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        return(0)

            DISPLAY.fill(BLACK)
            DISPLAY.blit(text0,(220,220))
            pygame.display.update()
            FpsClock.tick(FPS)
    if arg == 'exit':
        pygame.quit()
        sys.exit()

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
                        
                if event.key == pygame.K_LEFT:
                    Player.Move('left')
                      
                if event.key == pygame.K_UP:
                    Player.Move('up')
                        
                if event.key == pygame.K_DOWN:
                    Player.Move('down')
                    
                    
                if event.key == pygame.K_SPACE:
                    C.Move = True
                    if C.Humie == HumieLeft:
                        for Bot in C.Bots:
                            Bot.GetHit(C.HumieX-1,C.HumieY,30)
                    if C.Humie == HumieRight:
                        for Bot in C.Bots:
                            Bot.GetHit(C.HumieX+1,C.HumieY,30)
                    if C.Humie == HumieUp:
                        for Bot in C.Bots:
                            Bot.GetHit(C.HumieX,C.HumieY-1,30)
                    if C.Humie == HumieDown:
                        for Bot in C.Bots:
                            Bot.GetHit(C.HumieX,C.HumieY+1,30) 
                    
                if event.key == pygame.K_ESCAPE:
                    menu = Menu('pause')
                    if menu == 0: pass
                    if menu == 1: return(0)   
                    if menu == 2: pygame.quit(); sys.exit();
            
            # Calculating enviroment reaction  
            if C.Move == True:
            
                for Bot in C.Bots:
                    Bot.Turn()
                for Misc in C.Misc:
                    Misc.Move()
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
def Spawn(EnemyType, x=randint(0,AreaX-1), y=randint(0,AreaY-1)): # Spawn Enemy in x,y
    if EnemyType == 'Droid':
        Enemy = Enemies.droid
        C.Bots.append(Enemy(x,y))            

# Creating a bunch of enemies for testing                
for k in range(6,9):
    Spawn('Droid', k+2,k+2)


# Запуск
while True:
    menu = Menu('main')
    if menu == 0:
        Loop()
    elif menu == 1:
        menu == Menu('set')
        if menu == 0: continue
    elif menu == 2: pygame.quit(); sys.exit();
