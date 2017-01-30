# Returns a blank map
def Create_Map(x,y):
    Map = []
    for i in range(y):
        Line = []
        for j in range(x):
            if (i == 0 or i == y-1):
                n = [2,False,False,False]
            # Type, Passable, Transparrant, Scouted 
            else:
                n = [1,False,False,False]
            Line.append(n)
        Map.append(Line)
    return(Map)
    
def Make_Level():
    print()
            
        
