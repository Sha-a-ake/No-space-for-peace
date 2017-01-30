import random,math

def Btw(a,b,c):
    if (a > b > c or a < b < c): return True
    else: return False    
    
def CollisionTrue(x1,y1,x2,y2,X1,Y1,X2,Y2):
    if   Btw(x1,X1,x2) and Btw(y1,Y1,y2): T = True
    elif Btw(x1,X2,x2) and Btw(y1,Y2,y2): T = True
    elif Btw(x1,X1,x2) and Btw(y1,Y2,y2): T = True
    elif Btw(x1,X2,x2) and Btw(y1,Y1,y2): T = True
    else: T = False
    print('Check')
    return T  
    
def SquareCenter(x1,y1,x2,y2):
    return((x1+x2)/2),((y1+y2)/2)
    
def RandomPointInCircle(Radius):
    t = 2 * 3.141592 * random.random()
    u = random.random()+random.random()
    if u > 1: r = 2-u
    else: r = u
    return round(Radius*r*math.cos(t)), round(Radius*r*math.sin(t))
    
def MakeASquare(Radius):
    x1,y1 = RandomPointInCircle(Radius)
    x2,y2 = RandomPointInCircle(Radius)
    return(x1,y1,x2,y2)
    
def MakeSquaresInCircle(Rooms,Radius):
    Sq = []
    for i in range(Rooms):   
        Sq.append(MakeASquare(Radius))
    return(Sq)
    
def TupToLst(tup):
    lis = []
    for tuplette in tup:
        lis.append(list(tuplette))
    return(lis)
        
    
def Spread(Rooms):
    for z in range(len(Rooms)-1):
        for i in range(z,len(Rooms)):
            while CollisionTrue(Rooms[z][0],Rooms[z][1],Rooms[z][2],Rooms[z][3],
                             Rooms[i][0],Rooms[i][1],Rooms[i][2],Rooms[i][3],):
                x1,y1 = SquareCenter(Rooms[z][0],Rooms[z][1],Rooms[z][2],Rooms[z][3])
                x2,y2 = SquareCenter(Rooms[i][0],Rooms[i][1],Rooms[i][2],Rooms[i][3])
                print(x1,y1,x2,y2)
                if abs(x1 - x2) >= abs(y1-y2):
                    if x1 > x2:
                        Rooms[z][0] += 1
                        #Rooms[z][1] -= 1
                        Rooms[z][2] += 1
                        #Rooms[z][3] -= 1
                        print('Mov left')
                    elif x1 < x2:
                        Rooms[z][0] -= 1
                        #Rooms[z][1] += 1
                        Rooms[z][2] -= 1
                        #Rooms[z][3] += 1
                        print('Mov right')
        
                else:
                    if y1 > y2:
                        #Rooms[z][0] -= 1
                        Rooms[z][1] += 1
                        #Rooms[z][2] -= 1
                        Rooms[z][3] += 1
                        print('Mov up')
                    elif y2 > y1:
                        #Rooms[z][0] += 1
                        Rooms[z][1] -= 1
                        #Rooms[z][2] += 1
                        Rooms[z][3] -= 1
                        print('Mov down')
                print('Loop!', z,i)
    return Rooms
    
