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
    
def FindPath(Map,x1,y1,x2,y2,ReturnLen = False,Str = True):
    Y = len(Map)
    X = len(Map[0])
    A = []
    List = []
    for i in range(Y):
        A.append(['0'])
        for j in range(X):
            A[i].append('-')

    for i in range(Y):
        for j in range(X):
            if Map[i][j] == 0:
                A[i][j] = '0'
            else:
                A[i][j] = '|'
    
    y = x1
    x = y1
    A[y][x] = '1'
    A[x2][y2] = 'X'

    #Поиск
    List.append((y,x))
    for i in List:
        y,x = i[0],i[1]
        if A[y][x] == 'X':
            return((x1,y1))
        if A[y-1][x] == 'X':
            A[y-1][x] = str(int(A[y][x])+1)
            List = []
            List.append((y-1,x))
            y,x = y-1,x
            break
        if A[y][x-1] == 'X':
            A[y][x-1] = str(int(A[y][x])+1)
            List = []
            List.append((y,x-1))
            y,x = y,x-1
            break
        if A[y+1][x] == 'X':
            A[y+1][x] = str(int(A[y][x])+1)
            List = []
            List.append((y+1,x))
            y,x = y+1,x
            break
        if A[y][x+1] == 'X':
            A[y][x+1] = str(int(A[y][x])+1)
            List = []
            List.append((y,x+1))
            y,x = y,x+1
            break
        
        if A[y-1][x] == '0' and y-1 >= 0: #up
            A[y-1][x] = str(int(A[y][x])+1)
            List.append((y-1,x))
        if A[y][x-1] == '0' and x-1 >= 0: #left
            A[y][x-1] = str(int(A[y][x])+1)
            List.append((y,x-1))
        if A[y+1][x] == '0' and y+1 <= Y+1: #down
            A[y+1][x] = str(int(A[y][x])+1)
            List.append((y+1,x))
        if A[y][x+1] == '0' and x+1 <= X+1: #right
            A[y][x+1] = str(int(A[y][x])+1)
            List.append((y,x+1))
    else:
        return((x1,y1))
    
    if ReturnLen == True:
        return(int(A[List[0][1]][List[0][0]]))

    # Восстановление
    for i in List:
        if A[y-1][x] == '1':
            List.append((y-1,x))
            break
        if A[y][x-1] == '1':
            List.append((y,x-1))
            break
        if A[y+1][x] == '1':
            List.append((y+1,x))
            break
        if A[y][x+1] == '1':
            List.append((y,x+1))
            break
        
        if A[y-1][x] == str(int(A[y][x])-1):
            List.append((y-1,x))
            y,x = y-1,x
        if A[y][x-1] == str(int(A[y][x])-1):
            List.append((y,x-1))
            y,x = y,x-1
        if A[y+1][x] == str(int(A[y][x])-1):
            List.append((y+1,x))
            y,x = y+1,x
        if A[y][x+1] == str(int(A[y][x])-1):
            List.append((y,x+1))
            y,x = y,x+1

    List.reverse()
            
##    # Вывод для отладки
##    for i in List:
##        A[i[0]][i[1]] = '+'
##    print()
##    for i in A:
##        print(i)

    if Str == True:
        if List[1][1] - List[0][1] == -1: return('up')
        elif List[1][0] - List[0][0] == -1: return('left')
        elif List[1][1] - List[0][1] == 1: return('down')
        elif List[1][0] - List[0][0] == 1: return('right')
    else:
        return(List[1])
    
