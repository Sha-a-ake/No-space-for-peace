import Config as C

def Create_Map(x,y):
    C.Map = []
    for i in range(x):
        Line = []
        for j in range(y):
            
            """
            Type status:
            
            0 == Floor
            
            11 == Horizontal Wall Top
            12 == Horizontal Wall Bottom
            21 == Vertical Wall Left
            22 == Vertical Wall Right
            
            31 == Top Left Corner
            32 == Top Right Corner
            41 == Bottom Left Corner
            42 == Bottom Right Corner
            
            51 == Special Vertical Wall Left
            52 == Special Vertical Wall Right
            61 == Special Horizontal Wall Top
            62 == Special Horizontal Wall Bottom
            
            """
            
            if i == 0 or j == 0 or i == x-1 or j == y-1:
                if i == 0:
                    if j == 0:
                        n = [31,0,False,False,False] 
                    elif j == y-1:
                        n = [41,0,False,False,False]
                    else:
                        n = [21,0,False,False,False] # Left Wall
                        
                elif j == 0:
                    if i == x-1:
                        n = [32,0,False,False,False]
                    else:
                        n = [11,0,False,False,False] # Top Wall
                        
                elif i == x-1:
                    if j == y-1:
                        n = [42,0,False,False,False]
                    else:
                        n = [22,0,False,False,False] # Right Wall                    
                    
                elif j == y-1:                       # Bottom Wall
                    n = [12,0,False,False,False]
            
            else:
                n = [0,0,True,False,False]                                
                
            Line.append(n)
        C.Map.append(Line)
        
