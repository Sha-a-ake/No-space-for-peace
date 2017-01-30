# Returns a blank map
def Create_Map(x,y):
    Map = []
    for i in range(x):
        Line = []
        for j in range(y):
            """
            Type status:
            
            0 == Floor
            1 == Vertical Wall
            2 == Horizontal Wall
            3 == Special Vertical Wall
            4 == Special Horizontal Wall
            
            """
            n = [0,0,True,False,False]
            if (i == 0 or i == x-1) and (j != 0 and j != y-1):
                n = [2,0,False,False,False]
            elif (j == 0 or j == y-1) and (i != 0 and i != x-1):
                n = [1,0,False,False,False]
            else:   
                n = [0,0,True,False,False]
            Line.append(n)
        Map.append(Line)
    return(Map)
    
def Make_Level():
    print()
            
        
