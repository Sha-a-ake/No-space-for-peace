from Const import *
from pygame.locals import *
import pygame

Messages = ['0']*MsgBox_height
def Msg(message = None): # Send message to MessageBox
    global Messages
    if message != None:
        Messages = Messages[1:]
        Messages.append(message)
    return(Messages)


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
