import pygame
import Config as C
from Const import *
"""
            Type status:
            
            0 == Floor
            
            11 == Wall Horizontal Top
            12 == Wall Horizontal Bottom
            21 == Wall Vertical Left
            22 == Wall Vertical Right
            
            31 == Top Left Corner
            32 == Top Right Corner
            41 == Bottom Left Corner
            42 == Bottom Right Corner
            
            51 == Special Vertical Wall Left
            52 == Special Vertical Wall Right
            61 == Special Horizontal Wall Top
            62 == Special Horizontal Wall Bottom
            
"""

def Map():
    x = 0;
    for Line in C.Map:
        y = 0
        x += TileSize
        for X in Line:
            y += TileSize
            if X[0] == 0: DISPLAY.blit(Floor, (x,y))
            elif X[0] == 11: DISPLAY.blit(WallHorTop, (x,y))
            elif X[0] == 12: DISPLAY.blit(WallHorBottom, (x,y))
            elif X[0] == 21: DISPLAY.blit(WallVerLeft, (x,y))
            elif X[0] == 22: DISPLAY.blit(WallVerRight, (x,y))
            elif X[0] == 31: DISPLAY.blit(WallCornerTL, (x,y))
            elif X[0] == 32: DISPLAY.blit(WallCornerTR, (x,y))
            elif X[0] == 41: DISPLAY.blit(WallCornerBL, (x,y))
            elif X[0] == 42: DISPLAY.blit(WallCornerBR, (x,y))
            
def WalkMap():
    x = 0;
    for Line in C.Map:
        y = 0
        x += TileSize
        for X in Line:
            y += TileSize
            if   X[2] == False: DISPLAY.blit(RedCell, (x,y))
            elif X[3] == False: DISPLAY.blit(OrangeCell, (x,y))
            else:               DISPLAY.blit(GreenCell, (x,y))
            
            
def Model(Humie,x,y):
    DISPLAY.blit(Humie,((x+1)*24,(y+1)*24))
    
def Square(X1,Y1,X2,Y2):
    x = X1*24; y = Y1*24
    for Line in range(abs(X2-X1+1)):
        x = X1*24
        y += TileSize
        for X in range(abs(Y2-Y1+1)):
            x += TileSize
            DISP.blit(Tile, (x,y))
